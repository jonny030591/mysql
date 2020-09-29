import mysql.connector
import os,time
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="username"
)
rootpass="123456"
mycursor = mydb.cursor()
while(1):
    x=0
    try:
        print('(1)登入  (2)註冊  (3)刪除')
        x=int(input('輸入要選擇的服務：'))
        if(x==1):
            name=input('使用者名稱：')
            password=input('密碼：')
            mycursor.execute("SELECT * FROM user")
            myresult = mycursor.fetchone()
            mydb.commit()
            if(myresult[1]==name and myresult[2]==password):
                print("登入成功")
            else:
                print("登入失敗")
        elif(x==2):
            name=input('使用者名稱：')
            password=input('密碼：')
            repassword=input('重複密碼：')
            if(password==repassword):
                sql = "INSERT INTO user (name,password) VALUES (%s,%s)"
                val = (name, password)
                mycursor.execute(sql, val)
                mydb.commit()
                print("註冊成功")
            else:
                print('註冊失敗')
        elif(x==3):
            s=input('輸入要刪除的使用者名稱：')
            passw=input('輸入root密碼：')
            if(passw==rootpass):
                if(s!=""):
                    sql = "DELETE FROM user WHERE name = %s"%(s)
                    mycursor.execute(sql)
                    mydb.commit()
                    print('使用者{%s}刪除成功'%(s))
                else:
                    print('輸入發生錯誤')
            else:
                print('刪除失敗')
        else:
            print('請重新輸入')
    except:
        print('請重新輸入')

    time.sleep(1)
    os.system('cls')


#登入模式
""" name=input('使用者名稱：')
    password=input('密碼：')
    sql = "INSERT INTO user (name,password) VALUES (%s,%s)"
    val = (name, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("登入成功") """
    
#刪除模式
""" sql = "DELETE FROM user WHERE name = 'jonny'"
mycursor.execute(sql)
mydb.commit() """

#註冊模式
""" name=input('使用者名稱：')
password=input('密碼：')
repassword=input('重複密碼：')
if(password==repassword):
    sql = "INSERT INTO user (name,password) VALUES (%s,%s)"
    val = (name, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("註冊成功")
else:
    print('註冊失敗') """


