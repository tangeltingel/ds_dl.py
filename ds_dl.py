#!/usr/bin/python2

import sys
import urllib
import urllib2
import shutil

try: 
    id = sys.argv[1]
    run = True
except IndexError:
    print "dreamscene normal + donator download"
    print "usage: ./ds_dl.py [id]"
    print "download File: ds_dl_[id].zip" 
    run = False

if run :
    req = urllib2.Request('http://www.dreamscene.org/load.php')
    values = { 'Cmd': 'DownloadFile', 'ID' : id}
    req.add_data(urllib.urlencode(values))
    resp = urllib2.urlopen(req)


    myfile = open('ds_dl_'+id+'.zip', 'wb')
    shutil.copyfileobj(resp.fp, myfile)
    myfile.close()

