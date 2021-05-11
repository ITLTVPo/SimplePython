print("BẢNG CỬU CHƯƠNG")
for i in range(1,11):
    for j in range (2,10):
        print("{0:>2}x{1:>2} = {2:>2}".format(j,i,i*j),end="\t")
    print()


