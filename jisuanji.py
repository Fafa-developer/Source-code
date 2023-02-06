import time
print("-"*35)
print("欢迎使用计算机汐桶")
while True:
    print("记住：只支持加法，减法，乘法和除法")
    a=input('计算方式：')
    ab=int(input('加减乘除的第一位数字:'))
    ac=int(input('加减乘除的第二位数字:'))
    if a=="加法":
        b=ab+ac
        print("结果是：%s"%(b))
        r=input('是否退出？：')
        if r=="是":
            print("-"*35)
            break
    elif a=="减法":
        c=ab-ac
        print("结果是：%s"%(c))
        print("-"*35)
        p=input('是否退出？:')
        if p=="是":
            print("-"*35)
            break
    elif a=="乘法":
        d=ab*ac
        print("结果是：%s"%(d))
        t=input('是否退出？：')
        if t=="是":
            print("-"*35)
            break
    elif a=="除法":
        if ac==0:
            print("md除数写0逝吧？小学老师没教过你除数不能是0吗？")
            time.sleep(2)
        else:
            qwe=input('使用保留小数点还是输出整数(除不尽四舍五入)？:')
            if qwe=="输出整数":
                e=ab//ac
                print("结果是：%s"%(e))
                y=input('是否退出？：')
                if y=="是":
                    print("-"*35)
                    break
            if qwe=="保留小数点":
                f=ab/ac
                print("结果是：%s"%(f))
                u=input('是否退出？：')
                if u=="是":
                    print("-"*35)
                    break
            else:
                input('出了一些问题，请重新输入(按enter键重试)')                                                                         
    else:
        input('出了一些问题，请重新输入(按enter键重试)')
