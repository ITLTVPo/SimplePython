print("Chương trình thử For Else")
a = int(input("Nhập vào số nguyên a lớn hơn 2: "))
sum=0
if a>2:
    for i in range(2,a,2):
        sum +=i
        if sum > 10: 
            print ("Tổng số chẵn từ 2 đến a lớn hơn 10")
            break
    else:
        print("Tổng số chẵn từ 2 đến a nhỏ hơn 10")
else:
    print("Nhập sai dữ liệu")