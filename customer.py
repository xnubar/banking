import fileio 

def user_exists(customer_code):
    filename = "customers.csv"
    customers = fileio.read(filename)
    customer = ""
    for i in customers:
            customer = i.split(",")
            if customer[0] == customer_code:
                    return customer
    return customer


      
def check_balance(customer_code):    
    with open('customers.csv', 'r') as f:
        customers = f.readlines()   
        customers.pop(0) 
        for i in customers:
            customer = i.split(',')
            if customer_code == customer[0]:
                print(f"{customer[1]} {customer[2]}, balansiniz  {customer[3].split()[0]}"," azn teshkil edir")



def add_money(customer_code,money):
    list_c = fileio.read("customers.csv")

    for i in range(1,len(list_c)):
        customer = list_c[i].split(",")
        if customer[0] == customer_code and money>0:
            amount = float(customer[3]) + money
            customer[3] = str(amount)
            list_c[i] = ",".join(customer)
            print(f"Balansiniza {money} azn elave olundu. Cari balansiniz: {amount} azn.")

    fileio.write("customers.csv",list_c)


def withdraw(customer_code,money):
    list_b=fileio.read("customers.csv")
    for i in range(1,len(list_b)):
        customer = list_b[i].split(",")
        if customer[0] == customer_code:
            print(customer_code)
            if float(customer[3])-money>=0:
                amount = float(customer[3]) - money
                customer[3] = str(amount)
                list_b[i] = ",".join(customer)
                print(f"Balansinizdan {money} azn chixildi. Cari balansiniz: {amount} azn.")

    
    fileio.write("customers.csv",list_b)


                

def send_money(sender_code,receiver_code,amount):
    filename = "customers.csv"
    customers = fileio.read(filename)

    sender =  user_exists(sender_code)
    receiver =  user_exists(receiver_code)
   
    if  sender and  receiver:
        sender_new_balance = float(sender[3]) - amount
        if sender_new_balance >= 0:
                add_money(receiver[0],amount)
                withdraw(receiver[0],amount)
