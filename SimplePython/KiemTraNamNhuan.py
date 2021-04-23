print("="*30)
print("Chương trình kiểm tra năm nhuần")
try:
    while (True):
        print("-"*30)
        x= int(input("Nhập vào số năm cần tính: "))
        if ((x % 400 == 0) or (x % 4 == 0 and x % 100 != 0)):
            print("Năm ",x, " là năm nhuần")
        else:
            print("Năm ",x," không phải là năm nhuần")
except:
    print("Oops, something has gone wrong...")