from urllib.request import  Request
from  urllib.request import urlopen
import gzip

req = Request('http://www.debian.org')

#req.add_header('Accept-Language', 'sv') # language = Swedish
req.add_header('Accept-Encoding', 'gzip') # language = Swedish

response = urlopen(req)
content = gzip.decompress(response.read())

#print(response.readlines()[:5])
print(content.splitlines()[:5])


