data = [6, 4, 10, 9, 109, 56, 43, 145, 43, 33, 67, 95]

for index in range(0, len(data)):
    min_index = index
    
    for comp_index in range(index+1, len(data)):
        if data[comp_index] < data[min_index]:
            min_index = comp_index
            
    if min_index != index:
        data[index], data[min_index] = data[min_index], data[index]
        
        print(data)
