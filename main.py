import asyncio
import os
from datetime import date

import bs4  # type: ignore
import pyluach.dates  # type: ignore
from telebot import AsyncTeleBot
from telebot.util import smart_split

from sefaria import load_sefaria_tractate
from tractates import get_daf

TELEGRAM_ALLOWED_TAGS = ["b", "i", "u", "s", "a"]
TELEGRAM_TAG_MAPPING = {
    "strong": "u",
}
TELEGRAM_CHAR_MAPPING = {
    "§": "➡️",
}


def preprocess_paragraph(paragraph: str) -> str:
    soup = bs4.BeautifulSoup(paragraph, features="html.parser")
    for tag in soup.descendants:
        if not isinstance(tag, bs4.Tag):
            continue
        if tag.name in TELEGRAM_ALLOWED_TAGS:
            continue
        mapped_tag_name = TELEGRAM_TAG_MAPPING.get(tag.name)
        if mapped_tag_name is None:
            raise ValueError(f"No mapping exists for tag: {tag.name}")
        tag.name = mapped_tag_name
    processed = str(soup)
    for old, new in TELEGRAM_CHAR_MAPPING.items():
        processed = processed.replace(old, new)
    return processed


def format_daf(d: date) -> list[str]:
    daf = get_daf(d)
    if daf is None:
        raise ValueError(f"No daf found for the date: {d}")
    book = load_sefaria_tractate(daf.tractate)
    messages: list[str] = []

    paragraphs: list[str] = []

    if daf.page == daf.tractate.start_page:
        paragraphs.append(f"📕 Tractate {daf.tractate} ({book['heTitle']})")

    hebrew_date = pyluach.dates.GregorianDate.from_pydate(d).to_heb()
    assert hebrew_date is not None
    header_lines = [
        f"🗓️ {d.strftime('%B %-d %Y')} / {hebrew_date.month_name()} {hebrew_date.day} {hebrew_date.year}"
    ]
    festival = hebrew_date.festival(prefix_day=True)
    if festival:
        header_lines.append("🎉" + festival)
    header_lines.append(f"\n<b>{daf}</b>")

    paragraphs.append("\n".join(header_lines))
    for subpage in ("a", "b"):
        url = daf.url(subpage)  # type: ignore
        paragraphs.append(f'📜 <a href="{url}">{daf.page}{subpage}</a>')
        raw_paragraphs = book["text"][2 * (daf.page - 1) + (0 if subpage == "a" else 1)]

        split_paragraphs: list[str] = []
        for p in raw_paragraphs:
            split_paragraphs.extend(p.split("<br/>"))
        paragraphs.extend(preprocess_paragraph(p) for p in split_paragraphs)

        messages.append("\n\n".join(paragraphs))
        paragraphs.clear()
    return messages


async def main() -> None:
    bot = AsyncTeleBot(token=os.environ["TOKEN"])
    channel_id = os.environ["CHANNEL_ID"]
    d = date.today()
    print(f"Reading daf for today: {d}")
    message_texts = format_daf(d)
    print(f"Sending daf: {message_texts[0][:128]}...")
    for text in message_texts:
        for text_part in smart_split(text):
            await bot.send_message(
                chat_id=channel_id,
                text=text_part,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )
            await asyncio.sleep(1)
    print("Done!")


if __name__ == "__main__":
    asyncio.run(main())
