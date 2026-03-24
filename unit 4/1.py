import mysql.connector;

conn = mysql.connector.connect(
  user="root",
  
  port ="3306",
  database="mydb",
  password="",
  host="localhost"
)
print(conn)

cur = conn.cursor()


ch = None

while(ch!=9):
    print("1.insert ")
    print("2.update")
    print("3.delete")
    ch= int(input("Enter Choice : "))
    if(ch==1):
        insert ="insert into students(rollno,name) values(%s,%s)"
        rollno = int(input("Enter Roll no :"))
        name = input("Enter Name :")
        data = (rollno,name)
        cur.execute(insert,data)
        conn.commit();
        disp = "select * from students"
        cur.execute(disp)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        print(cur)
    elif ch==2:
        uprollno = int(input("Enter Roll no where to update :"))
        upname = input("Enter new Name :")
        updated_val = tuple([upname,uprollno]) 
        update = "update students set name =%s where rollno =%s"
        cur.execute(update,updated_val)
        conn.commit();
        disp = "select * from students"
        cur.execute(disp)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        print(cur)
    elif ch ==3:
        delrollno = int(input("Enter Rollno to delete :"))
        delete = "delete from students where rollno = %s"
        deldata = (delrollno)
        cur.execute(delete,deldata)
        conn.commit();
        disp = "select * from students"
        cur.execute(disp)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        print(cur)
    else:
        print("Enter valid Choice..!")
        


    
conn.close()