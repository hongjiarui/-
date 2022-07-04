import random
while True:
    xsgs = input('请输入学生个数或输入q退出：')
    if xsgs.isdigit():
        while True:
                cxhgs = input('请输入抽学号次数或输入q返回上一步：')
                if cxhgs.isdigit():
                    for i in range(int(cxhgs)):
                        r = random.randint(1,int(xsgs))
                        print(r)
                    continue
                elif cxhgs == 'q':
                    break
                else:
                    print('抽学号次数或输入q返回上一步输入错误，请重新输入')
    elif xsgs == 'q':
        break
    else:
        print('学生个数或输入q退出输入错误，请重新输入')
