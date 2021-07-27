"""

• The ? matches zero or one of the preceding group.
• The * matches zero or more of the preceding group.
• The + matches one or more of the preceding group.
• The {n} matches exactly n of the preceding group.
• The {n,} matches n or more of the preceding group.
• The {,m} matches 0 to m of the preceding group.
• The {n,m} matches at least n and at most m of the preceding group.
• {n,m}? or *? or +? performs a nongreedy match of the preceding group.
• ^spam means the string must begin with spam.
• spam$ means the string must end with spam.
• The . matches any character, except newline characters.
• \d, \w, and \s match a digit, word, or space character, respectively.
• \D, \W, and \S match anything except a digit, word, or space character,
respectively.
• [abc] matches any character between the brackets (such as a, b, or c).
• [^abc] matches any character that isn’t between the brackets.

you can spread the regular expression over multiple lines with comments
like this:
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?          # area code
(\s|-|\.)?                  # separator
\d{3}                       # first 3 digits
(\s|-|\.)                   # separator
\d{4}                       # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

"""