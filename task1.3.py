text = input ("Enter the text: ")
length = len(text)
 
lower = upper = 0
 
for i in text:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
 
per_lower = lower / length * 100
per_upper = upper / length * 100
print(f"Lower: {per_lower}" )
print(f"Upper: { per_upper}" )
