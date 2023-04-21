def houseArea(l,w):
    print(f"The area is {l*w}")
    # return l*w

def circCirc(r):
    from math import pi
    print(f"The circumference is {r*2*pi}")
    # return (float(r)*2*pi)


def prompter():
    #Assuming valid inputs
    what_do=input("Choose to calculate house area (ha) or circle circumference (cc): ")
    if what_do=="ha":
        l=input("Enter length: ")
        w=input("Enter width: ")
        try:
            houseArea(int(l),int(w))
        except:
            houseArea(float(l),float(w))
    elif what_do=="cc":
        r=input("Enter radius: ")
        circCirc(float(r)) #pi means this is always gonna be floats
    else:
        print("Bad input")