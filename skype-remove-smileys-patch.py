#!/usr/bin/env python

import os, sys
fname = 'app.asar'

if not os.path.isfile(fname):
    fname = '/Applications/Skype.app/Contents/Resources/app.asar'

if not os.path.isfile(fname):
    print('Copy this script to the same folder '
        'with app.asar is before running')
    sys.exit(-1)

with open(fname,"rb") as f:
    data = f.read()

# this probably is an unnecessary replace - can't find where this one goes to
# data = data.replace(
#     b'_onKeyboardButtonClick}:{icon:n(11).SkypeIcon.EmoticonStroke,',
#     b'_onKeyboardButtonClick}:'
#     b'{icon:"\xEE\x90\x9F",size:18,'
#     b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
# )

# previous skype version, emoji keyboard popup button
data = data.replace(
    b't.size=18):(t.icon=n(11).SkypeIcon.EmoticonStroke,',
    b't.size=18):'
    b'(t.icon="\xEE\x90\x9F",t.size=18,'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

# emoji keyboard popup, Skype 8.36.0.52
data = data.replace(
    b',e.size=18):(e.icon=n(11).SkypeIcon.EmoticonStroke,',
    b',e.size=18):(e.icon="\xEE\x90\x9F",e.size=18,'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)  

# the most obnoxious one next to the message
data = data.replace(
    b'default:return n(11).SkypeIcon.EmoticonStroke}},',
    b'default:return ""/*).SkypeIcon.EmoticonStro*/}},',
)

with open(fname,"wb") as f:
    f.write(data)

print('Patching done')
