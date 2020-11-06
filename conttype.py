from urllib.request import Request
from urllib.request import urlopen

response = urlopen('http://www.python.org')

params = response.getheader('Content-Type').split(':')
print(params)