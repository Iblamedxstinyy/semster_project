x = 0
y = 0

new_x = x
new_y = y

ClosedBlockX = 2
ClosedBlockY = 2

BottomLimitX = 0
TopLimitX = 4 
BottomLimitY = 0
TopLimitY = 4

returnY = 0
returnX = 0 

def Moving(d,x,y,returnY,returnX): 
    print(f'd{d}')
    if d == 1:
        x += 1
        returnX = x - 1
        returnY = y
    elif d == 2:
        x -= 1
        returnX = x + 1
        returnY = y
    elif d == 3:
        y += 1
        returnY = y - 1
        returnX = x
    elif d == 4:
        y -= 1
        returnY = y + 1
        returnX = x
    else:
        print('no')

    return x,y,returnY,returnX
    
def Checking(x,y,returnY,returnX,ClosedBlockX ,ClosedBlockY,BottomLimitX,TopLimitX,BottomLimitY,TopLimitY):

    if x == ClosedBlockX and y == ClosedBlockY:
        print("Heads UP! The chosen block is polluted with mines, death is immitent. You have been retreated back to your previous position. ")
        x = returnX
        y = returnY
        return x,y
    if x < BottomLimitX or x > TopLimitX or y < BottomLimitY or y > TopLimitY:
        print("Heads UP! The chosen block is the edge of the map, you have been retreated back to your previous position.")
        y = returnY
        x = returnX
        return x,y
    
    return x,y

while(True):
    
    d = 0
    d = int(input('выберите ваше напровление (1 : +x ,2 : -x,3 : +y,4 : -y)'))
    print(d)
    
    new_x, new_y, returnY, returnX = Moving(d,new_x,new_y ,returnY,returnX)

    new_x, new_y = Checking(new_x,new_y,returnY,returnX,
                            ClosedBlockX ,ClosedBlockY,
                            BottomLimitX,TopLimitX,
                            BottomLimitY,TopLimitY)
    
    print(f'радар : {new_x} // {new_y}')