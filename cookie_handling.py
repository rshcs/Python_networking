from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor

cookie_jar = CookieJar()

opener = build_opener(HTTPCookieProcessor(cookie_jar))
opener.open('http://www.github.com')

print(len(cookie_jar))