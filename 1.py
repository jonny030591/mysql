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
            sql="SELECT * FROM user WHERE name =%s"
            n=(name,)
            mycursor.execute(sql,n)
            myresult = mycursor.fetchall()
            mydb.commit()
            if(name in str(myresult) and password in str(myresult)):
                print("登入成功")
            else:
                print("登入失敗")

        elif(x==2):
            name=input('使用者名稱：')
            sql="SELECT * FROM user WHERE name =%s"
            n=(name,)
            mycursor.execute(sql,n)
            myresult = mycursor.fetchall()
            if(name in str(myresult)):
                print("使用者名稱有人使用")
            else:
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
            name=input('輸入要刪除的使用者名稱：')
            passw=input('輸入root密碼：')
            if(passw==rootpass):
                if(name!=""):
                    sql="SELECT * FROM user WHERE name =%s"
                    n=(name,)
                    mycursor.execute(sql,n)
                    myresult = mycursor.fetchall()
                    if(name in str(myresult)):
                        sql="DELETE FROM user WHERE name =%s"
                        n=(name,)
                        mycursor.execute(sql,n)
                        mydb.commit()
                        print('使用者{%s}刪除成功'%(name))
                    else:
                        print('無此資料')
                else:
                        print('輸入發生錯誤')
            else:
                print('密碼錯誤，刪除失敗')
    except:
        print('錯誤')

    time.sleep(1)
    os.system('cls')


""" sql="SELECT * FROM user WHERE name =%s"
n=('jonny',)
mycursor.execute(sql,n)
myresult = mycursor.fetchall()
print('jonny' in str(myresult)) """

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


