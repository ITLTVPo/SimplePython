import math
print("Chương trình kiểm tra số nguyên tố đơn giản O(sqrt(n))")
while True:
    result = True
    n= int(input("Số cần kiểm tra: "))
    if n<=2:
        result=False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            result = False
    if result==False:
        print("Không phải là số nguyên tố")
    else:
        print("Là số nguyên tố")