print("-"*30)
print("Chương trình tính chu vi hoặc diện tích đường tròn")
import math
pi=math.pi

def ChuVi(r):
    return r*2*pi

def DienTich(r):
    return r*r*pi
try: 
    while (True):
        print ("-"*20)
        print("""Hãy chọn phép toán bạn muốn sử dụng: 
        1. Tính chu vi
        2. Tính diện tích
        3. Thoát ứng dụng\n""")
        x = input()
        if (x=="1"):
            r = input("Bán kính đường tròn = ")
            print("{0} là chu vi của đường tròn".format(ChuVi(int(r))))
            continue
        if (x=="2"):
            r = input("Bán kính đường tròn = ")
            print("{0} là diện tích của đường tròn".format(DienTich(int(r))))
            continue
        if (x=="3"):
            break
        print("Xin hãy chọn 1, 2 hoặc 3")
except:
    print("Something is Wrong!!!")

    