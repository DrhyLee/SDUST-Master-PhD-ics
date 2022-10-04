import time
from uuid import uuid4

def ics(classTable,classNum,stuNum):
  # if os.path.exists("i"+"1707020110"+".ics"):
  #   os.remove("i"+"1707020110"+".ics")
  newfile="it"+stuNum+".ics"#文件名：学号.ics 需要换成传入的参数：本人学号
  b_new_file=open(newfile,'w')
  t_n=b_new_file.write("BEGIN:VCALENDAR\n"+
        "METHOD:PUBLISH\n"+
        "VERSION:2.0\n"+
        "COMMENT:本软件服务由中国石油大学（华东）李恒源提供，代码编写人员：李恒源，杨国铭，田继林，本代码半开源，使用本软件造成的法律后果由使用者承担。需要代码请联系李恒源：870575989@qq.com\n"
        "X-WR-CALNAME:课程\n"+
        "PRODID:-//Apple Inc.//Mac OS X 10.15.3//EN\n"+
        "X-APPLE-CALENDAR-COLOR:#1D9BF6\n"+
        "X-WR-TIMEZONE:Asia/Shanghai\n"+
        "CALSCALE:GREGORIAN\n"+
        "BEGIN:VTIMEZONE\n"+
        "TZID:Asia/Shanghai\n"+
        "BEGIN:STANDARD\n"+
        "TZOFFSETFROM:+0900\n"+
        "RRULE:FREQ=YEARLY;UNTIL=19910914T170000Z;BYMONTH=9;BYDAY=3SU\n"+
        "DTSTART:19890917T020000\n"+
        "TZNAME:GMT+8\n"+
        "TZOFFSETTO:+0800\n"+
        "END:STANDARD\n"+
        "BEGIN:DAYLIGHT\n"+
        "TZOFFSETFROM:+0800\n"+
        "DTSTART:19910414T020000\n"+
        "TZNAME:GMT+8\n"+
        "RDATE:19910414T020000\n"+
        "END:DAYLIGHT\n"+
        "END:VTIMEZONE\n")#ics固定格式
  for each in range(classNum) :#每个EVENT的实现（写ics文件）
    uuid = short_uuid()
    t_n=b_new_file.write("BEGIN:VEVENT\n")
    t_n=b_new_file.write("CREATED:"+time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())+"\n")
    t_n=b_new_file.write("UID:"+stuNum+"-"+uuid+"&Drhylee.github.io\n")#(更新)学号仅做实验用途
    t_n=b_new_file.write("DTEND;TZID=Asia/Shanghai:"+classTable[each][3]+"T"+classTable[each][5]+"\n")
    t_n=b_new_file.write("TRANSP:OPAQUE\n")
    t_n=b_new_file.write("X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC\n")
    t_n=b_new_file.write("SUMMARY:"+classTable[each][0]+"@"+classTable[each][2]+"\n")
    t_n=b_new_file.write("LOCATION:"+classTable[each][1]+"\n")
    t_n=b_new_file.write("LAST-MODIFIED:"+time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())+"\n")
    t_n=b_new_file.write("DTSTAMP:"+time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())+"\n")
    t_n=b_new_file.write("DTSTART;TZID=Asia/Shanghai:"+classTable[each][3]+"T"+classTable[each][4]+"\n")
    t_n=b_new_file.write("SEQUENCE:0\n")
    t_n=b_new_file.write("BEGIN:VALARM\n")
    t_n=b_new_file.write("X-WR-ALARMUID:"+stuNum+"-"+uuid+"&hylee.xyz\n")
    t_n=b_new_file.write("UID:"+stuNum+"-"+uuid+"&hylee.xyz\n")
    t_n=b_new_file.write("TRIGGER:-PT15M\n")
    t_n=b_new_file.write("ACKNOWLEDGED:20220928T100000Z\n")
    t_n=b_new_file.write("ATTACH;VALUE=URI:Chord\n")
    t_n=b_new_file.write("ACTION:AUDIO\n")
    t_n=b_new_file.write("END:VALARM\n")
    t_n=b_new_file.write("END:VEVENT\n")
  t_n=b_new_file.write("END:VCALENDAR\n")
  b_new_file.close()

def short_uuid():
    uuidChars = ("a", "b", "c", "d", "e", "f",
               "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
               "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
               "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
               "W", "X", "Y", "Z")
    uuid = str(uuid4()).replace('-', '')
    result = ''
    for i in range(0,8):
        sub = uuid[i * 4: i * 4 + 4]
        x = int(sub,16)
        result += uuidChars[x % 0x3E]
    return result

def prt(classTable):#这是一个测试函数，用来测试classTable的数据结构
  for each in classTable:
    print(each)