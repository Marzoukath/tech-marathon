import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')
 


  match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
  match = re.search(r'igs', 'piiig') # not found, match == None

  match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

  ## \d = digit char, \w = word char
  match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
  match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"
