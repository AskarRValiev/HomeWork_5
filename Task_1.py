#1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

from tracemalloc import start


def del_is_letters(start_string: str, letters: str):
    '''
    Функция принимает исходную строку и последовательность удаляемых из строки символов.
    Возвращает строку без удаленных символов
    '''
    lst = (start_string.split())
    for item in lst:
        if letters in item:
            lst.remove(item)
    print(lst)
    res = ' '.join(lst)
    return(res)

start_string = 'абвгдейка - это передача'
print(del_is_letters(start_string, 'абв'))

