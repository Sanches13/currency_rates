import requests, re

def get_iso_char_code_list() -> list[str] | None:
    valute_info = requests.get("https://www.cbr.ru/scripts/XML_valFull.asp").text
    iso_char_code_format = re.compile(r'<ISO_Char_Code>([A-Z]{3})</ISO_Char_Code>')
    return iso_char_code_format.findall(valute_info)

def get_rate_by_date(code: str, date: str) -> str | None:
    # TODO: обработать исключительные ситуации при отсутствии информации
    rates = requests.get(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}").text
    rate_format = re.compile(code + r'''</CharCode>
                             <Nominal>(\d){1,5}</Nominal>
                             <Name>([А-Яа-яЁё ]+)</Name>
                             <Value>((\d){1,3},(\d){4})</Value>''', re.VERBOSE)
    
    return rate_format.search(rates).group(3)

def get_full_russian_name(code: str) -> str:
    valute_info = requests.get("https://www.cbr.ru/scripts/XML_valFull.asp").text
    russian_name_format = re.compile(r'''<Name>([А-Яа-яЁё ]+)</Name>
                                     <EngName>([a-zA-Z ]+)</EngName>
                                     <Nominal>(\d+)</Nominal>
                                     <ParentCode>(\S+)\s+</ParentCode>
                                     <ISO_Num_Code>(\d+)</ISO_Num_Code>
                                     <ISO_Char_Code>''' + code, re.VERBOSE)
    return russian_name_format.search(valute_info).group(1)