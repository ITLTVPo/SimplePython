print("Chương trình tính tổng các số chẵn / lẻ từ 1 đến n")
n = int(input("Nhập n = "))
s=0
if n<0:
    print("Vui lòng nhập n > 0\n")
else:
    if n%2==0:
        for i in range(2,n+1,2):
            s+=i
        print("Tổng các số chẵn từ 0 đến n là: ",s)
    else:
        for i in range(1,n+1,2):
            s+=i
        print("Tổng các số lẻ từ 0 đến n là: ",s)

