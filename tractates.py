from dataclasses import dataclass
from datetime import date, datetime
import itertools
from typing import Literal


@dataclass
class Tractate:
    name: str
    start_date: date
    end_date: date
    start_page: int
    url: str

    def __str__(self) -> str:
        return f"{self.name} ({self.start_date} - {self.end_date})"


tractates = [
    Tractate(
        name="Berakhot",
        start_date=date(2020, 1, 5),
        end_date=date(2020, 3, 7),
        start_page=2,
        url="https://www.sefaria.org/Berakhot",
    ),
    Tractate(
        name="Shabbat",
        start_date=date(2020, 3, 8),
        end_date=date(2020, 8, 10),
        start_page=2,
        url="https://www.sefaria.org/Shabbat",
    ),
    Tractate(
        name="Eruvin",
        start_date=date(2020, 8, 11),
        end_date=date(2020, 11, 22),
        start_page=2,
        url="https://www.sefaria.org/Eruvin",
    ),
    Tractate(
        name="Pesachim",
        start_date=date(2020, 11, 23),
        end_date=date(2021, 3, 22),
        start_page=2,
        url="https://www.sefaria.org/Pesachim",
    ),
    Tractate(
        name="Shekalim",
        start_date=date(2021, 3, 23),
        end_date=date(2021, 4, 12),
        start_page=1,
        url="https://www.sefaria.org/Mishnah_Shekalim",
    ),
    Tractate(
        name="Yoma",
        start_date=date(2021, 4, 13),
        end_date=date(2021, 7, 8),
        start_page=2,
        url="https://www.sefaria.org/Yoma",
    ),
    Tractate(
        name="Sukkah",
        start_date=date(2021, 7, 9),
        end_date=date(2021, 9, 1),
        start_page=2,
        url="https://www.sefaria.org/Sukkah",
    ),
    Tractate(
        name="Beitzah",
        start_date=date(2021, 9, 2),
        end_date=date(2021, 10, 10),
        start_page=2,
        url="https://www.sefaria.org/Beitzah",
    ),
    Tractate(
        name="Rosh Hashanah",
        start_date=date(2021, 10, 11),
        end_date=date(2021, 11, 13),
        start_page=2,
        url="https://www.sefaria.org/Rosh_Hashanah",
    ),
    Tractate(
        name="Taanit",
        start_date=date(2021, 11, 14),
        end_date=date(2021, 12, 13),
        start_page=2,
        url="https://www.sefaria.org/Taanit",
    ),
    Tractate(
        name="Megillah",
        start_date=date(2021, 12, 13),
        end_date=date(2022, 1, 13),
        start_page=2,
        url="https://www.sefaria.org/Megillah",
    ),
    Tractate(
        name="Moed Katan",
        start_date=date(2022, 1, 14),
        end_date=date(2022, 2, 10),
        start_page=2,
        url="https://www.sefaria.org/Moed_Katan",
    ),
    Tractate(
        name="Chagigah",
        start_date=date(2022, 2, 11),
        end_date=date(2022, 3, 8),
        start_page=2,
        url="https://www.sefaria.org/Chagigah",
    ),
    Tractate(
        name="Yevamot",
        start_date=date(2022, 3, 9),
        end_date=date(2022, 7, 7),
        start_page=2,
        url="https://www.sefaria.org/Yevamot",
    ),
    Tractate(
        name="Ketubot",
        start_date=date(2022, 7, 8),
        end_date=date(2022, 10, 26),
        start_page=2,
        url="https://www.sefaria.org/Ketubot",
    ),
    Tractate(
        name="Nedarim",
        start_date=date(2022, 10, 27),
        end_date=date(2023, 1, 24),
        start_page=2,
        url="https://www.sefaria.org/Nedarim",
    ),
    Tractate(
        name="Nazir",
        start_date=date(2023, 1, 25),
        end_date=date(2023, 3, 30),
        start_page=2,
        url="https://www.sefaria.org/Nazir",
    ),
    Tractate(
        name="Sotah",
        start_date=date(2023, 3, 31),
        end_date=date(2023, 5, 17),
        start_page=2,
        url="https://www.sefaria.org/Sotah",
    ),
    Tractate(
        name="Gittin",
        start_date=date(2023, 5, 18),
        end_date=date(2023, 8, 14),
        start_page=2,
        url="https://www.sefaria.org/Gittin",
    ),
    Tractate(
        name="Kiddushin",
        start_date=date(2023, 8, 15),
        end_date=date(2023, 11, 3),
        start_page=2,
        url="https://www.sefaria.org/Kiddushin",
    ),
    Tractate(
        name="Bava Kamma",
        start_date=date(2023, 11, 4),
        end_date=date(2024, 2, 29),
        start_page=2,
        url="https://www.sefaria.org/Bava_Kamma",
    ),
    Tractate(
        name="Bava Metzia",
        start_date=date(2024, 3, 1),
        end_date=date(2024, 6, 26),
        start_page=2,
        url="https://www.sefaria.org/Bava_Metzia",
    ),
    Tractate(
        name="Bava Batra",
        start_date=date(2024, 6, 27),
        end_date=date(2024, 12, 18),
        start_page=2,
        url="https://www.sefaria.org/Bava_Batra",
    ),
    Tractate(
        name="Sanhedrin",
        start_date=date(2024, 12, 19),
        end_date=date(2025, 4, 9),
        start_page=2,
        url="https://www.sefaria.org/Sanhedrin",
    ),
    Tractate(
        name="Makkot",
        start_date=date(2025, 4, 10),
        end_date=date(2025, 5, 2),
        start_page=2,
        url="https://www.sefaria.org/Makkot",
    ),
    Tractate(
        name="Shevuot",
        start_date=date(2025, 5, 3),
        end_date=date(2025, 6, 19),
        start_page=2,
        url="https://www.sefaria.org/Shevuot",
    ),
    Tractate(
        name="Avodah Zarah",
        start_date=date(2025, 6, 20),
        end_date=date(2025, 9, 2),
        start_page=2,
        url="https://www.sefaria.org/Avodah_Zarah",
    ),
    Tractate(
        name="Horayot",
        start_date=date(2025, 9, 3),
        end_date=date(2025, 9, 15),
        start_page=2,
        url="https://www.sefaria.org/Horayot",
    ),
    Tractate(
        name="Zevachim",
        start_date=date(2025, 9, 16),
        end_date=date(2026, 1, 12),
        start_page=2,
        url="https://www.sefaria.org/Zevachim",
    ),
    Tractate(
        name="Menachot",
        start_date=date(2026, 1, 13),
        end_date=date(2026, 5, 1),
        start_page=2,
        url="https://www.sefaria.org/Menachot",
    ),
    Tractate(
        name="Chullin",
        start_date=date(2026, 5, 2),
        end_date=date(2026, 9, 19),
        start_page=2,
        url="https://www.sefaria.org/Chullin",
    ),
    Tractate(
        name="Bekhorot",
        start_date=date(2026, 9, 20),
        end_date=date(2026, 11, 18),
        start_page=2,
        url="https://www.sefaria.org/Bekhorot",
    ),
    Tractate(
        name="Arakhin",
        start_date=date(2026, 11, 19),
        end_date=date(2026, 12, 21),
        start_page=2,
        url="https://www.sefaria.org/Arakhin",
    ),
    Tractate(
        name="Temurah",
        start_date=date(2026, 12, 22),
        end_date=date(2027, 1, 23),
        start_page=2,
        url="https://www.sefaria.org/Temurah",
    ),
    Tractate(
        name="Keritot",
        start_date=date(2027, 1, 24),
        end_date=date(2027, 2, 19),
        start_page=2,
        url="https://www.sefaria.org/Keritot",
    ),
    Tractate(
        name="Meilah",
        start_date=date(2027, 2, 20),
        end_date=date(2027, 3, 12),
        start_page=2,
        url="https://www.sefaria.org/Meilah",
    ),
    Tractate(
        name="Kinim",
        start_date=date(2027, 3, 13),
        end_date=date(2027, 3, 15),
        start_page=1,
        url="https://www.sefaria.org/Mishnah_Kinnim",
    ),
    Tractate(
        name="Tamid",
        start_date=date(2027, 3, 16),
        end_date=date(2027, 3, 22),
        start_page=25,
        url="https://www.sefaria.org/Tamid",
    ),
    Tractate(
        name="Midot",
        start_date=date(2027, 3, 23),
        end_date=date(2027, 3, 27),
        start_page=1,
        url="https://www.sefaria.org/Midot",
    ),
    Tractate(
        name="Niddah",
        start_date=date(2027, 3, 28),
        end_date=date(2027, 6, 7),
        start_page=2,
        url="https://www.sefaria.org/Niddah",
    ),
]


