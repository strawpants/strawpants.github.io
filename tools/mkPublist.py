#!/usr/bin/python3
#pyhton script to make a nice publication list in markdown for the academic homepage
# aug 2016, Roelof Rietbroek

from pyzotero import zotero

library_id='3253202'
library_type='user'
api_key='5j1t012J2IfzzcMfkQ34rCnJ'
zot = zotero.Zotero(library_id, library_type, api_key)
zot.add_parameters(content='bib', style='mla',limit=5,q='Slangen')
items = zot.top()
for item in items:
    print('Item: %s | Key: %s'%(item['data']['itemType'], item['data']['key']))
