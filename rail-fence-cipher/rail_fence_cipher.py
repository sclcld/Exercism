def indexes(message, rails):
    
    from_top = True
    rail_index = 0

    for ind in range(len(message)):
        if rail_index == 0:
            from_top = True
        if rail_index == rails - 1:
            from_top = False
        yield (rail_index, ind)   
        rail_index += 1 if from_top else - 1

def encode(message, rails):

    encoded = ["" for i in range(rails)]

    for rail, letter in indexes(message,rails):        
        encoded[rail] += message[letter]
        
    return "".join(encoded)

def decode(encoded_message, rails):
    
    rail = [[[] for cols in range(len(encoded_message))] for rows in range(rails)]
    indx = zip(indexes(encoded_message, rails), encoded_message)
    
    for i, encoded in enumerate(encoded_message):
        rail_ind, col_ind = indx[i]
        rail[rail_ind][col_ind].append(encoded)

    return "".join(rail[a][b][0] for a,b in indexes(encoded_message,rails))