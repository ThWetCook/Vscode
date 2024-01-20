from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.youtube.com/watch?v=XVv6mJpFOb0').text
soup = BeautifulSoup(html_text, 'lxml')
print(html_text)