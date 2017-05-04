import requests

response = requests.get('https://www.nytimes.com/2017/05/03/opinion/james-comey-fbi-mildly-nauseous.html')
response.encoding = 'utf-8'
page_text =   response.text
status_code = response.status_code

to_write = page_text.encode('utf-8')

with open('test.txt', 'a') as write_file:
    write_file.write(to_write)