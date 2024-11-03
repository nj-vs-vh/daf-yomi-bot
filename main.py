import asyncio
import os
from datetime import date

import bs4  # type: ignore
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


def preprocess_for_telegram(paragraph: str) -> str:
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

    paragraphs.append(f"🗓️ <b>{d.strftime('%-d %b %Y')} - {daf}</b>")
    for subpage in ("a", "b"):
        url = daf.url(subpage)  # type: ignore
        paragraphs.append(f'📜 <a href="{url}">{daf.page}{subpage}</a>')
        subpage_paragraphs = book["text"][
            2 * (daf.page - 1) + (0 if subpage == "a" else 1)
        ]
        paragraphs.extend(preprocess_for_telegram(p) for p in subpage_paragraphs)

        messages.append("\n\n".join(paragraphs))
        paragraphs.clear()
    return messages


async def main() -> None:
    bot = AsyncTeleBot(token=os.environ["TOKEN"])
    channel_id = os.environ["CHANNEL_ID"]
    d = date.today()
    print(f"Reading daf for today: {d}")
    message_texts = format_daf(date.today())
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
