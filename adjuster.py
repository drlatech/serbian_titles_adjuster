# -*- coding: utf-8 -*-

# A little bit improved version of subtitle adjuster, it is not 
# necessary to apply it on only one .srt file, now you can
# do all job at once for all movies in your collection...

import os
import sys
import codecs

# Source directory and directory of all movies
"""
Traverse all directories of movies, search for subtitle files, open them, read,
close, copy them in another file, make changes on letters on already open file 
context, then open again and save those changes to that file...
	movies --
	        |
                 -- Movie 1 folder --
	                           |
	                           -- Video
				|
				-- subtitle file
	        |
                 -- Movie 2 folder --
				|
				-- Video
				|
				-- subtitle file
                 :
                 :
                 :
                 |
                 -- adjuster.py
"""

curr_dir = os.getcwd()

film_dirs = [folder for folder in os.listdir(curr_dir) if os.path.isdir(folder)]

# Tuple of pairs symbols and letters that should be shown in subtitle.
# First symbol in first four pairs are not empty strings.
# They are not only visible in browser.
pairs = (('', 'ž'),
         ('', 'Ž'),
         ('', 'š'),
         ('', 'Š'),
         ('è', 'č'),
         ('È', 'Č'),
         ('æ', 'ć'),
         ('Æ', 'Ć'),
         ('ð', 'đ'),
        )


for film in film_dirs:
    files = os.listdir(film)
    for f in files:
        print f
        if f.endswith('.srt'):
            path = film + '/' + f
            fn = open(path, 'r')
            ff = fn.read()
            ff = unicode(ff, 'iso-8859-1').encode('utf-8')
            fn.close()
            os.rename(path, path + '.copy')

            for pair in pairs:
                ff = ff.replace(pair[0], pair[1])

            fn = open(path, 'w')
            fn.write(ff)

            fn.close()



