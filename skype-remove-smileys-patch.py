#!/usr/bin/env python

# on Windows: run as Administrator
# on Linux: run with sudo

import os, sys
fname = 'app.asar'

if not os.path.isfile(fname):
    fname = '/Applications/Skype.app/Contents/Resources/app.asar'

if not os.path.isfile(fname):
    fname = "C:/Program Files (x86)/Microsoft/Skype for Desktop/resources/app.asar" 

if not os.path.isfile(fname):
    fname = "/usr/share/skypeforlinux/resources/app.asar" 

if not os.path.isfile(fname):
    print('Copy this script to the same folder '
          'with app.asar is before running')
    sys.exit(-1)

with open(fname,"rb") as f:
    data = f.read()


# emoji keyboard popup, Skype 8.60.0.76
data = data.replace(
    b'=p.IconSize.size18):(e.icon=p.SkypeIcon.EmoticonStroke',
    b'=p.IconSize.size18):(e.icon="\xEE\x90\x9F"'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

# emoji keyboard popup, Skype 8.36.0.52
data = data.replace(
    b',e.size=18):(e.icon=n(11).SkypeIcon.EmoticonStroke,',
    b',e.size=18):(e.icon="\xEE\x90\x9F",e.size=18,'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

# emoji keyboard popup, Skype 8.38.0.161, 8.51.0.72
data = data.replace(
    b':(e.icon=n(10).SkypeIcon.EmoticonStroke,',
    b':(e.icon="\xEE\x90\x9F",e.size=18,'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
) 

# emoji keyboard popup Skype 8.59.0.77
data = data.replace(
    b'.size18):(e.icon=n(9).SkypeIcon.EmoticonStroke,',
    b'.size18):(e.icon="\xEE\x90\x9F",e.size=18,\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

# emoji keyboard popup Skype xxxx
data = data.replace(
    b't.size=18):(t.icon=n(10).SkypeIcon.EmoticonStroke,',
    b't.size=18):(t.icon="\xEE\x90\x9F",t.size=18,\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

# emoji keyboard popup Skype yyyy
data = data.replace(
    b't.size=18):(t.icon=n(11).SkypeIcon.EmoticonStroke,',
    b't.size=18):'
    b'(t.icon="\xEE\x90\x9F",t.size=18,'
    b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20'
)

# emoji keyboard popup Skype 8.72.0.82
data = data.replace(
    b'.size18):(e.icon=g.SkypeIcon.EmoticonStroke,',
    b'.size18):(e.icon="\xEE\x90\x9F",e.size=18,           ',
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
    b'void 0,icon:n(10).SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*).SkypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0,icon:n(9).SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*.SkypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0,icon:f.SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*ypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0,icon:b.SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*ypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0,icon:u.SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*ypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0,icon:y.SkypeIcon.EmoticonStroke,',
    b'void 0,icon:""/*ypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0:this._onReactKeyPress,size:t,color:e,hoverColor:e,icon:f.SkypeIcon.EmoticonStroke,',
    b'void 0:this._onReactKeyPress,size:t,color:e,hoverColor:e,icon:""/*ypeIcon.EmoticonStro*/,'
)

data = data.replace(
    b'void 0:this._onReactKeyPress,size:t,color:e,hoverColor:e,icon:y.SkypeIcon.EmoticonStroke,',
    b'void 0:this._onReactKeyPress,size:t,color:e,hoverColor:e,icon:""/*ypeIcon.EmoticonStro*/,'
)

print('Patching file: '+fname)
with open(fname,"wb") as f:
    f.write(data)

print('Patching done')

# change False to True: code for printing potential replacement candidates for a new Skype version
while False:
    idx = data.index(b'SkypeIcon.EmoticonStroke')
    print(data[idx-32:idx+64])
    data = data[:idx] + b'Q' + data[idx+1:]
