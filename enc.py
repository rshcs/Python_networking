from urllib.request import  Request
from  urllib.request import urlopen
import gzip

req = Request('http://www.debian.org')

req.add_header('Accept-Encoding', 'identity') 

response = urlopen(req)

print(response.getheader('Content-Type'))

