import random
while True:
    xsgs = input('请输入学生个数或输入q退出：')
    if xsgs.isdigit():
        while True:
                cxhgs = input('请输入抽学号次数或输入q返回上一步：')
                if cxhgs.isdigit():
                    list = []
                    while True:
                        if len(list) == int(cxhgs):
                            for i in range(int(cxhgs)):
                                print(list[i])
                            break
                        else:
                            r = random.randint(1,int(xsgs))
                            if r not in list:
                                list.append(r)
                elif cxhgs == 'q':
                    break
                else:
                    print('抽学号次数或输入q返回上一步输入错误，请重新输入')
    elif xsgs == 'q':
        break
    else:
        print('学生个数或输入q退出输入错误，请重新输入')
