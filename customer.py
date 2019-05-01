import fileio 
import transaction



def user_exists(customer_code):
    filename = "customers.csv"
    customers = fileio.read(filename)
    for i in customers:
            customer = i.split(",")
            if customer[0] == customer_code:
                    return customer
    return None


      
def check_balance(customer_code):    
    with open('customers.csv', 'r') as f:
        customers = f.readlines()   
        customers.pop(0) 
        for i in customers:
            customer = i.split(',')
            if customer_code == customer[0]:
                print(f"{customer[1]} {customer[2]}, balansiniz  {customer[3].split()[0]}"," azn teshkil edir")





def add_money(customer_code,money,transaction_type):
    list_c = fileio.read("customers.csv")

    for i in range(1,len(list_c)):
        customer = list_c[i].split(",")
        if customer[0] == customer_code and money>0:
            amount = float(customer[3]) + money
            customer[3] = str(amount)
            list_c[i] = ",".join(customer)
            if transaction_type == transaction.ADD_MONEY:
                print(f"Balansiniza {money} azn elave olundu. Cari balansiniz: {amount} azn.")
            transaction_txt = f"\n{customer[0]},{transaction_type},{money}"
            transaction.add("transactions.csv",transaction_txt)
            fileio.write("customers.csv",list_c)
            break
        elif money < 0:
            print(f"{customer[1]} {customer[2]}, emeliyyatchun hesabinizda kifayet qeder pul yoxdur.")


def withdraw(customer_code,money,transaction_type):
    list_b=fileio.read("customers.csv")
    for i in range(1,len(list_b)):
        customer = list_b[i].split(",")
        if customer[0] == customer_code:
            if float(customer[3])-money>=0:
                amount = float(customer[3]) - money
                customer[3] = str(amount)
                list_b[i] = ",".join(customer)
                if transaction_type == transaction.WITHDRAW_MONEY:
                    print(f"Balansinizdan {money} azn chixildi. Cari balansiniz: {amount} azn.")
                transaction_txt = f"\n{customer[0]},{transaction_type},{money}"
                transaction.add("transactions.csv",transaction_txt)
                break
            else:
                print(f"{customer[1]} {customer[2]}, emeliyyatchun hesabinizda kifayet qeder pul yoxdur.")
                

    
    fileio.write("customers.csv",list_b)

def send_money(sender_code,receiver_code,amount):
    filename = "customers.csv"
    customers = fileio.read(filename)

    sender =  user_exists(sender_code)
    receiver =  user_exists(receiver_code)
    if  sender is not None and  receiver is not None:
        sender_new_balance = float(sender[3]) - amount
        if sender_new_balance >= 0 and sender_code != receiver_code:
                sender_transaction_txt = transaction.WITHDRAW_MONEY+"," + receiver[0]
                receiver_transaction_txt = transaction.ADD_MONEY + "," + sender[0]
                add_money(receiver[0],amount,receiver_transaction_txt)
                withdraw(sender[0],amount,sender_transaction_txt)
                print(f'{sender[1]} {sender[2]}, balansinizdan {amount} azn {receiver[1]} {receiver[2]} hesabina kochuruldu.')
        elif sender_new_balance<0:
            print(f'{sender[1]} {sender[2]}, balansinizda kifayet qeder vesait yoxdur')
            
    else:
            print("Pul gondereceyiniz mushteri kodu movcud deyil.")

