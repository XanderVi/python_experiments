# -*- coding: utf-8 -*-
import urllib.request

url = 'https://github.com/XanderVi' # or any html page you need to download
html = urllib.request.urlopen(url).read()
file = open("site.html", "wb")
file.write(html)
file.close()
