def DocSoThanhChu():
    a = ["một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
    b = ["mốt","hai","ba","tư","lăm","sáu","bảy","tám","chín"]
    SoAm=False
    number = int(input("Nhập số bạn muốn chuyển đổi: "))
    if (number <0):
        number = 0-number
        SoAm =True
    if (number==0):
        print("Không")
    if (number>0):
        if (number>0 and number<10):
            s=str(a[number-1])
        elif (number==10):
            s="Mười"
        elif (number>10 and number<20):
            if (number==15):
                s = "Mười lăm"
            else:
                s = "Mười " + a[number%10-1]
        elif (number>=20):
            if (number%10==0):
                s = a[number//10-1] + " mươi "
            else:
                s = a[number//10-1] + " mươi "+ b[number%10-1]
    if SoAm == True:
        s = "Âm "+s
    s = s.capitalize()
    print("{0} đọc là: {1}".format(str(number),str(s)))

def TimNgayTiepTheo():
    ngay = int(input("Ngày hiện tại: "))
    thang = int(input("Tháng hiện tại: "))
    nam = int(input("Năm hiện tại: "))
    if ((nam%400 == 0 or (nam%4 == 0 and nam//100 != 0)) and thang==2 and ngay==29):
        print("Ngày mai là: ngày 1 tháng 3 năm ",nam)
    elif (thang==2 and ngay==28):
        print("Ngày mai là: ngày 1 tháng 3 năm ",nam)
    elif (str(thang) in ("1","3","5","7","8","10","12") and ngay==31):
        print("Ngày mai là: ngày 1 tháng {0} năm {1}".format(thang+1, nam))
    elif (str(thang) in ("4","6","11","9") and ngay==30):
        print("Ngày mai là: ngày 1 tháng {0} năm {1}".format(thang+1, nam))
    else:
        print("Ngày mai là: ngày {0} tháng {1} năm {2}".format(ngay+1, thang, nam))

def PhepTinhDonGian():
    print("Nhập vào hai số a và b")
    a = int(input("a = "))
    b = int(input("b = "))
    PhepToan = input("Nhập vào phép toán cộng bạn muốn sử dụng (+), trừ (-), nhân (*), chia (/) ")
    if PhepToan=="+":
        print("{} + {} = {}".format(a,b,a+b))
    elif PhepToan=="-":
        print("{} - {} = {}".format(a,b,a-b))
    elif PhepToan=="*":
        print("{} * {} = {}".format(a,b,a*b))
    elif PhepToan=="/":
        if b==0:
            print("b phải khác 0!")
        else:
            print("{} / {} = {}".format(a,b,a/b))


while (True):
    x = input("""Chọn một option:
    1. Chuyển đổi số sang chữ (2 chữ số)
    2. Nhập vào ngày tháng năm, tìm ngày kế tiếp
    3. Nhập vào a và b, chọn + - * /
    4. Nhập vào một tháng, xuất ra tháng thuộc quí mấy \n""")
    if (x=='1'):
        DocSoThanhChu()
    elif (x=='2'):
        TimNgayTiepTheo()
    elif (x=='3'):
        PhepTinhDonGian()
    elif (x=='4'):
        month = int(input("Nhập vào tháng bạn muốn kiếm tra: "))
        print("Tháng {0} thuộc quí: {1}".format(str(month),month//3+1))
    else:
        print("Bạn đã nhập sai giá trị, chương trình tự động thoát...")
        break
