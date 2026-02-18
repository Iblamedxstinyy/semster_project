
cordinates_x = 0
cordinates_y = 0


new_cordinates_x = cordinates_x
new_cordinates_y = cordinates_y


closed_block_x = 2
closed_block_y = 2


bottom_limit_x = 0
top_limit_x = 4 
bottom_limit_y = 0
top_limit_y = 4


initial_cordinates_y = 0
initial_cordinates_x = 0 

def Moving(d,cordinates_x,cordinates_y,initial_cordinates_y,initial_cordinates_x): 

    if d == 1:
        cordinates_x += 1
        initial_cordinates_x = cordinates_x - 1
        initial_cordinates_y = cordinates_y
    elif d == 2:
        cordinates_x -= 1
        initial_cordinates_x = cordinates_x + 1
        initial_cordinates_y = cordinates_y
    elif d == 3:
        cordinates_y += 1
        initial_cordinates_y = cordinates_y - 1
        initial_cordinates_x = cordinates_x
    elif d == 4:
        cordinates_y -= 1
        initial_cordinates_y = cordinates_y + 1
        initial_cordinates_x = cordinates_x
    else:
        print('no')

    return cordinates_x,cordinates_y,initial_cordinates_y,initial_cordinates_x
    
def Checking(cordinates_x,cordinates_y,initial_cordinates_y, InitialCordinates_x,ClosedBlockX ,closed_block_y ,bottom_limit_x ,top_limit_x,bottom_limit_y,top_limit_y):

    if cordinates_x == ClosedBlockX and cordinates_y == closed_block_y:
        print("Heads UP! The chosen block is polluted with mines, death is immitent. You have been retreated back to your previous position. ")
        cordinates_x = initial_cordinates_x
        cordinates_y = initial_cordinates_y
        return cordinates_x,cordinates_y
    if cordinates_x < bottom_limit_x or cordinates_x > top_limit_x or cordinates_y < bottom_limit_y or cordinates_y > top_limit_y:
        print("Heads UP! The chosen block is the edge of the map, you have been retreated back to your previous position.")
        cordinates_y = initial_cordinates_y
        cordinates_x = InitialCordinates_x
        return cordinates_x,cordinates_y
    
    return cordinates_x,cordinates_y

while(True):
    
    d = 0
    d = int(input('выберите ваше напровление (1 : +x ,2 : -x,3 : +y,4 : -y)'))
    print(d)
    
    new_cordinates_x, new_cordinates_y, initial_cordinates_y, initial_cordinates_x = Moving(d,new_cordinates_x,new_cordinates_y ,initial_cordinates_y,initial_cordinates_x)

    new_cordinates_x, new_cordinates_y = Checking(new_cordinates_x,new_cordinates_y,initial_cordinates_y,initial_cordinates_x,
                            closed_block_x ,closed_block_y,
                            bottom_limit_x,top_limit_x,
                            bottom_limit_y,top_limit_y)
    
    print(f'радар : {new_cordinates_x} // {new_cordinates_y}')