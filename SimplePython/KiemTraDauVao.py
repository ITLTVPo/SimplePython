import math
value=1
try: 
    while value>-1 and value <10:
        value=int(input("Nhập vào số nguyên dương nhỏ hơn 10: "))
        print("Căn bậc hai của số đó là ",math.sqrt(value))
    print("Kết thúc chương trình...")
except:
    print("Oops, something has gone wrong! ")