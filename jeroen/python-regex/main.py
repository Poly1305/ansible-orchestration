#!/usr/bin/env python3

import re

# Zoek tekst in faketekst.txt m.b.v. regex
# Om tekst te kunnen zoeken moet je gebruik maken van raw string met r voor de zin

tekstbestand = "/home/student/ansible-orchestration/jeroen/python-regex/faketekst.txt"


with open (tekstbestand, 'r') as file_object:
   tekst = file_object.read()


zin = "Zelfs als men weet dat he"

pattern = re.compile(r'Zelfs als')

matches = pattern.finditer(tekst)

for match in matches:
  print(match)

print(tekst[362:371])
