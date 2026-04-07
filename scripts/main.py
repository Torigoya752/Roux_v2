EDGE_POSITION_MASK = 1 << 12 -1
ALL_MASK = (1 << 144) - 1
GOOD_CUBE = 0x543210000076543210000000ba9876543210
TUPLE_EO_1 = (1,0,2,3)
TUPLE_CO_1 = (1,2,0,3)
TUPLE_CO_2 = (2,0,1,3)


def goU(cube0):
    tempCube = cube0
    temp0 = cube0 & 0xf
    temp1 = (cube0 & 0xf0) >> 4
    temp2 = (cube0 & 0xf00) >> 8
    temp3 = (cube0 & 0xf000) >> 12
    tempCube = tempCube & (ALL_MASK ^ 0xffff)
    tempCube = tempCube | (temp0 << 4) | (temp1 << 8) | (temp2 << 12) | (temp3)
    # eo
    temp0 = (cube0 >> 48) & 0x3
    temp1 = (cube0 >> 50) & 0x3
    temp2 = (cube0 >> 52) & 0x3
    temp3 = (cube0 >> 54) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 48))
    tempCube = tempCube | (temp0 << 50) | (temp1 << 52) | (temp2 << 54) | (temp3 << 48)
    # cp
    temp0 = (cube0 >> 72) & 0xf
    temp1 = (cube0 >> 76) & 0xf
    temp2 = (cube0 >> 80) & 0xf
    temp3 = (cube0 >> 84) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xffff << 72))
    tempCube = tempCube | (temp0 << 76) | (temp1 << 80) | (temp2 << 84) | (temp3 << 72)
    # co
    temp0 = (cube0 >> 104) & 0x3
    temp1 = (cube0 >> 106) & 0x3
    temp2 = (cube0 >> 108) & 0x3
    temp3 = (cube0 >> 110) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 104))
    tempCube = tempCube | (temp0 << 106) | (temp1 << 108) | (temp2 << 110) | (temp3 << 104)
    return tempCube

def goU1(cube0):
    # ep
    tempCube = cube0
    temp0 = cube0 & 0xf
    temp1 = (cube0 & 0xf0) >> 4
    temp2 = (cube0 & 0xf00) >> 8
    temp3 = (cube0 & 0xf000) >> 12
    tempCube = tempCube & (ALL_MASK ^ 0xffff)
    tempCube = tempCube | (temp0 << 12) | (temp1) | (temp2 << 4) | (temp3 << 8)
    # eo
    temp0 = (cube0 >> 48) & 0x3
    temp1 = (cube0 >> 50) & 0x3
    temp2 = (cube0 >> 52) & 0x3
    temp3 = (cube0 >> 54) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 48))
    tempCube = tempCube | (temp0 << 54) | (temp1 << 48) | (temp2 << 50) | (temp3 << 52)
    # cp
    temp0 = (cube0 >> 72) & 0xf
    temp1 = (cube0 >> 76) & 0xf
    temp2 = (cube0 >> 80) & 0xf
    temp3 = (cube0 >> 84) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xffff << 72))
    tempCube = tempCube | (temp0 << 84) | (temp1 << 72) | (temp2 << 76) | (temp3 << 80)
    # co
    temp0 = (cube0 >> 104) & 0x3
    temp1 = (cube0 >> 106) & 0x3
    temp2 = (cube0 >> 108) & 0x3
    temp3 = (cube0 >> 110) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 104))
    tempCube = tempCube | (temp0 << 110) | (temp1 << 104) | (temp2 << 106) | (temp3 << 108)
    return tempCube

