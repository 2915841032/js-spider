import fontTools
from fontTools.ttLib import TTFont

font=TTFont('font.woff')
font.saveXML('font.xml')

font_dict = {}
font = TTFont('font.woff')
for k, v in font.getBestCmap().items():
    # print(k, v)
    if v[3:]:
        content = '\\u00' + v[3:] if len(v[3:]) == 2 else "\\u" + v[3:]
        font_dict[hex(k).replace('0x', '&#x')] = content.encode('utf-8').decode('unicode_escape')
        # @font-face
# print(font.getBestCmap())
print(font_dict)