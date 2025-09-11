text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
num = text[colon+1:]
stringaling = num.lstrip()
print(float(stringaling))