POSITIONS = [(r, c) for c in (-1, 0, 1) for r in (-1, 0, 1)] 


def annotate(minefield: list[str]) -> list[str]:

    if not minefield:
        return []  
    
    if not all(len(row) == len(minefield[0]) for row in minefield
               ) or not all(val in " *" for row in minefield for val in row):
        raise ValueError("The board is invalid with current input.")
           
    new_field = []
    r_lenght = len(minefield)
    c_lenght = len(minefield[0])
         
    for r_i, row in enumerate(minefield):
        new_row = []
        for c_i, col in enumerate(row):
            if col == "*":
                new_row.append("*")
            else:
                count = sum(1 for n_r, n_c in POSITIONS 
                            if 0 <= n_r + r_i < r_lenght
                            and 0 <= n_c + c_i < c_lenght
                            and minefield[n_r + r_i][n_c + c_i] == "*")
                if count == 0:
                    new_row.append(" ")
                else:
                    new_row.append(str(count))         
        new_field.append("".join(new_row))         
    return new_field   