def goU2(cube0):
    tempCube = cube0
    # ep
    temp0 = cube0 & 0xf
    temp1 = (cube0 & 0xf0) >> 4
    temp2 = (cube0 & 0xf00) >> 8
    temp3 = (cube0 & 0xf000) >> 12
    tempCube = tempCube & (ALL_MASK ^ 0xffff)
    tempCube = tempCube | (temp0 << 8) | (temp1 << 12) | (temp2) | (temp3 << 4)
    # eo
    temp0 = (cube0 >> 48) & 0x3
    temp1 = (cube0 >> 50) & 0x3
    temp2 = (cube0 >> 52) & 0x3
    temp3 = (cube0 >> 54) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 48))
    tempCube = tempCube | (temp0 << 52) | (temp1 << 54) | (temp2 << 48) | (temp3 << 50)
    # cp
    temp0 = (cube0 >> 72) & 0xf
    temp1 = (cube0 >> 76) & 0xf
    temp2 = (cube0 >> 80) & 0xf
    temp3 = (cube0 >> 84) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xffff << 72))
    tempCube = tempCube | (temp0 << 80) | (temp1 << 84) | (temp2 << 72) | (temp3 << 76)
    # co
    temp0 = (cube0 >> 104) & 0x3
    temp1 = (cube0 >> 106) & 0x3
    temp2 = (cube0 >> 108) & 0x3
    temp3 = (cube0 >> 110) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 104))
    tempCube = tempCube | (temp0 << 108) | (temp1 << 110) | (temp2 << 104) | (temp3 << 106)
    return tempCube

def goD(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> 32) & 0xf
    temp1 = (cube0 >> 36) & 0xf
    temp2 = (cube0 >> 40) & 0xf
    temp3 = (cube0 >> 44) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xffff00000000)
    tempCube = tempCube | (temp0 << 44) | (temp1 << 32) | (temp2 << 36) | (temp3 << 40)
    # eo
    temp0 = (cube0 >> 64) & 0x3
    temp1 = (cube0 >> 66) & 0x3
    temp2 = (cube0 >> 68) & 0x3
    temp3 = (cube0 >> 70) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 64))
    tempCube = tempCube | (temp0 << 70) | (temp1 << 64) | (temp2 << 66) | (temp3 << 68)
    # cp
    temp0 = (cube0 >> 88) & 0xf
    temp1 = (cube0 >> 92) & 0xf
    temp2 = (cube0 >> 96) & 0xf
    temp3 = (cube0 >> 100) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xffff << 88))
    tempCube = tempCube | (temp0 << 100) | (temp1 << 88) | (temp2 << 92) | (temp3 << 96)
    # co
    temp0 = (cube0 >> 112) & 0x3
    temp1 = (cube0 >> 114) & 0x3
    temp2 = (cube0 >> 116) & 0x3
    temp3 = (cube0 >> 118) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 112))
    tempCube = tempCube | (temp0 << 118) | (temp1 << 112) | (temp2 << 114) | (temp3 << 116)
    return tempCube

def goD1(cube0):
    tempCube = cube0
    temp0 = (cube0 >> 32) & 0xf
    temp1 = (cube0 >> 36) & 0xf
    temp2 = (cube0 >> 40) & 0xf
    temp3 = (cube0 >> 44) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xffff00000000)
    tempCube = tempCube | (temp0 << 36) | (temp1 << 40) | (temp2 << 44) | (temp3 << 32)
    # eo
    temp0 = (cube0 >> 64) & 0x3
    temp1 = (cube0 >> 66) & 0x3
    temp2 = (cube0 >> 68) & 0x3
    temp3 = (cube0 >> 70) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 64))
    tempCube = tempCube | (temp0 << 66) | (temp1 << 68) | (temp2 << 70) | (temp3 << 64)
    # cp
    temp0 = (cube0 >> 88) & 0xf
    temp1 = (cube0 >> 92) & 0xf
    temp2 = (cube0 >> 96) & 0xf
    temp3 = (cube0 >> 100) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xffff << 88))
    tempCube = tempCube | (temp0 << 92) | (temp1 << 96) | (temp2 << 100) | (temp3 << 88)
    # co
    temp0 = (cube0 >> 112) & 0x3
    temp1 = (cube0 >> 114) & 0x3
    temp2 = (cube0 >> 116) & 0x3
    temp3 = (cube0 >> 118) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 112))
    tempCube = tempCube | (temp0 << 114) | (temp1 << 116) | (temp2 << 118) | (temp3 << 112)
    return tempCube

