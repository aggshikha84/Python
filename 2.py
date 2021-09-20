import string

original_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
converted_text = ""

# Option 1
for x in original_text:
    ascii_value= ord(x)
    if 96 < ascii_value < 121:
        converted_text = converted_text + chr(ascii_value + 2)
    elif ascii_value == 121:
        converted_text = converted_text + chr(97)
    elif ascii_value == 122:
        converted_text = converted_text + chr(98)
    else:
        converted_text = converted_text + x

print (converted_text)

# Option 2
translator_dict = original_text.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
translated_text = original_text.translate( translator_dict);
print(translated_text)

puzzle_text = "map"
translated_text = puzzle_text.translate(translator_dict)
print(translated_text)
