import math

def cipher_text(plain_text):  

    plain_text="".join([letter for letter in plain_text.replace(" ","").lower() if letter.isalnum()])
    if not plain_text:
        return plain_text
    rows = math.ceil(math.sqrt(len(plain_text)))
    columns = math.ceil(len(plain_text) / rows)    
    while len(plain_text)<rows*columns:
        plain_text+=" "
    
    return ' '.join(plain_text[row::rows] for row in range(rows))