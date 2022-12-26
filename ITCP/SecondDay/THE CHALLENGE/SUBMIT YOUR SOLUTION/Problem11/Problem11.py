text = "ITCCC"

Upper = True
for i in range(1, len(text)):
    if not(text[i].isupper()):
        Upper = False
        break
    
print(Upper)