def get_tractate(d: date) -> Tractate | None:
    matching = [t for t in tractates if t.start_date <= d <= t.end_date]
    if not matching:
        return None
    if len(matching) > 1:
        raise RuntimeError(f"More than one tractate matched for date {d}: {matching}")
    return matching[0]


@dataclass
class Daf:
    tractate: Tractate
    page: int

    def __str__(self) -> str:
        return f"{self.tractate.name} {self.page}"

    def url(self, subpage: Literal["a", "b"]) -> str:
        return f"{self.tractate.url}.{self.page}{subpage}?lang=bi"


SEC_PER_DAY = 24 * 60 * 60


def get_daf(d: date) -> Daf | None:
    tractate = get_tractate(d)
    if tractate is None:
        return None
    days_since_start = int((d - tractate.start_date).total_seconds() / SEC_PER_DAY)
    return Daf(
        tractate=tractate,
        page=tractate.start_page + days_since_start,
    )


if __name__ == "__main__":
    for d in [
        date.today(),
    ]:
        print(d, "->", get_daf(d))

    import csv

    for file in [
        "hebcal_2024_eur.csv",
        "hebcal_2025_eur.csv",
        "hebcal_2026_eur.csv",
        "hebcal_2027_eur.csv",
    ]:
        with open(file) as f:
            reader = csv.reader(f)
            for idx, line in enumerate(reader):
                if idx == 0:
                    continue
                d = datetime.strptime(line[1], "%d/%m/%Y").date()
                if d > date(2027, 6, 7):
                    break
                daf = get_daf(d)
                assert daf is not None
                daf_str = str(daf)
                daf_test = (
                    line[0]
                    .replace("Baba", "Bava")
                    .replace("Bechorot", "Bekhorot")
                    .replace("Arachin", "Arakhin")
                    .replace("Kinnim", "Kinim")
                )
                if daf.tractate.name == "Kinim":
                    continue
                if daf_str != daf_test:
                    print(d, daf_str, daf_test)
                    break
