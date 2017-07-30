from bs4 import BeautifulSoup
import requests

def genurl(formt, formtable, baseurl):
    return baseurl + formtable[formt]

baseurl = 'http://mtgtop8.com/format?f='

top8formats = { 'vintage'   : 'VI',
                'legacy'    : 'LE',
                'modern'    : 'MO', 
                'standard'  : 'ST',
                'commander' : 'EDH' }

top8urls = { f : genurl(f, top8formats, baseurl) for f in top8formats.keys() }
top8pages = { f : requests.get(top8urls[f]) for f in top8formats.keys() }

#bs4 parsed pages
pages = { f : BeautifulSoup(top8pages[f].content, 'html.parser') for f in top8formats.keys() }

print(top8formats)
print(top8urls)
print(top8pages)
#print(pages)

#metas
metas = pages['modern'].find_all('select')
meta = []

for m in metas:
    print(m)
    if m['name'] == "meta":
        print('---- meta list ----')
        meta = m
        break

print(meta)

meta_list = meta.find_all('option')
print('---- actual options ----')
for meta in meta_list:
    print(meta)

#vintage_metas
#legacy_metas

#testxpath = '/html/body/div[4]/div/table/tbody/tr/td[1]/table/tbody/tr[13]/td[1]'

