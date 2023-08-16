import sys, requests, re, argparse
from datetime import datetime

def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--code', type=str, required=True)
    parser.add_argument('--date', type=str, required=True)
    return parser.parse_args()

def is_code_correct(code) -> bool:
    iso_list = requests.get("https://www.cbr.ru/scripts/XML_valFull.asp").text
    iso_char_code = re.compile(r'<ISO_Char_Code>([A-Z]{3})</ISO_Char_Code>')
    return code in iso_char_code.findall(iso_list)

def is_date_correct(date) -> bool:
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def main():
    args = arguments_parser()
    print(is_date_correct(args.date))

if __name__ == "__main__":
    main()