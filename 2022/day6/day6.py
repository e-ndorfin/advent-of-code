with open('day6.in') as file:
    data = file.read()

# Part 1 
# for i in range (3, len(data)): 
#     temp = [data[i+a] for a in range (-3, 1)]

#     if len(temp) == len(set(temp)):
#         print (i+1) 
#         break 
    
# Part 2 
for i in range (13, len(data)): 
    temp = [data[i+a] for a in range (-13, 1)]

    if len(temp) == len(set(temp)):
        print (i+1) 
        break 
        
        