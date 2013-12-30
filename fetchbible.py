#!/usr/bin/python

import sys, os
import urllib, urllib2
import re

books = [
   "Genesis",
   "Exodus",
   "Leviticus",
   "Numbers",
   "Deuteronomy",
   "Joshua",
   "Judges",
   "Ruth",
   "1 Samuel",
   "2 Samuel",
   "1 Kings",
   "2 Kings",
   "1 Chronicles",
   "2 Chronicles",
   "Ezra",
   "Nehemiah",
   "Esther",
   "Job",
   "Psalms",
   "Proverbs",
   "Ecclesiastes",
   "Song of Songs",
   "Isaiah",
   "Jeremiah",
   "Lamentations",
   "Ezekiel",
   "Daniel",
   "Hosea",
   "Joel",
   "Amos",
   "Obadiah",
   "Jonah",
   "Micah",
   "Nahum",
   "Habakkuk",
   "Zephaniah",
   "Haggai",
   "Zechariah",
   "Malachi",
   "Matthew",
   "Mark",
   "Luke",
   "John",
   "Acts",
   "Romans",
   "1 Corinthians",
   "2 Corinthians",
   "Galatians",
   "Ephesians",
   "Philippians",
   "Colossians",
   "1 Thessalonians",
   "2 Thessalonians",
   "1 Timothy",
   "2 Timothy",
   "Titus",
   "Philemon",
   "Hebrews",
   "James",
   "1 Peter",
   "2 Peter",
   "1 John",
   "2 John",
   "3 John",
   "Jude",
   "Revelation"
   ]

chapters = {
   "Genesis": 50,
   "Exodus": 40,
   "Leviticus": 27,
   "Numbers": 36,
   "Deuteronomy": 34,
   "Joshua": 24,
   "Judges": 21,
   "Ruth": 4,
   "1 Samuel": 31,
   "2 Samuel": 24,
   "1 Kings": 22,
   "2 Kings": 25,
   "1 Chronicles": 29,
   "2 Chronicles": 36,
   "Ezra": 10,
   "Nehemiah": 13,
   "Esther": 10,
   "Job": 42,
   "Psalms": 150,
   "Proverbs": 31,
   "Ecclesiastes": 12,
   "Song of Songs": 8,
   "Isaiah": 66,
   "Jeremiah": 52,
   "Lamentations": 5,
   "Ezekiel": 48,
   "Daniel": 12,
   "Hosea": 14,
   "Joel": 3,
   "Amos": 9,
   "Obadiah": 1,
   "Jonah": 4,
   "Micah": 7,
   "Nahum": 3,
   "Habakkuk": 3,
   "Zephaniah": 3,
   "Haggai": 2,
   "Zechariah": 14,
   "Malachi": 4,
   "Matthew": 28,
   "Mark": 16,
   "Luke": 24,
   "John": 21,
   "Acts": 28,
   "Romans": 16,
   "1 Corinthians": 16,
   "2 Corinthians": 13,
   "Galatians": 6,
   "Ephesians": 6,
   "Philippians": 4,
   "Colossians": 4,
   "1 Thessalonians": 5,
   "2 Thessalonians": 3,
   "1 Timothy": 6,
   "2 Timothy": 4,
   "Titus": 3,
   "Philemon": 1,
   "Hebrews": 13,
   "James": 5,
   "1 Peter": 5,
   "2 Peter": 3,
   "1 John": 5,
   "2 John": 1,
   "3 John": 1,
   "Jude": 1,
   "Revelation": 22
   }

apikey = urllib.quote_plus("d4a7410cbf1fcf4c4d4ba52a460c6458")
bible = "KJV1900"
formattype = ".txt"
baseurl = "http://api.biblia.com/v1/bible/content/"
#qstring = urllib.quote_plus(sys.argv[1])
#url = baseurl + bible + formattype + "?key=" + apikey + "&passage=" + qstring + "&style=oneVersePerLine"
rqurl = baseurl + bible + formattype + "?key=" + apikey + "&style=oneVersePerLine&passage="

#text = urllib2.urlopen(url).read()

for book in books:
   bfilename = re.sub(" ", "-", book.lower()) + ".tex"
   bookfile = open(bfilename, "w")
   bookfile.write("\\book{" + book + "}")
   for chap in range(1, chapters[book]):
      cfile = re.sub(" ", "-", book.lower()) + str(chap)
      cfilename = cfile + ".tex"
      bookfile.write("\\input " + cfile)
      q = rqurl + urllib.quote_plus(book + " " + str(chap))
      text = urllib2.urlopen(q).read()
      text = re.sub(r'^[0-9]+', "\\verse ", text)
      text = re.sub(r'.* (KJV 1900)', "\\chapter", text)
      chapfile = open(cfilename, "w")
      chapfile.write(text)
      chapfile.close()
   bookfile.close()
