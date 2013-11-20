from py2scad import *

x = INCH2MM*(18.0+3.0/8.0)
y = INCH2MM*3.5
y = INCH2MM*5.0
z = INCH2MM*0.25

mountHoleDiam = INCH2MM*0.1960
mountHoleSpacingX = INCH2MM*17.5*0.5
mountHoleSpacingY = INCH2MM*1.0

slotLength = INCH2MM*7.5
slotWidth = mountHoleDiam
slotRadius = 0.5*mountHoleDiam
slotSpacingX = 0.5*mountHoleSpacingX
slotSpacingY = mountHoleSpacingY

# Add holes
holeList = []
for i in (-1,0,1):
    for j in (-1,0,1):
        posX = mountHoleSpacingX*i
        posY = mountHoleSpacingY*j
        hole = (posX,posY,mountHoleDiam)
        holeList.append(hole)


plate = plate_w_holes(x,y,z,holeList) 


# Add slots

slotBase = rounded_box(slotLength,slotWidth,2*z,slotRadius, round_z=False)

slotList = []
for i in (-1,1):
    for j in (-1,0,1):
        posX = slotSpacingX*i
        posY = slotSpacingY*j
        slotTemp = Translate(slotBase,v=(posX,posY,0))
        slotList.append(slotTemp)

plate = Difference([plate] + slotList)
plate = Projection(plate)


prog = SCAD_Prog()
prog.fn = 50
prog.add([plate,])
prog.write('taig_plate.scad')


