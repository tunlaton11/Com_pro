# Creating a recursive function  
def hanoi_tower(disks, source, auxiliary, target):  
    if(disks == 1):  
        print(source, target))  
        return  
    # function call itself  
    hanoi_tower(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    hanoi_tower(disks - 1, auxiliary, source, target)  


# We are referring source as A, auxiliary as B, and target as C  
hanoi_tower(int(input()), '1', '2', '3')  # Calling the function  