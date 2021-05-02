print("Chương trình tính trung bình của một dãy số")
sum=0
count = 0
flag=0
test=True
while (test==True):
    temp = float(input("Vui lòng nhập một số dương: "))
    if temp<0:
        print("Không thể nhập số nhỏ hơn 0...")
        if flag==0:
            flag+=1
            continue
        else:
            test=False
    else:
        count+=1
        sum=sum+temp
else:
    if count>0:
        print("Giá trị trung bình của dãy số bạn đưa là: ", sum/count)
    else: 
        print("Bạn chưa nhập giá trị đúng nào cả, thoát chương trình...")