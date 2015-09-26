# -*- coding: utf-8 -*-
import sys

# Tuple of pairs symbols and letters that should be shown in subtitle.
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

# Open .srt file providede after source file in terminal.
fn = open(sys.argv[1], 'r')
ff = fn.read()
fn.close()

# Change encoding from ISO-8859-1 to UTF-8
ff = unicode(ff, 'iso-8859-1').encode('utf-8')

for pair in pairs:
    ff = ff.replace(pair[0], pair[1])
# Open same file but in 'write' mode to overwrite content.
fn = open(sys.argv[1], 'w')
fn.write(ff)

fn.close()