def goD2(cube0):
    tempCube = cube0
    temp0 = (cube0 >> 32) & 0xf
    temp1 = (cube0 >> 36) & 0xf
    temp2 = (cube0 >> 40) & 0xf
    temp3 = (cube0 >> 44) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xffff00000000)
    tempCube = tempCube | (temp0 << 40) | (temp1 << 44) | (temp2 << 32) | (temp3 << 36)
    # eo
    temp0 = (cube0 >> 64) & 0x3
    temp1 = (cube0 >> 66) & 0x3
    temp2 = (cube0 >> 68) & 0x3
    temp3 = (cube0 >> 70) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 64))
    tempCube = tempCube | (temp0 << 68) | (temp1 << 70) | (temp2 << 64) | (temp3 << 66)
    # cp
    temp0 = (cube0 >> 88) & 0xf
    temp1 = (cube0 >> 92) & 0xf
    temp2 = (cube0 >> 96) & 0xf
    temp3 = (cube0 >> 100) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xffff << 88))
    tempCube = tempCube | (temp0 << 96) | (temp1 << 100) | (temp2 << 88) | (temp3 << 92)
    # co
    temp0 = (cube0 >> 112) & 0x3
    temp1 = (cube0 >> 114) & 0x3
    temp2 = (cube0 >> 116) & 0x3
    temp3 = (cube0 >> 118) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xff << 112))
    tempCube = tempCube | (temp0 << 116) | (temp1 << 118) | (temp2 << 112) | (temp3 << 114)
    return tempCube

def goR(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> 12) & 0xf
    temp1 = (cube0 >> 24) & 0xf
    temp2 = (cube0 >> 44) & 0xf
    temp3 = (cube0 >> 28) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xf000ff00f000)
    tempCube = tempCube | (temp0 << 24) | (temp1 << 44) | (temp2 << 28) | (temp3 << 12)
    # eo
    temp0 = (cube0 >> (48 + 3*2)) & 0x3
    temp1 = (cube0 >> (48 + 6*2)) & 0x3
    temp2 = (cube0 >> (48 + 11*2)) & 0x3
    temp3 = (cube0 >> (48 + 7*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xc0f0c0 << 48))
    tempCube = tempCube | (temp0 << (48 + 6*2)) | (temp1 << (48 + 11*2)) | (temp2 << (48 + 7*2)) | (temp3 << (48 + 3*2))
    # cp
    temp0 = (cube0 >> (72 + 3*4)) & 0xf
    temp1 = (cube0 >> (72 + 2*4)) & 0xf
    temp2 = (cube0 >> (72 + 6*4)) & 0xf
    temp3 = (cube0 >> (72 + 7*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xff00ff00 << 72))
    tempCube = tempCube | (temp0 << (72 + 2*4)) | (temp1 << (72 + 6*4)) | (temp2 << (72 + 7*4)) | (temp3 << (72 + 3*4))
    # co
    temp0 = TUPLE_CO_1[(cube0 >> (104 + 3*2)) & 0x3]
    temp1 = TUPLE_CO_2[(cube0 >> (104 + 2*2)) & 0x3]
    temp2 = TUPLE_CO_1[(cube0 >> (104 + 6*2)) & 0x3]
    temp3 = TUPLE_CO_2[(cube0 >> (104 + 7*2)) & 0x3]
    tempCube = tempCube & (ALL_MASK ^ (0xf0f0 << 104))
    tempCube = tempCube | (temp0 << (104 + 2*2)) | (temp1 << (104 + 6*2)) | (temp2 << (104 + 7*2)) | (temp3 << (104 + 3*2))
    return tempCube

