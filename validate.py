from datetime import date, timedelta
from main import format_daf
from tractates import Tractate, tractates


DOWNLOADED = [
    tractates[22],
    tractates[23],
    tractates[24],
    tractates[25],
]

DAY = timedelta(days=1)


if __name__ == "__main__":
    print(f"Expected to be downloaded:\n{'\n'.join(str(t) for t in DOWNLOADED)}")
    for t in DOWNLOADED:
        print(f"Validating {t}...")
        d = t.start_date
        while d <= t.end_date:
            print(d)
            format_daf(d)
            d += DAY
    print("OK")
