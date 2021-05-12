print("Vẽ hình vuông")
h=int(input("Độ dài cạnh hình vuông: "))
for i in range(h):
    for j in range(h):
        if i==0 or i==h-1:
            print("*",end="")
        elif j==0 or j==h-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for i in range(h):
    for j in range(h):
        if j>=h-i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

h=h*2-1
for i in range(h):
    for j in range(h):
        if (i<(h+1)/2-1):
            if j==0:
                print("*",end="")
            elif j==i:
                print("*",end="")
            else:
                print(" ",end="")
        elif (i==(h+1)/2-1):
            print("*",end="")
        elif (i>(h+1)/2-1):
            if j==h-1:
                print("*",end="")
            elif j==i:
                print("*",end="")
            else:
                print(" ",end="")
    print()

print("Chương trình tính S(x,n)")
x=int(input("Nhập x = "))
n=int(input("Nhập n = "))
s=x
for i in range(1,n+1):
    tu=x**(2*i+1)
    mau=1
    for j in range(2,i*2+2):
        mau=mau*j
    print(tu)
    print(mau)
    s+=tu/mau
print(s)