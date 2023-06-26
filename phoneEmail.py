#!/usr/bin/python3
# Description: Find phone numbers and email addresses on the clipboard.
# Pyper clip module is used for copy and paste strings.
import pyperclip, re

# create phone number regular expression pattern
phoneRegex = re.compile(r'''(
                        (\d{3}|\d{3}\))?
                        (\s|-|.)?
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?
                        )''', re.VERBOSE)

# create email regex

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        )''', re.VERBOSE)

# Find all matches in clipboard text.
txt = str(pyperclip.paste())
matches = []
for grp in phoneRegex.findall(txt):
    phoneNum = '-'.join([grp[1], grp[3], grp[5]])
    if grp[8] != '':
        phoneNum += ' x' + grp[8]
    matches.append(phoneNum)

for g in emailRegex.findall(txt):
    matches.append(grp[0])

# copy result to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard...')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')

