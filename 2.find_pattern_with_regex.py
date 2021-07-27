import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())  # mo.group to display the whole match

'''GROUP WITH PARENTHESIS'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


'''matching multiple groups with the pipe'''
print('\nmatching multiple groups with the pipe')
piperegx = re.compile(r'batman|tina fey')
mo1 = piperegx.search('we got batman and tina fey')
print(mo1.group())


'''optional matching with the question mark'''
print('\noptional matching with the question mark')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


'''matching zero or more with the star'''
print('\noptional matching with the question mark')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
# use Bat(wo)+man for one or more


'''matching specific repetition with curly brackets'''
print('\nmatching specific repetition with curly brackets')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHaHaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 is None)
haRegex = re.compile(r'(Ha){3,}')
mo3 = haRegex.search('HaHaHaHaHaHa')
print(mo3.group())
haRegex = re.compile(r'(Ha){,5}')
mo4 = haRegex.search('HaHaHaHaHaHa')
print(mo4.group())