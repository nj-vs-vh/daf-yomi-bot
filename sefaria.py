import json
from pathlib import Path
from typing import TypedDict

from tractates import Tractate


class SefariaBook(TypedDict):
    language: str
    title: str
    versionSource: str
    versionTitle: str
    actualLanguage: str
    languageFamilyName: str
    isSource: bool
    isPrimary: bool
    direction: str
    status: str
    priority: float
    license: str
    versionNotes: str
    versionTitleInHebrew: str
    versionNotesInHebrew: str
    shortVersionTitle: str
    purchaseInformationImage: str
    purchaseInformationURL: str
    heTitle: str
    categories: list[str]
    text: list[list[str]]
    sectionNames: list[str]


BOOKS_DIR = Path(__file__).parent / "json"


def load_sefaria_tractate(tractate: Tractate) -> SefariaBook:
    file_prefix = tractate.url.split("/")[-1].replace("_", " ")
    book_json_matches = [
        f for f in BOOKS_DIR.iterdir() if f.name.startswith(file_prefix)
    ]
    if not book_json_matches:
        raise FileNotFoundError(
            f"Sefaria book json not found for {tractate}, expected prefix: {file_prefix}"
        )
    elif len(book_json_matches) > 1:
        raise FileNotFoundError(
            f"More than one file matches the prefix {file_prefix}: {book_json_matches}"
        )
    return json.loads(book_json_matches[0].read_text())
