```
from time import sleep, time, mktime, strptime, strftime, localtime

TargetTimeInput = "2018-12-4 13:30:00"

if __name__ == '__main__':
    TargetTime = mktime(strptime(TargetTimeInput, '%Y-%m-%d %H:%M:%S'))
    CountTime = TargetTime - time()
    print("抢券目标时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(TargetTime)) )
    print("当前时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(time())) )

    while CountTime > 1:
        print("抢券倒计时：%s 分 %s 秒" % (abs(int(CountTime)) // 60, abs(int(CountTime)) % 60))
        CountTime = CountTime - 1
        sleep(1)

```
