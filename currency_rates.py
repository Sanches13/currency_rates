import requests, re, argparse, sys
from datetime import datetime
import cbr_parser

def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--code', type=str, required=True)
    parser.add_argument('--date', type=str, required=True)
    return parser.parse_args()

def is_code_correct(code: str) -> bool | None:
    return code in cbr_parser.get_iso_char_code_list()

def is_date_correct(date: str) -> bool:
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def main() -> None:
    args = arguments_parser()
    if is_code_correct(args.code) and is_date_correct(args.date):
        russian_name = cbr_parser.get_full_russian_name(args.code)
        rate = cbr_parser.get_rate_by_date(args.code, args.date)
        print(f"{args.code} ({russian_name}): {rate}")
    else:
        sys.exit()

if __name__ == "__main__":
    main()