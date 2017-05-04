import re

a = 'https://www.nytimes.com/2017/05/03/us/politics/trump-immigration-spending-bill.html'
res = re.search(r'/([\w+-]+).html$', a)
print res.group(1)
exit()

match_strings = [
    'hello world 00',
    'goodbye world    ',
    ' 23 bonjour',
    'wilkommen23  ',
    'aloha',
    '99',
    '88557799',
    'Que 3 Tal!',
    'myfile.jpg',
    'yourfile.JPG'
]


_8_1 = r'\d+'
_8_2 = r'^\d'
_8_3 = r'\d$'
_8_4 = r'^\d\d$'
_8_5 = r'^\d\d$'
_8_6 = r'^\d*$'
_8_7 = r'^\D*$'
_8_8 = r'[a-zA-Z]+'
_8_9 = r'^\w+$'
_8_10 = r'^[a-zA-Z]+$'
_8_11 = r'[A-Z]+'
_8_12 = r'\s\s+$'
_8_13 = r'\S'
_8_14 = r'^\S+$'
_8_15 = r'\D$'
_8_16 = r'[^a-zA-Z]'
_8_17 = r'[a-zA-Z]\d'
_8_18 = r'\w\.'
_8_19 = r'\w+\s+\w+'
_8_20 = r'\.(jpg|JPG)$'
_8_21 = r'\.jpg$' #with re.IGNORECASE as 2nd arg
_8_22 = r'^\D+$'

# test
for str in match_strings:
    res = re.search(_8_22, str)
    if res:
        print str
