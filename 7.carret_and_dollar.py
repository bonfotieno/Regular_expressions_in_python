import re

# ------mostly used when working with sentences------

beginsWithHello = re.compile(r'^Hello')
print("\n", beginsWithHello.search('Hello world!') is not None)
print(beginsWithHello.search('He said hello.') is None)

endsWithNumber = re.compile(r'\d$')
print("\n", endsWithNumber.search('Your number is 42') is not None)
print(endsWithNumber.search('Your number is forty two.') is None)

wholeStringIsNum = re.compile(r'^\d+$')
print("\n", wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') is None)
print(wholeStringIsNum.search('12 34567890') is None)
