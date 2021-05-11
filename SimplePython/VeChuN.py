print("Chương trình vẽ chữ N bằng dấu * với độ cao h")
while True:
    h = int(input("Nhập độ cao h: "))
    for i in range(h):
        for j in range(h):
            if j==0 or j==i or j==h-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("",end="\n")
    print("-"*13)

    i=0
    j=0
    while i<=h-1:
        while j<=h-1:
            if j==0 or j==i or j==h-1:
                print("*",end="")
            else:
                print(" ",end="")
            j+=1
        j=0
        i+=1
        print("")
    print("-"*13)