def goR1(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> (3*4)) & 0xf
    temp1 = (cube0 >> (7*4)) & 0xf
    temp2 = (cube0 >> (11*4)) & 0xf
    temp3 = (cube0 >> (6*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xf000ff00f000)
    tempCube = tempCube | (temp0 << (7*4)) | (temp1 << (11*4)) | (temp2 << (6*4)) | (temp3 << (3*4))
    # eo 
    temp0 = (cube0 >> (48 + 3*2)) & 0x3
    temp1 = (cube0 >> (48 + 7*2)) & 0x3
    temp2 = (cube0 >> (48 + 11*2)) & 0x3
    temp3 = (cube0 >> (48 + 6*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xc0f0c0 << 48))
    tempCube = tempCube | (temp0 << (48 + 7*2)) | (temp1 << (48 + 11*2)) | (temp2 << (48 + 6*2)) | (temp3 << (48 + 3*2))
    # cp
    temp0 = (cube0 >> (72 + 2*4)) & 0xf
    temp1 = (cube0 >> (72 + 3*4)) & 0xf
    temp2 = (cube0 >> (72 + 7*4)) & 0xf
    temp3 = (cube0 >> (72 + 6*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xff00ff00 << 72))
    tempCube = tempCube | (temp0 << (72 + 3*4)) | (temp1 << (72 + 7*4)) | (temp2 << (72 + 6*4)) | (temp3 << (72 + 2*4))
    # co
    temp0 = TUPLE_CO_2[(cube0 >> (104 + 2*2)) & 0x3]
    temp1 = TUPLE_CO_1[(cube0 >> (104 + 3*2)) & 0x3]
    temp2 = TUPLE_CO_2[(cube0 >> (104 + 7*2)) & 0x3]
    temp3 = TUPLE_CO_1[(cube0 >> (104 + 6*2)) & 0x3]
    tempCube = tempCube & (ALL_MASK ^ (0xf0f0 << 104))
    tempCube = tempCube | (temp0 << (104 + 3*2)) | (temp1 << (104 + 7*2)) | (temp2 << (104 + 6*2)) | (temp3 << (104 + 2*2))
    return tempCube
    
def goR2(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> 12) & 0xf
    temp1 = (cube0 >> 24) & 0xf
    temp2 = (cube0 >> 44) & 0xf
    temp3 = (cube0 >> 28) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xf000ff00f000)
    tempCube = tempCube | (temp0 << 44) | (temp1 << 28) | (temp2 << 12) | (temp3 << 24)
    # eo
    temp0 = (cube0 >> (48 + 3*2)) & 0x3
    temp1 = (cube0 >> (48 + 6*2)) & 0x3
    temp2 = (cube0 >> (48 + 11*2)) & 0x3
    temp3 = (cube0 >> (48 + 7*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xc0f0c0 << 48))
    tempCube = tempCube | (temp0 << (48 + 11*2)) | (temp1 << (48 + 7*2)) | (temp2 << (48 + 3*2)) | (temp3 << (48 + 6*2))
    # cp
    temp0 = (cube0 >> (72 + 3*4)) & 0xf
    temp1 = (cube0 >> (72 + 2*4)) & 0xf
    temp2 = (cube0 >> (72 + 6*4)) & 0xf
    temp3 = (cube0 >> (72 + 7*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xff00ff00 << 72))
    tempCube = tempCube | (temp0 << (72 + 6*4)) | (temp1 << (72 + 7*4)) | (temp2 << (72 + 3*4)) | (temp3 << (72 + 2*4))
    # co
    temp0 = (cube0 >> (104 + 3*2)) & 0x3
    temp1 = (cube0 >> (104 + 2*2)) & 0x3
    temp2 = (cube0 >> (104 + 6*2)) & 0x3
    temp3 = (cube0 >> (104 + 7*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xf0f0 << 104))
    tempCube = tempCube | (temp0 << (104 + 6*2)) | (temp1 << (104 + 7*2)) | (temp2 << (104 + 3*2)) | (temp3 << (104 + 2*2))
    return tempCube

