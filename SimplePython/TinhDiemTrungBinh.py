print("Chương trình tính điểm trung bình của học sinh\n\n")
print("Nhập vào điểm các môn Toán, Lý, Hóa và chương trình sẽ tính điểm trung bình của học sinh\n")
print("="*30)
try:
    while (True):
        toan = int(input("Điểm Toán của học sinh là: "))
        ly = int(input("Điểm Lý của học sinh là: "))
        hoa  = int(input("Điểm Hóa của học sinh là: "))
        dtb = (toan+ly+hoa)/3
        print("Điểm trung bình của học sinh là: ",round(dtb,2))
except:
    print("Oops, something has gone wrong...")