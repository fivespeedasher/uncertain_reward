#todo 帮助系统找txt文件
import random

def Read_text(filename):
    with open(filename+".txt","r",encoding="UTF-8") as file1:
        print(file1.read())

def Read_list(filename):
    with open(filename+".txt","r",encoding="UTF-8") as file1:
        list_row =file1.readlines()
        list_source = []
        for i in range(len(list_row)):
            column_list = list_row[i].strip().split("\n")  # 每一行split后是一个列表
            list_source.append(column_list)                # 在末尾追加到list_source
    file1.close()
    return list_source

def add_reward(filename,new_reward):    #追加一个新的奖励
    rewards_list.append(new_reward)
    with open(filename+".txt",'a',encoding="UTF-8") as file1:
        file1.write(new_reward)
    file1.close()

#

#Todo 实现删除奖励
# def list2txt(filename, list):#filename为写入CSV文件的路径，data为要写入数据列表.
#     file = open(filename+'.txt','w')
#     for i in range(len(list)):
#         print(i)
#         s = str(list[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
#         s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
#         file.write(s)
#     file.close()
#     print("保存文件成功")
# def delect_reward(d_reward):
#     d_reward = '[\''+d_reward+'\']'
#     print(d_reward)
#     if d_reward in rewards_list:
#         rewards_list.remove(d_reward)
#         list2txt('rewards', rewards_list)
#     else:print("Error:此项奖励不存在)

def Raffle(rewards_list):
    reward = random.choice(rewards_list)
    return reward[0]

if __name__ == '__main__':
    rewards_list = Read_list(r"D:\I'M\pycharm\uncertain_reward\rewards")
    while(1):
        Read_text(r"D:\I'M\pycharm\uncertain_reward\指示语")
        select = int(input())
        while select == 1 or 2 or 3:
            if select == 1:
                Read_text(r"D:\I'M\pycharm\uncertain_reward\rewards")
                break
            elif select ==2:
                print("请输入要添加的奖励：")
                new_reward = str(input())
                add_reward("rewards",new_reward)
                break
            elif select == 3:
                print("恭喜你，"+Raffle(rewards_list)+'\n')
                break
            else:print("Error:1")
        else:print("Error: 不存在这个选项")
# print(rewards_list)
# new_reward = str(input())
# add_reward("rewards",new_reward)
# rewards_list = Read_list("rewards")
# print(rewards_list)
