from time import time, sleep
while True:
    n = int(input("Đồng hồ đếm ngược... Vui lòng nhập số giây: "))
    start = time()
    for i in range(n,0,-1):
        print("Bạn còn lại {0} giây...".format(i))
        sleep(1)
    duration = time() - start
    print("Mất tổng cộng {0} giây để đếm".format(duration))
    print("=====================")