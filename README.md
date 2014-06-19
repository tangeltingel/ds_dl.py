ds_dl.py
========

Dreamscene Live Background Downloader

http://www.dreamscene.org/gallery.php

Downloads Background zip files via Post request
also works for donator Backgrounds

usage: ds_dl.py [id]
downloadFile: ds_dl_[id].zip

example ./ds_dl.py 180
downloads the background with id 180

if you want to know the id of a Background
just mouseover the download button (directly over the Wallpaper and Preview buttons)
the id is the last url parameter

for example
look on 
http://www.dreamscene.org/gallery.php?Cmd=Show&site=donator#downloadgallery
there is a Background Eye of Beauty
the download links looks like
http://www.dreamscene.org/load_donator.php?Cmd=Download&AL=Yes&ID=297
ID = 297


========

Linux using Video Files as Background

simply add 

mplayer video_file.{wmv,mp4,...} -rootwin -vf -noconsolecontrols -loop 0

to your autostart, .xinitrc or whatever

example mplayer background.mp4 -rootwin -vf -noconsolecontrols -loop 0
