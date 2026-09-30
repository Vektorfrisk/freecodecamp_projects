

def number_pattern(n):     
    
    if isinstance(n, int):
        if n > 1:
                        
            return " ".join([str(num) for num in range(1, n + 1)])
                 
        else:
            return 'Argument must be an integer greater than 0.'                                    

    else:                
        return 'Argument must be an integer value.'
           
        
print(number_pattern(10))

