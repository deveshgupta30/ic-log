# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 08:35:58 2018

@author: G Sriram
"""

import mysql.connector
def addStudent(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE IF NOT EXISTS devgup8_iclog")
  mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME VARCHAR(100), REG_NO VARCHAR(10) PRIMARY KEY, PH_NO VARCHAR(10), EMAIL VARCHAR(200))")
  mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT_LOGIN(REG_NO VARCHAR(10) PRIMARY KEY, EMAIL VARCHAR(200), PASSWORD VARCHAR(200) DEFAULT 'ASDFGF')" )
  sql="INSERT INTO STUDENTS(NAME, REG_NO, PH_NO, EMAIL) VALUES(%s, %s, %s, %s)"
  mycursor.execute(sql,a[:4])
  sql= "INSERT INTO STUDENT_LOGIN(REG_NO, EMAIL, PASSWORD) VALUES(%s, %s, %s)"
  mycursor.execute(sql, [a[1],a[3], a[4]])
  mydb.commit()

def addAdmin(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE IF NOT EXISTS devgup8_iclog")
  mycursor.execute("CREATE TABLE IF NOT EXISTS ADMIN(NAME VARCHAR(100), E_ID VARCHAR(10) PRIMARY KEY, EMAIL VARCHAR(200),PH_NO VARCHAR(10), lAB_NO VARCHAR(20))")
  mycursor.execute("CREATE TABLE IF NOT EXISTS ADMIN_LOGIN(E_ID VARCHAR(10) PRIMARY KEY, EMAIL VARCHAR(200), PASSWORD VARCHAR(200) DEFAULT 'ASDFGF')" )
  sql="INSERT INTO ADMIN(NAME, E_ID, EMAIL, PH_NO, LAB_NO) VALUES(%s, %s, %s, %s,%s)"
  mycursor.execute(sql,a[:5])
  sql= "INSERT INTO ADMIN_LOGIN(E_ID, EMAIL, PASSWORD) VALUES(%s, %s, %s)"
  mycursor.execute(sql, [a[1],a[2], a[5]])
  mydb.commit() 
  
def addComponent(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE IF NOT EXISTS devgup8_iclog")
  mycursor.execute("CREATE TABLE IF NOT EXISTS COMPONENTS(NAME VARCHAR(100), COMP_ID VARCHAR(100) PRIMARY KEY, STOCK INT, LAB_NO VARCHAR(200))")
  sql="INSERT INTO COMPONENTS(NAME, COMP_ID, STOCK, LAB_NO) VALUES(%s, %s, %s, %s)"
  mycursor.execute(sql,a)
  mydb.commit()  

def adminLogin(user, password):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT PASSWORD FROM ADMIN_LOGIN WHERE %s IN (E_ID, EMAIL)"
  mycursor.execute(sql, [user])
  result=mycursor.fetchall()
  if len(result)==0:
      return "Email/Employee ID not found!"
  for x in result:
     if(password in x):
         return True
     else:
         return False

def studentLogin(user, password):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT PASSWORD FROM STUDENT_LOGIN WHERE %s IN (REG_NO, EMAIL)"
  mycursor.execute(sql, [user])
  result=mycursor.fetchall()
  if len(result)==0:
      return "Email/USN not found, please ask your lab instructor to add your name!"
  for x in result:
     if(password in x):
         return True
     else:
         return False

def changePassword(email,password):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="UPDATE STUDENT_LOGIN SET PASSWORD = %s WHERE EMAIL=%s"
  mycursor.execute(sql,[password,email])
  mydb.commit()  
  
def changePasswordAdmin(email,password):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="UPDATE ADMIN_LOGIN SET PASSWORD = %s WHERE EMAIL=%s"
  mycursor.execute(sql,[password,email])
  mydb.commit()  

def fetchReg_No(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT REG_NO FROM STUDENT_LOGIN WHERE %s IN (REG_NO, EMAIL)"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]

def fetchStudentName(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql="SELECT NAME FROM STUDENTS WHERE %s = REG_NO"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]

def fetchCompID(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT COMP_ID FROM COMPONENTS WHERE %s = NAME"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]
  
def fetchE_ID(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT E_ID FROM ADMIN_LOGIN WHERE %s IN (E_ID, EMAIL)"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]

def fetchAdminName(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql="SELECT NAME FROM ADMIN WHERE %s = E_ID"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]
   
def searchCompDB(text):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT NAME FROM COMPONENTS WHERE NAME LIKE %s"
  a=[]
  mycursor.execute(sql,['%'+text+'%'])
  result=mycursor.fetchall()
  for x in result:
      a.append(str(x[0]))
  return a

def searchAdminDB(text):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT NAME FROM ADMIN WHERE NAME LIKE %s"
  a=[]
  mycursor.execute(sql,['%'+text+'%'])
  result=mycursor.fetchall()
  for x in result:
      a.append(str(x[0]))
  return a

def searchStudentDB(text):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT NAME FROM STUDENTS WHERE NAME LIKE %s"
  a=[]
  mycursor.execute(sql,['%'+text+'%'])
  result=mycursor.fetchall()
  for x in result:
      a.append(str(x[0]))
  return a

def getComponentStock(comp_id, lab_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT STOCK FROM COMPONENTS WHERE COMP_ID=%s AND LAB_NO=%s" 
  mycursor.execute(sql, [comp_id, lab_no])
  result=mycursor.fetchall()
  for x in result:
      return x[0]
  
def requestComponent(comp_id,reg_no, lab_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  mycursor.execute("CREATE TABLE IF NOT EXISTS REQ_LIST(REG_NO VARCHAR(10), COMP_ID VARCHAR(200), LAB_NO VARCHAR(100))")
  sql="INSERT INTO REQ_LIST(REG_NO, COMP_ID, LAB_NO) VALUES(%s, %s, %s)" 
  mycursor.execute(sql, [reg_no, comp_id, lab_no])
  mydb.commit()

def issueComponent(comp_id,reg_no, lab_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql1="DELETE FROM REQ_LIST WHERE COMP_ID = %s AND REG_NO = %s LIMIT 1"
  mycursor.execute(sql1,[comp_id, reg_no])
  mycursor.execute("CREATE TABLE IF NOT EXISTS BORROW_LIST(REG_NO VARCHAR(10), COMP_ID VARCHAR(200), LAB_NO VARCHAR(100))")
  sql="INSERT INTO BORROW_LIST(REG_NO, COMP_ID, LAB_NO) VALUES(%s, %s, %s)" 
  mycursor.execute(sql, [reg_no, comp_id, lab_no])
  sql2="UPDATE COMPONENTS SET STOCK=STOCK-1 WHERE COMP_ID=%s AND LAB_NO=%s"
  mycursor.execute(sql2, [comp_id,lab_no])
  mydb.commit()

def rejectComponent(comp_id,reg_no, lab_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql1="DELETE FROM REQ_LIST WHERE COMP_ID = %s AND REG_NO = %s LIMIT 1"
  
  mycursor.execute(sql1,[comp_id, reg_no])
  mydb.commit()
  
def returnComponent(comp_id,reg_no, lab_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql1="DELETE FROM BORROW_LIST WHERE COMP_ID = %s AND REG_NO = %s LIMIT 1"
  sql2="UPDATE COMPONENTS SET STOCK=STOCK+1 WHERE COMP_ID=%s AND LAB_NO=%s"
  mycursor.execute(sql1,[comp_id, reg_no])
  mycursor.execute(sql2,[comp_id, lab_no])
  mydb.commit()
  

def fetchComponentDetails(a):
    mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
    mycursor = mydb.cursor()
    sql="SELECT COMP_ID ,NAME, STOCK, LAB_NO FROM COMPONENTS WHERE COMP_ID=%s"
    mycursor.execute(sql, [a])
    result=mycursor.fetchall()    
    for x in result:
        return x

def fetchStudentDetails(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT REG_NO,NAME, PH_NO, EMAIL FROM STUDENTS WHERE %s = REG_NO"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x

def fetchAdminDetails(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  sql="SELECT E_ID, NAME, EMAIL, PH_NO, LAB_NO FROM ADMIN WHERE %s = E_ID"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x
   
def getRequestedComponentsLab(reg_no,lab_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  a=[]
  mycursor = mydb.cursor()    
  sql="SELECT COMP_ID FROM REQ_LIST WHERE REG_NO=%s AND LAB_NO=%s"
  mycursor.execute(sql,[reg_no, lab_no])
  result=mycursor.fetchall()    
  for x in result:
      sql="SELECT NAME FROM COMPONENTS WHERE COMP_ID=%s"
      mycursor.execute(sql, x)
      result1=mycursor.fetchall()
      for y in result1:
          a.append(y[0])
  return a

def getRequestedComponents(reg_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  a=[]
  mycursor = mydb.cursor()    
  sql="SELECT COMP_ID FROM REQ_LIST WHERE REG_NO=%s"
  mycursor.execute(sql,[reg_no])
  result=mycursor.fetchall()    
  for x in result:
      sql="SELECT NAME FROM COMPONENTS WHERE COMP_ID=%s"
      mycursor.execute(sql, x)
      result1=mycursor.fetchall()
      for y in result1:
          a.append(y[0])
  return a

def getBorrowedComponents(reg_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  a=[]
  mycursor = mydb.cursor()    
  sql="SELECT COMP_ID FROM BORROW_LIST WHERE REG_NO=%s"
  mycursor.execute(sql,[reg_no])
  result=mycursor.fetchall()    
  for x in result:
      sql="SELECT NAME FROM COMPONENTS WHERE COMP_ID=%s"
      mycursor.execute(sql, x)
      result1=mycursor.fetchall()
      for y in result1:
          a.append(y[0])
  return a
    
def modifyAdmin(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="UPDATE ADMIN SET NAME=%s, EMAIL=%s, PH_NO=%s, LAB_NO=%s WHERE E_ID=%s"
  mycursor.execute(sql,a)
  sql=sql="UPDATE ADMIN_LOGIN SET EMAIL=%s WHERE E_ID=%s"
  mycursor.execute(sql, [a[1], a[4]])
  mydb.commit()
  
def modifyStudent(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="UPDATE STUDENTS SET NAME=%s, PH_NO=%s, EMAIL=%s WHERE REG_NO=%s"
  mycursor.execute(sql,a)
  sql=sql="UPDATE STUDENT_LOGIN SET EMAIL=%s WHERE REG_NO=%s"
  mycursor.execute(sql, [a[2], a[3]])
  mydb.commit()
    
def modifyComponent(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )  
  mycursor = mydb.cursor()
  sql="UPDATE COMPONENTS SET NAME=%s, STOCK=%s,LAB_NO=%s WHERE COMP_ID=%s"
  mycursor.execute(sql,a)
  mydb.commit()  
  
def fetchAdminE_ID(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql="SELECT E_ID FROM ADMIN WHERE NAME = %s"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]    
  
def fetchStudentReg(a):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()
  sql="SELECT REG_NO FROM STUDENTS WHERE NAME = %s"
  mycursor.execute(sql, [a])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]  
  
def delAdmin(a):
     
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="DELETE FROM ADMIN WHERE E_ID=%s"
  mycursor.execute(sql,[a])
  sql=sql="DELETE FROM ADMIN_LOGIN WHERE E_ID=%s"
  mycursor.execute(sql, [a])
  mydb.commit()   
  
def delStudent(a):
     
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="DELETE FROM STUDENTS WHERE REG_NO=%s"
  mycursor.execute(sql,[a])
  sql=sql="DELETE FROM STUDENT_LOGIN WHERE REG_NO=%s"
  mycursor.execute(sql, [a])
  mydb.commit()   
  
def delComp(a):
     
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="DELETE FROM COMPONENTS WHERE COMP_ID=%s"
  mycursor.execute(sql,[a])
  mydb.commit() 

def getReqStudentList(lab):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT DISTINCT REG_NO FROM REQ_LIST WHERE LAB_NO = %s"
  a=[]
  mycursor.execute(sql,[lab])
  result=mycursor.fetchall()
  for x in result:
      sql="SELECT NAME FROM STUDENTS WHERE REG_NO=%s"
      mycursor.execute(sql, [x[0]])
      result1=mycursor.fetchall()
      for y in result1:
          a.append(str(y[0]))
  return a

def getAdminLabNumber(E_id):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  mycursor = mydb.cursor()
  
  sql="SELECT LAB_NO FROM ADMIN WHERE E_ID = %s"
  
  mycursor.execute(sql,[E_id])
  result=mycursor.fetchall()    
  for x in result:
      return x[0]
  
def getBorrowStudentList(lab):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT DISTINCT REG_NO FROM BORROW_LIST WHERE LAB_NO = %s"
  a=[]
  mycursor.execute(sql,[lab])
  result=mycursor.fetchall()
  for x in result:
      sql="SELECT NAME FROM STUDENTS WHERE REG_NO=%s"
      mycursor.execute(sql, [x[0]])
      result1=mycursor.fetchall()
      for y in result1:
          a.append(str(y[0]))
  return a   
    
def getComponentsinLab(lab):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT DISTINCT COMP_ID FROM COMPONENTS WHERE LAB_NO = %s"
  a=[]
  mycursor.execute(sql,[lab])
  result=mycursor.fetchall()
  for x in result:
      a.append(x[0])
  return a    

def getNoRequested(labNo):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT COUNT(REG_NO) FROM REQ_LIST WHERE LAB_NO = %s"
  mycursor.execute(sql,[labNo])
  result=mycursor.fetchall()
  for x in result:
      return x[0]  
  
def getNoBorrowed(labNo):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT COUNT(REG_NO) FROM BORROW_LIST WHERE LAB_NO = %s"
  mycursor.execute(sql,[labNo])
  result=mycursor.fetchall()
  for x in result:
      return x[0]  

def getNoRequestedStud(reg_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT COUNT(REG_NO) FROM REQ_LIST WHERE REG_NO = %s"
  mycursor.execute(sql,[reg_no])
  result=mycursor.fetchall()
  for x in result:
      return x[0]  
  
def getNoBorrowedStud(reg_no):
  mydb = mysql.connector.connect(
    host="mysql.freehostia.com",
    user="devgup8_iclog",
    passwd="Hellohiy0!",
    database="devgup8_iclog"
  )
  
  mycursor = mydb.cursor()

  sql="SELECT COUNT(REG_NO) FROM BORROW_LIST WHERE REG_NO = %s"
  mycursor.execute(sql,[reg_no])
  result=mycursor.fetchall()
  for x in result:
      return x[0]
