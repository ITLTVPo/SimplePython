print("Chương trình tính tổng dãy số s = x +... + x^n/n!")
while True:
    s=0
    x=int(input("Nhập x: "))
    n=int(input("Nhập n: "))
    for i in range(1,n+1):
        tu = x**i
        mau=1
        for j in range(1,i+1):
            mau = mau * j
        s+=tu/mau
    print("Đáp án là: ",s)
    print("-"*10)