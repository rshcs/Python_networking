from urllib.request import Request
from urllib.request import urlopen

req = Request('http://www.python.org')
urlopen(req)
print(req.get_header('User-agent'))



