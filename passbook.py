import datetime
import mysql.connector
amount=50000

# MySQL connection
con = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="paymentt"

)

id=int(input("ENTER YOUR ID :")) 
name=input("Enter your name: ")
choice=int(input('''Enter your choice 
1 for withdraw
2 for deposite'''))


def withdraw():
    bank_withdraw=int(input("enter amount to withdraw:"))
    if bank_withdraw<= amount :
        final_amount=amount-bank_withdraw
        print(f"{final_amount} is your final amount")
        x=str(id)
        file=open(f"{x}.txt","w")
        now=datetime.datetime.now()
        file.write(f"date and time: {now}")
        file.write(f"\n customer id : {id}\n customer name : {name}\n withdraw_amount:{bank_withdraw}\n balance: {final_amount}")

    cursor = con.cursor()
    sql = "INSERT INTO passbook (id,customer_name, final_amount,deposite_amount,withdraw_amount) VALUES (%s, %s, %s, %s,%s)"
    values = (id,name,final_amount,None,bank_withdraw)
    cursor.execute(sql,values)
    con.commit()

    print("✅ Data successfully inserted into orders table!")
    cursor.close()
    con.close()    
    
def deposite():
    bank_deposite=int(input("enter amount to deposite: "))
    final_amount=bank_deposite+amount
    print(f"your final amount is {final_amount}")
    
    x=str(id)
    file=open(f"{x}.txt","w")
    now=datetime.datetime.now()
    file.write(f"date and time: {now}")
    file.write(f"\n customer id : {id}\n  customer name : {name}\ndeposite_amount:{bank_deposite}\n balance:{final_amount}")


    cursor = con.cursor()
    sql = "INSERT INTO passbook (id,customer_name, final_amount,deposite_amount,withdraw_amount) VALUES (%s, %s, %s, %s,%s)"
    values = (id,name,final_amount,bank_deposite,None)
    cursor.execute(sql,values)
    con.commit()

    print("✅ Data successfully inserted into orders table!")
    cursor.close()
    con.close()



if choice==1:
    withdraw()
   
elif choice==2:
    deposite()
else:    
    print("invalid choice")