
a = 1       
total = 0  
hasil_str = ""  

while a <= 5:
    total += a              
    hasil_str += str(a) + " + "  
    a += 1                  
hasil_str = hasil_str[:-3]  
print(f"{hasil_str} = {total}")
