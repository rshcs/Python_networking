from urllib.request import  Request
from  urllib.request import urlopen

req = Request('http://www.debian.org')

req.add_header('Accept-Language', 'sv')

response = urlopen(req)
print(response.readlines()[:5])