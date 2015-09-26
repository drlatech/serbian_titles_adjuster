# serbian_titles_adjuster
Adjusting Serbian Latin letters from Serbian .srt file with ISO-8859-1 encoding to UTF-8 encoding letters.

  Before change    | After change
  -----------------|-------------
  unicode(0x9E)    | ž           
  unicode(0x8E)    | Ž           
  unicode(0x9A)    | š           
  unicode(0x8A)    | Š           
  è                | č           
  È                | Č           
  æ                | ć           
  Æ                | Ć           
  ð                | đ            

Adjuster is executing in CLI.
Examples of some calls of adjuster:

```bash
python adjuster.py subtitle_name.srt
```
