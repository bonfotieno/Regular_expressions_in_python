import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2), "\n")


nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group(), "\n")

# --------matching new lines------------- #
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group(), "\n")

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

