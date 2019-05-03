#!/usr/bin/env python

# When on Windows, run as Administrator

import os, sys
fname = 'app.asar'

if not os.path.isfile(fname):
    fname = '/Applications/Skype.app/Contents/Resources/app.asar'

if not os.path.isfile(fname):
    fname = "C:/Program Files (x86)/Microsoft/Skype for Desktop/resources/app.asar" 

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

# emoji keyboard popup, Skype 8.38.0.161
data = data.replace(
    b',e.size=18):(e.icon=n(10).SkypeIcon.EmoticonStroke,',
    b',e.size=18):(e.icon="\xEE\x90\x9F",e.size=18,'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
) 

# the most obnoxious one next to the message for various Skype versions
data = data.replace(
    b'default:return n(11).SkypeIcon.EmoticonStroke}},',
    b'default:return ""/*).SkypeIcon.EmoticonStro*/}},',
)

data = data.replace(
    b'default:return n(10).SkypeIcon.EmoticonStroke}},',
    b'default:return ""/*).SkypeIcon.EmoticonStro*/}},',
)

data = data.replace(
    b't.size=18):(t.icon=n(10).SkypeIcon.EmoticonStroke,',
    b't.size=18):(t.icon="\xEE\x90\x9F",t.size=18,\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

data = data.replace(
    b'void 0,icon:n(10).SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*).SkypeIcon.EmoticonStro*/,'
)

with open(fname,"wb") as f:
    f.write(data)

print('Patching done')
