text = "X-DSPAM-Confidence:    0.8475"

f = text.find('0')
value = text[f:]
float_var = float(value)
print(float_var)