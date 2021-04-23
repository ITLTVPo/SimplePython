print("Chương trình giải phương trình bậc hai: ax**2 + bx + c = 0")
try:
    while(True):
        a=float(input("a = "))
        b=float(input("b = "))
        c=float(input("c = "))
        delta = b**2 - 4*a*c
        if delta<0: 
            print("delta = b**2 - 4*a*c = ",delta)
            print("delta < 0 -> Phương trình vô nghiệm")
        elif delta>=0:
            print("delta = b**2 - 4*a*c = ",delta)
            print("Phương trình có nghiệm x1 = ",(-b + delta ** (1/2))/(2*a))
            print("Phương trình có nghiệm x2 = ",(-b - delta ** (1/2))/(2*a))
except: 
    print("Oops, something has gone wrong...")