def goL(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> (1*4)) & 0xf
    temp1 = (cube0 >> (4*4)) & 0xf
    temp2 = (cube0 >> (9*4)) & 0xf
    temp3 = (cube0 >> (5*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xf000ff00f0)
    tempCube = tempCube | (temp0 << (4*4)) | (temp1 << (9*4)) | (temp2 << (5*4)) | (temp3 << (1*4))
    # eo
    temp0 = (cube0 >> (48 + 1*2)) & 0x3
    temp1 = (cube0 >> (48 + 4*2)) & 0x3
    temp2 = (cube0 >> (48 + 9*2)) & 0x3
    temp3 = (cube0 >> (48 + 5*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xc0f0c << 48))
    tempCube = tempCube | (temp0 << (48 + 4*2)) | (temp1 << (48 + 9*2)) | (temp2 << (48 + 5*2)) | (temp3 << (48 + 1*2))
    # cp
    temp0 = (cube0 >> (72 + 1*4)) & 0xf
    temp1 = (cube0 >> (72 + 0*4)) & 0xf
    temp2 = (cube0 >> (72 + 4*4)) & 0xf
    temp3 = (cube0 >> (72 + 5*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xff00ff << 72))
    tempCube = tempCube | (temp0 << (72 + 0*4)) | (temp1 << (72 + 4*4)) | (temp2 << (72 + 5*4)) | (temp3 << (72 + 1*4))
    # co
    temp0 = TUPLE_CO_1[(cube0 >> (104 + 1*2)) & 0x3]
    temp1 = TUPLE_CO_2[(cube0 >> (104 + 0*2)) & 0x3]
    temp2 = TUPLE_CO_1[(cube0 >> (104 + 4*2)) & 0x3]
    temp3 = TUPLE_CO_2[(cube0 >> (104 + 5*2)) & 0x3]
    tempCube = tempCube & (ALL_MASK ^ (0xf0f << 104))
    tempCube = tempCube | (temp0 << (104 + 0*2)) | (temp1 << (104 + 4*2)) | (temp2 << (104 + 5*2)) | (temp3 << (104 + 1*2))
    return tempCube

def goL1(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> (1*4)) & 0xf
    temp1 = (cube0 >> (5*4)) & 0xf
    temp2 = (cube0 >> (9*4)) & 0xf
    temp3 = (cube0 >> (4*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xf000ff00f0)
    tempCube = tempCube | (temp0 << (5*4)) | (temp1 << (9*4)) | (temp2 << (4*4)) | (temp3 << (1*4))
    # eo
    temp0 = (cube0 >> (48 + 1*2)) & 0x3
    temp1 = (cube0 >> (48 + 5*2)) & 0x3
    temp2 = (cube0 >> (48 + 9*2)) & 0x3
    temp3 = (cube0 >> (48 + 4*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xc0f0c << 48))
    tempCube = tempCube | (temp0 << (48 + 5*2)) | (temp1 << (48 + 9*2)) | (temp2 << (48 + 4*2)) | (temp3 << (48 + 1*2))
    # cp
    temp0 = (cube0 >> (72 + 1*4)) & 0xf
    temp1 = (cube0 >> (72 + 5*4)) & 0xf
    temp2 = (cube0 >> (72 + 4*4)) & 0xf
    temp3 = (cube0 >> (72 + 0*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xff00ff << 72))
    tempCube = tempCube | (temp0 << (72 + 5*4)) | (temp1 << (72 + 4*4)) | (temp2 << (72 + 0*4)) | (temp3 << (72 + 1*4))
    # co
    temp0 = TUPLE_CO_1[(cube0 >> (104 + 1*2)) & 0x3]
    temp1 = TUPLE_CO_2[(cube0 >> (104 + 5*2)) & 0x3]
    temp2 = TUPLE_CO_1[(cube0 >> (104 + 4*2)) & 0x3]
    temp3 = TUPLE_CO_2[(cube0 >> (104 + 0*2)) & 0x3]
    tempCube = tempCube & (ALL_MASK ^ (0xf0f << 104))
    tempCube = tempCube | (temp0 << (104 + 5*2)) | (temp1 << (104 + 4*2)) | (temp2 << (104 + 0*2)) | (temp3 << (104 + 1*2))
    return tempCube

def goL2(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> (1*4)) & 0xf
    temp1 = (cube0 >> (4*4)) & 0xf
    temp2 = (cube0 >> (9*4)) & 0xf
    temp3 = (cube0 >> (5*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xf000ff00f0)
    tempCube = tempCube | (temp0 << (9*4)) | (temp1 << (5*4)) | (temp2 << (1*4)) | (temp3 << (4*4))
    # eo
    temp0 = (cube0 >> (48 + 1*2)) & 0x3
    temp1 = (cube0 >> (48 + 4*2)) & 0x3
    temp2 = (cube0 >> (48 + 9*2)) & 0x3
    temp3 = (cube0 >> (48 + 5*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xc0f0c << 48))
    tempCube = tempCube | (temp0 << (48 + 9*2)) | (temp1 << (48 + 5*2)) | (temp2 << (48 + 1*2)) | (temp3 << (48 + 4*2))
    # cp
    temp0 = (cube0 >> (72 + 1*4)) & 0xf
    temp1 = (cube0 >> (72 + 0*4)) & 0xf
    temp2 = (cube0 >> (72 + 4*4)) & 0xf
    temp3 = (cube0 >> (72 + 5*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xff00ff << 72))
    tempCube = tempCube | (temp0 << (72 + 4*4)) | (temp1 << (72 + 5*4)) | (temp2 << (72 + 1*4)) | (temp3 << (72 + 0*4))
    # co
    temp0 = (cube0 >> (104 + 1*2)) & 0x3
    temp1 = (cube0 >> (104 + 0*2)) & 0x3
    temp2 = (cube0 >> (104 + 4*2)) & 0x3
    temp3 = (cube0 >> (104 + 5*2)) & 0x3
    tempCube = tempCube & (ALL_MASK ^ (0xf0f << 104))
    tempCube = tempCube | (temp0 << (104 + 4*2)) | (temp1 << (104 + 5*2)) | (temp2 << (104 + 1*2)) | (temp3 << (104 + 0*2))
    return tempCube

def goF(cube0):
    tempCube = cube0
    # ep
    temp0 = (cube0 >> (0*4)) & 0xf
    temp1 = (cube0 >> (7*4)) & 0xf
    temp2 = (cube0 >> (8*4)) & 0xf
    temp3 = (cube0 >> (4*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ 0xff00f000f)
    tempCube = tempCube | (temp0 << (7*4)) | (temp1 << (8*4)) | (temp2 << (4*4)) | (temp3 << (0*4))
    # eo
    temp0 = TUPLE_EO_1[(cube0 >> (48 + 0*2)) & 0x3]
    temp1 = TUPLE_EO_1[(cube0 >> (48 + 7*2)) & 0x3]
    temp2 = TUPLE_EO_1[(cube0 >> (48 + 8*2)) & 0x3]
    temp3 = TUPLE_EO_1[(cube0 >> (48 + 4*2)) & 0x3]
    tempCube = tempCube & (ALL_MASK ^ (0x3c303 << 48))
    tempCube = tempCube | (temp0 << (48 + 7*2)) | (temp1 << (48 + 8*2)) | (temp2 << (48 + 4*2)) | (temp3 << (48 + 0*2))
    # cp
    temp0 = (cube0 >> (72 + 0*4)) & 0xf
    temp1 = (cube0 >> (72 + 3*4)) & 0xf
    temp2 = (cube0 >> (72 + 7*4)) & 0xf
    temp3 = (cube0 >> (72 + 4*4)) & 0xf
    tempCube = tempCube & (ALL_MASK ^ (0xf00ff00f << 72))
    tempCube = tempCube | (temp0 << (72 + 3*4)) | (temp1 << (72 + 7*4)) | (temp2 << (72 + 4*4)) | (temp3 << (72 + 0*4))
    # co
    temp0 = TUPLE_CO_1[(cube0 >> (104 + 0*2)) & 0x3]
    temp1 = TUPLE_CO_2[(cube0 >> (104 + 3*2)) & 0x3]
    temp2 = TUPLE_CO_1[(cube0 >> (104 + 7*2)) & 0x3]
    temp3 = TUPLE_CO_2[(cube0 >> (104 + 4*2)) & 0x3]
    tempCube = tempCube & (ALL_MASK ^ (0xc3c3 << 104))
    tempCube = tempCube | (temp0 << (104 + 3*2)) | (temp1 << (104 + 7*2)) | (temp2 << (104 + 4*2)) | (temp3 << (104 + 0*2))
    return tempCube
    
if (__name__ == "__main__"):
    cube0 = GOOD_CUBE
    for i in range(4):
        cube0 = goF(cube0)
    print((hex)(cube0))
    print(cube0 == GOOD_CUBE)