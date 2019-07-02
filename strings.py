text = "X-DSPAM-Confidence:    0.8475"

white_spaces = text.find(" ")
#number = text[white_spaces::1]
number = text[white_spaces:]

strip_white_spaces = number.lstrip()
result = float(strip_white_spaces)
print(result)


