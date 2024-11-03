import asyncio
import os
from datetime import date

import bs4  # type: ignore
from telebot import AsyncTeleBot  # type: ignore

from sefaria import load_sefaria_tractate
from tractates import get_daf

TELEGRAM_ALLOWED_TAGS = ["b", "i", "u", "s", "a"]
TELEGRAM_TAG_MAPPING = {
    "strong": "u",
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
    return str(soup)


def format_daf(d: date) -> str:
    daf = get_daf(d)
    if daf is None:
        raise ValueError(f"No daf found for the date: {d}")
    book = load_sefaria_tractate(daf.tractate)
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
    return "\n\n".join(paragraphs)


async def main() -> None:
    bot = AsyncTeleBot(token=os.environ["TOKEN"])
    channel_id = os.environ["CHANNEL_ID"]
    message = format_daf(date.today())
    await bot.send_message(chat_id=channel_id, text=message)


if __name__ == "__main__":
    asyncio.run(main())
