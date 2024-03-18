'''
1)	Вам дана строка. Выведите все подстроки, содержащие "cat".

import re
pattern = r"[Cc][Aa][Tt]"
text = "cAt 3fr56Catgt6789 caT123dflj CAT sdaf34fcat adfr324 Cat"
print(re.findall(pattern, text))
_____________
2)	Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

import re

pattern = r"\b\w*[Zz]\S{3}[Zz]\w*\b"
text = "zAZ 3fZq1jzatgt6789 zz2pzf1hjZ Z z z 12dz_3_Zddw3 Z1zZ szaf4Zfcat adfr324 Zat5Zf"
print(re.findall(pattern, text))
_____________
3)	Номер должен быть длиной 10 знаков и начинаться с 8 или 9. Есть список телефонных номеров,
и нужно проверить их, используя регулярные выражения в Python

import re

result = re.findall(r'[8|9][0-9]{9}', '8123456789 9123456789 8966 812345678 0123456789 589')
print(result)
_____________
# 4)	Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.

import re

result = re.findall(r'\b[aeiouAEIOU]\w+', 'The order of the fields in all of the generated methods is '
                                                    'the order in which they appear in the class definition')
print(result)
_____________
5)	Дана строка. Вывести все числа этой строки, как отрицательные так и положительные.

import re

result = re.findall(r'-?\b\d+\b', '-81 23 sfs 4Fs7 -d91 -23 456 8df3 678 -589')
print(result)
_____________
6)	В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

import re

text = 'Human rights are rights inherent to all human'
print(re.sub(r'[H|h]uman', 'computer', text))
_____________

7)	Извлечь дату из строки. Формат даты dd–mm-yyyy (например, 2022-02-28).

import re

pattern = r'\d{2}-\d{2}-\d{4}|\d{4}-\d{2}-\d{2}'
text = "2022-02-28 asd 34-3456 20-03-2015, XyZ 56-4532 10-12-2007, ABC 67-8945 31-01-2023"
print(re.findall(pattern, text))
_____________
8)	Найти все слова, в которых есть хотя бы одна буква ‘b’

import re
pattern = r'\b\w*[Bb]\w*\b'

text = 'behavior, job, be objects, B are b added suBscribe, adsf bjkybbbbbb bBbb'
print(re.findall(pattern, text))
'''

