#4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def rle_coding(s):
    '''
    Принимает строку, возвращает код строки в формате RLE.
    '''
    coded_str = ''
    i = 0
    while i < len(s):
        count = 1
        while (i+1 < len(s) and s[i] == s[i+1]):
            count += 1
            i += 1
        coded_str += str(count) + s[i]
        i += 1
    return coded_str


def rle_decoding(s: str):
    decoded_str = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            decoded_str += int(s[i]) * s[i+1]
        i += 1
    return decoded_str



with open('input.txt', 'r') as cd_data:
    for cd_line in cd_data:
        with open('out_coded.txt', 'a') as cd:
            cd.write(rle_coding(cd_line + '\n'))


with open('input_rle.txt', 'r') as dcd_data:
    for dcd_line in dcd_data:
        with open('out_decoding.txt', 'a') as d_cd:
            d_cd.write(rle_decoding(dcd_line + '\n'))  #вот тут я не понял, почему при записис в файл не срабатывает перенос строки, 
            #хотя в строке 34 запись такая же и все прекрасно работает
       
        


