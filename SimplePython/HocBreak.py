print("Chương trình kiểm tra tính chẵn lẻ")
while True:
    x = int(input("Nhập vào một số nguyên dương x, hoặc 0 để exit: "))
    if x>0:
        if (x%2==0):
            print("x là số chẵn")
        else:
            print("x là số lẻ")
    elif x==0:
        print("Xin cảm ơn đã sử dụng phần mềm")
        break
    else: 
        print("Vui lòng nhập đúng theo yêu cầu")