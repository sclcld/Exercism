
def rectangles(strings):

    corners_rows_indexes = [r_index for r_index, row in enumerate(strings) if "+" in row]
    corners_rows_indexes = corners_combine(corners_rows_indexes)   
    count = 0
    
    for index_list in corners_rows_indexes:
        up, down = index_list        
        top_edge_coords = [c_index for c_index, col in enumerate(strings[up]) if col == "+"]
        top_edge_coords = corners_combine(top_edge_coords)  
        for left, right in top_edge_coords:
            has_four_corners = strings[up][left] == strings[up][right] == strings[down][left
            ]== strings[down][right] == "+"
            if has_four_corners:
                top_edge = strings[up][left: right + 1]
                sides = [side_row for side_row in strings[up + 1: down]]
                lower_edge = strings[down][left: right + 1]
                has_tops = all((side_checker(top_edge), side_checker(lower_edge)))            
                has_sides = all(all((side[left] in "+|", side[right] in "+|")) for side in sides)
                if all((has_tops, has_sides)):
                    count += 1
            
    return count


def corners_combine(coords):

    return [
                (first_corner_coord, second_corner_coord) for index, first_corner_coord in enumerate(
                 coords[:-1]) for second_corner_coord in coords[index + 1: ]
            ]
            
def side_checker(line,):
    
    rectangle_side_symbols = "+-"

    for symbol in line :
        if symbol not in rectangle_side_symbols:
            return False
            
    return True


