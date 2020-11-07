from urllib.request import urlopen
import urllib.error


response  = urlopen('http://www.debian.org')

print(response.readline())
#print(response.url)
#print(response.read(50))
#print(response.status)
#print(response.read(1000).decode('utf-8'))
#print(response.getheaders())
'''
try:
    response2 = urlopen('http://debian.org/halo.txt')
except urllib.error.URLError as e:
    print(e)
'''

