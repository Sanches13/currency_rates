""" 
Считываем два аргумента из консоли
Проверяем их на корректность
Определяем значения параметров --code и --date
Подставляем date в https://www.cbr.ru/scripts/XML_daily.asp?date_req=dd/mm/yyyy
Ищем значение курса для code
"""
import sys, requests, re

def check_arguments_format(options) -> bool:
    options_format = re.compile(r"--(code|date)=*")
    for option in options:
        if options_format.search(option).group() == []:
            return False
    return True

def arguments_correct(options) -> bool:
    if check_arguments_format(options):
        pass

if len(sys.argv) != 3 or arguments_correct(sys.argv[1:]):
    print(f"Usage {sys.argv[0]} --code=ISO_FORMAT --date=DD-MM-YYYY")
    sys.exit()
    