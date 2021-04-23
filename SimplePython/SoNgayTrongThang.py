print("Đếm số ngày trong tháng")

def KiemTraNamNhuan(month, NamNhuan):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif NamNhuan==True:
        return 29
    elif NamNhuan==False:
        return 28
try:
    while (True): 
        print("-"*30)
        month = int(input("Nhập tháng bạn muốn kiểm tra: "))
        year = int(input("Tháng đó nằm trong năm: "))
        if (year%400==0 or (year%4==0 and year%100!=0)):
            print("Tháng đó có: ", KiemTraNamNhuan(month,True))
        else:
            print("Tháng đó có: ", KiemTraNamNhuan(month,False))
except:
    print("Oops, something has gone wrong...")
