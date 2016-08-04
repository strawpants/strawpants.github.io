#!/usr/bin/python3
#python script to parse publications from zotero in html for my academic homepage
# aug 2016, Roelof Rietbroek

from pyzotero import zotero
import keyring
import os.path
import shutil
import re
import codecs

zoterodatdir='/home/roelof/wolk7/zoteroData/storage'
root='/home/roelof/work2/homep8ge'
library_id='3253202'
library_type='user'
#to put your APIkey in your keyring adapt the following:
#keyring.set_password('Zotero','PyzoteroKey','YOURAPIkey')
api_key=keyring.get_password('Zotero','PyzoteroKey')

htmlout=root+'/layouts/partials/pubsbody.html'
fid=open(htmlout,'w')
fid.write('<div class="mdl-color-text--grey-700 mdl-card__supporting-text meta">\n<div class="hugo-content" >\n <h4> Peer reviewed </h4>')




stripdiv=re.compile('</div>$')
author='Rietbroek'
authorsearch=re.compile(author)

zot = zotero.Zotero(library_id, library_type, api_key)
zot.add_parameters(tag='RRpeer',sort='date')
items = zot.everything(zot.top())
for item in items:
	#get a parsed entry for each hit 
	htmlentry=zot.item(item['key'],content='bib',style='geophysical-research-letters')[0].encode('utf-8').decode('latin-1')
	htmlentry=authorsearch.sub('<b>'+author+'</b>',htmlentry)
	#find out if there is a free pdf attached which we can provide a link to
	freepdfentry=zot.children(item['key'],tag='freepdf')
	if freepdfentry:
		src=zoterodatdir+'/'+freepdfentry[0]['data']['key']+'/'+freepdfentry[0]['data']['filename']
		destpdf='/data/'+freepdfentry[0]['data']['filename']
		#copy the pdf to the static folder if there does not exist one yet
		if not os.path.isfile(root+'/static'+destpdf):
			shutil.copy2(src,root+'/static'+destpdf)

		#modify the html entry to include the link
		htmlentry=stripdiv.sub('',htmlentry) #first strip the final </div>
		htmlentry+='<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect icon-button" href="'+destpdf+'" aria-label="Download pdf" title="Download pdf" data-upgraded=",MaterialButton,MaterialRipple"><i class="material-icons_2x icon ion-link"></i><span class="mdl-button__ripple-container"><span class="mdl-ripple"></span></span></a></div>'
	
	fid.write('\t'+htmlentry+'\n')

fid.write('</div>\n')
fid.close()	

