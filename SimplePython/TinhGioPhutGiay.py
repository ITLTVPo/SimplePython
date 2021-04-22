print("="*30)
print("Chương trình tính giờ phút giây...")
print("HDSD: Nhập vào một thời gian và qui đổi ra số giờ, phút, giây tương ứng")
try:
    while (True):
        temp = input("Nhập số giây mà bạn muốn qui đổi: ")
        s = int(temp)
        h = s//3600
        s -= h*3600
        m = s//60
        s -= m*60
        print("{0} giây tương ứng với: {1} giờ {2} phút {3} giây".format(temp,h,m,s))
        print("-"*30)
except:
    print("Oops, something is wrong...!")