# -*- coding: utf-8 -*-
# coding: utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123123',
    db = 'test')
cur = conn.cursor()
def prc_line(line):
 _result = line.decode("utf-8").strip().split(" ")
 _result[2] = int(_result[2])
 return _result
with open("/home/lizhaoxuan/study/department.txt","r") as f:
    datas = [prc_line(line) for line in f.readlines()]
for d in datas:
    cur.execute("insert into department(dept_name,building_budget) values('%s','%s','%d')"%(d[0],d[1],d[2]))
cur.close()


def prc_line_student(line):
    _result = line.decode("utf-8").strip().split(" ")
    _result[0] = int(_result[0])
    _result[3] = int(_result[3])
    return _result


def prc_line_dept(line):
    _result = line.decode("utf-8").strip().split(" ")
    _result[2] = int(_result[2])
    return _result


def prc_line_exam(line):
    _result = line.decode("utf-8").strip().split(" ")
    _result[0] = int(_result[0])
    _result[2] = int(_result[2])
    return _result


with open("/home/lizhaoxuan/study/department.txt", "r") as f:
    datas = [prc_line_dept(line) for line in f.readlines()]
for d in datas:
    cur.execute("insert into department(dept_name,building,budget) values('%s','%s',%d)" % (d[0], d[1], d[2]))
    conn.commit()

with open("/home/lizhaoxuan/study/student.txt", "r") as f:
    datas = [prc_line_student(line) for line in f.readlines()]
for d in datas:
    cur.execute("insert into student(name,sex,age,emotion_state,dept_name) values('%s','%s',%d,'%s',%s)" % (
    d[1], d[2], d[3], d[4], "'" + d[5] + "'"))
    conn.commit()

with open("/home/lizhaoxuan/study/exam.txt", "r") as f:
    datas = [prc_line_exam(line) for line in f.readlines()]
for d in datas:
    cur.execute("insert into exam(student_ID,exam_name,grade) values('%d','%s',%d)" % (d[0], d[1], d[2]))
    conn.commit()

cur.close()
conn.close()