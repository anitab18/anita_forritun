num_int = int(input("Input a number: "))    
positive_list = []
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > 0: 
        positive_list.append(num_int)
else:
    max_int = max(positive_list)
    print("The maximum is", max_int)