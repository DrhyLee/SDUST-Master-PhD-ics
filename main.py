import datetime
import json
import random
import time
import configparser

import requests
import re

from ics import ics
from get_stu_info import get_stu_info

if __name__ == '__main__':
    sInfo = input(
        "由于嵙研究生登录验证过程过于麻烦，因此请按下列步骤登录。\n请在浏览器中登录研究生管理系统,进入学生课表查询\n复制链接中S括号内的内容，例如复制192.168.111.51/gmis/(S(kcbh1uqpkxng4xs4yibthexe))中的kcbh1uqpkxng4xs4yibthexe部分，并在下方输入\n输入完后按回车键继续。\n")
    cookie = input(
        "请继续按 F12 打开开发人员工具，然后在应用->存储->cookie->http://192.168.111.51中找到_SINDEXCOOKIE_ "
        "并将_SINDEXCOOKIE_的值粘贴在下面。\n输入完后按回车键继续。\n")
    stuNum = input("请输入您的学号信息\n")

    data = get_stu_info(sInfo,cookie)
    # wfsf4jqc3tswwgytrtq0ttih
    # cda2b13d557f6bb7158ed99655a344b9


    tableCount = 0
    dataTmpCount = 0
    classCount = 0

    for rank in range(0,10,2):
        for i in range(1,8):
            # if data[rank]['z' + str(i)]:
            #     data[rank]['z'+str(i)] = data[rank]['z'+str(i)]+'z'+str(i)#添加当日是周几的信息
            if data[rank]['z'+str(i)]:
                dataTmp = re.split("(?:['''<br/>'''\[\]])", data[rank]['z'+str(i)])
                # print(data[rank]['z' + str(i)])
                while '' in dataTmp:
                    dataTmp.remove('')
                dataTmpCount += len(dataTmp)
    tableStep1 = [[0 for i in range(7)] for j in range(dataTmpCount//4)]

    for rank in range(0,10,2):
        for i in range(1,8):
            if data[rank]['z'+str(i)]:
                dataTmp = re.split("(?:['''<br/>'''\[\]])", data[rank]['z'+str(i)])
                # print(data[rank]['z' + str(i)])
                while '' in dataTmp:
                    dataTmp.remove('')
                for insertCount in range(0,int(len(dataTmp))//4):
                    dataTmp.insert(5*insertCount+4,'z'+str(i))

                # print(dataTmp)

                for j in range(0,int(len(dataTmp))//4):
                    tableStep1[tableCount][0] = dataTmp[5 * j]
                    weekStartEnd = re.split("(?:[-周])" , dataTmp[5 * j + 1])
                    tableStep1[tableCount][1] = int(weekStartEnd[0])
                    tableStep1[tableCount][2] = int(weekStartEnd[1])
                    tableStep1[tableCount][3] = dataTmp[5 * j + 2]
                    tableStep1[tableCount][4] = dataTmp[5 * j + 3]
                    tableStep1[tableCount][5] = i
                    tableStep1[tableCount][6] = rank+1
                    tableCount += 1
                    classCount += int(weekStartEnd[1]) - int(weekStartEnd[0]) + 1

    #
    # for i in range(dataTmpCount//4):
    #     print(tableStep1[i])



    tableStep2 = [[0 for i in range(6)] for j in range(classCount)]
    i = 0
    initWeek = 34

    for cls in range(0,tableCount):
        for week in range(tableStep1[cls][1],tableStep1[cls][2]+1):
            tableStep2[i][0] = tableStep1[cls][0]
            tableStep2[i][1] = tableStep1[cls][4]
            tableStep2[i][2] = tableStep1[cls][3]
            time1 = '2022-' + str(initWeek+week) + '-' +str(tableStep1[cls][5])
            time2 = time.strptime(time1, '%Y-%U-%w')
            time3 = time.strftime("%Y%m%d",time2)
            tableStep2[i][3] = time3
            if tableStep1[cls][6] == 1:
                tableStep2[i][4] = '080000'
                tableStep2[i][5] = '095000'
            if tableStep1[cls][6] == 3:
                tableStep2[i][4] = '101000'
                tableStep2[i][5] = '120000'
            if tableStep1[cls][6] == 5:
                tableStep2[i][4] = '140000'
                tableStep2[i][5] = '155000'
            if tableStep1[cls][6] == 7:
                tableStep2[i][4] = '161000'
                tableStep2[i][5] = '180000'
            if tableStep1[cls][6] == 9:
                tableStep2[i][4] = '190000'
                tableStep2[i][5] = '205000'

            i += 1

    ics(tableStep2, classCount,stuNum)





    # classTable = [119][6]
    # classNum = 0
    # for week in range(10):
    #     for i in range(7):
    #         classTable[classNum][0] = data[week]['z'+i]


