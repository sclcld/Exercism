def triplets_with_sum(number):
       
        return [
                [a, b, (number - a - b)] for a in range(1, number // 3 + 1) 
                for b in range(a + 1, (number - a) // 2 + 1)                
                if a * a + b * b == (number - a - b) * (number - a - b)
        ]
                    