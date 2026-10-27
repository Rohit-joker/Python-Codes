import random

print("welcome to connect four ")
print("-------------------------")

possibleletters = ["A","B","C","D","E","F","G"]
gameboard=[["","","","","","",""],
           ["","","","","","",""],
           ["","","","","","",""],
           ["","","","","","",""],
           ["","","","","","",""],
           ["","","","","","",""]]

rows= 6
col= 7 

def printgameboard():
    print("\n    A    B    C    D    E    F    G    ",end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x , " |",end="")
        for y in range(col):
            if(gameboard[x][y] == "🟡"):
                print("",gameboard[x][y],end="  |")
            elif(gameboard[x][y] == "🔴"):
                print("",gameboard[x][y],end="  |")
            else:
                print(" ",gameboard[x][y],end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyarray(spacepicked,turn):
    gameboard[spacepicked[0]][spacepicked[1]]=turn

def checkforwinner(chip):
    #check horizontal 
    for y in range(rows):
        for x in range(col - 3):
            if(gameboard[x][y]==chip and gameboard[x+1][y]==chip and gameboard[x+2][y]==chip and
            gameboard[x+3][y]==chip):
                print("\nGame over! ",chip,"wins! Thank you for playing :")
                return True

    #check vertical
    for y in range(rows):
        for x in range(col - 3):
            if(gameboard[x][y]==chip and gameboard[x][y+1]==chip and gameboard[x][y+2]==chip and
            gameboard[x][y+3]==chip):
                print("\nGame over! ",chip,"wins! Thank you for playing :")
                return True
            
    #check diagonal top right to bottom left
    for y in range(rows-3):
        for x in range(3,col):
            if(gameboard[x][y]==chip and gameboard[x+1][y-1]==chip and gameboard[x+2][y-2]==chip and
            gameboard[x+3][y-3]==chip):
                print("\nGame over! ",chip,"wins! Thank you for playing :")
                return True
            
    #check diagonal top left to bottom right
    for y in range(rows-3):
        for x in range(col-3):
            if(gameboard[x][y]==chip and gameboard[x+1][y+1]==chip and gameboard[x+2][y+2]==chip and
            gameboard[x+3][y+3]==chip):
                print("\nGame over! ",chip,"wins! Thank you for playing :")
                return True
            
    return False

def coordinateParser(inputString):
    coordinate= [None] * 2
    if(inputString[0]=="A"):
        coordinate[1]= 0
    elif(inputString[0]=="B"):
        coordinate[1]= 1
    elif(inputString[0]=="C"):
        coordinate[1]= 2
    elif(inputString[0]=="D"):
        coordinate[1]= 3
    elif(inputString[0]=="E"):
        coordinate[1]= 4
    elif(inputString[0]=="F"):
        coordinate[1]= 5
    elif(inputString[0]=="G"):
        coordinate[1]= 6 
    else:
        print("invalid ")
    coordinate[0]=int(inputString[1])
    
    try:
        coordinate[1]=ord(inputString[0].upper())-ord("A")
        coordinate[0]=6-int(inputString[1])
        if not 0 <= coordinate[1] <= 6 or not 0 <= coordinate[0] <= 5:
            raise ValueError("invalid column and rows")
    except ValueError as e:
        print("invalid input")
        return None
    Exception 
    return coordinate
    
def isspaceavailable(intendedCoordinate):

    if intendedCoordinate(intendedCoordinate) is None:
        return False
    rows,col=intendedCoordinate
    return gameboard[rows][col]==' '
    
    if(gameboard[intendedCoordinate[0]][intendedCoordinate[1]]=="🟡"):
        return False
    elif(gameboard[intendedCoordinate[0]][intendedCoordinate[1]]=="🔴"):
        return False
    else:
        return True
    

def gravitychecker(intendedCoordinate):
    #calculate space below
    spaceBelow=[None]*2
    spaceBelow[0]=intendedCoordinate[0]+1
    spaceBelow[1]=intendedCoordinate[1]
    
    #is the coordinate at ground level
    if(spaceBelow[0]==6):
        return True
    #check if there a token below
    if(isspaceavailable(spaceBelow)==False):
        return True
    return False

turncounter=0
while True:
    if(turncounter%2==0):
        printgameboard()
        while True:
            spacePicked=input("\n choose a space: ")
            coordinate=coordinateParser(spacePicked)
            try:
                #check if space is available
                if(isspaceavailable(coordinate)and gravitychecker(coordinate)):
                    modifyarray(coordinate,'🟡')
                    break
                else:
                    print("not a valid coordinate")
            except:
                print("error occured, please try again . ")
        winner=checkforwinner('🟡')
        turncounter+=1
    #it computer turn
    else:
        while True:
            cpuChoice=[random.choice(possibleletters),random.randint(0,5)]
            cpuCoordinate=coordinateParser(cpuChoice)
            if(isspaceavailable(cpuCoordinate)and gravitychecker(cpuCoordinate)):
                modifyarray(coordinate,'🔴')
                break
        turncounter+=1
        winner=checkforwinner('🔴')

    if(winner):
        printgameboard()
        break