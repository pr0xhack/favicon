#source https://gist.github.com/yehgdotnet/b9dfc618108d2f05845c4d8e28c5fc6a
#python3

import mmh3
import requests
import codecs
import sys
import os

response = requests.get(sys.argv[1],verify=False)
favicon = codecs.encode(response.content, 'base64')
hash = mmh3.hash(favicon)
print('\nShodan search query: http.favicon.hash:'+str(hash))

os.system ("shodan search http.favicon.hash:"+str(hash))
