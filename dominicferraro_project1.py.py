#Dominic Ferraro; Project01; 9-28-22
#This program does the following:
#receives input for the length, width, and shade of a room. 
#The program than calculates and outputs the correct window unit air conditioner that is needed to cool the room.
#=============================================================variables declared
BTU = 0
shadePrint = str("Dummy")
stringObject = str("Air Conditioning Window Unit Cooling Capacity\n")
#==============================================================input statements
length = float(input("Please enter the length of the room (in feet): "))
width = float(input("Please enter the width of the room (in feet): "))
shade = int(input("What is the amount of shade that this room receives? \n 1. Little Shade \n 2. Moderate Shade \n 3. Abundant Shade\n Please select from the options above: "))
#===========================================================Processing Statements
area = length*width
if area < 250:
  BTU = 5500
elif area > 250 and area < 500:
  BTU = 10000
elif area > 501 and area < 1000:
  BTU = 17500
elif area > 1000:
  BTU = 24000
if shade == 1:
  BTU = (BTU*1.15)
  shadePrint = str("Little")
elif shade == 3:
  BTU = BTU*.9
  shadePrint = str("Abundant")
elif shade == 2:
  shadePrint = str("Moderate")
#=====================================================Output statement
print('\n',stringObject)
print("Room Area (in square feet): ",area)
print("Amount of Shade: ", shadePrint)
print("BTU's Per Hour needed: ","{:,}".format(int(round(BTU))))
