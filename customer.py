import fileio 

def user_exists(customer_code):
    filename = "customers.csv"
    customers = fileio.read(filename)
    customer = ""
    for i in customers:
            customer = i.split(",")
            if customer[0] == customer_code:
                    return {customers.index(i):customer}
    return customer




def send_money(sender_code,receiver_code,amount):
    filename = "customers.csv"
    customers = fileio.read(filename)

    sender =  user_exists(sender_code)
    receiver =  user_exists(receiver_code)
   
    if  sender and  receiver:

        sender_customer = [sender[k] for k in sender][0]
        receiver_customer = [receiver[k] for k in receiver][0]

        sender_id = [k for k in sender.keys()][0]
        receiver_id = [k for k in receiver.keys()][0]
        
        sender_new_balance = float(sender_customer[3]) - amount
        receiver_new_balance = float(receiver_customer[3]) +amount
        if sender_new_balance >= 0:
                receiver_customer[3] = str(receiver_new_balance)
                sender_customer[3] = str(sender_new_balance) 
               
                customers[sender_id] = ",".join(sender_customer)
                customers[receiver_id] = ",".join(receiver_customer)
                fileio.write("customers.csv",customers)
                    
send_money('1234','1235',50)
        
def check_balance(customer_code):    
    with open('customers.csv', 'r') as f:
        customers = f.readlines()   
        customers.pop(0) 
        
        for i in customers:
            customer = i.split(',')
            if customer_code == customer[0]:
                return customer[3]



def add_money(customer_code,money):
    list_c = fileio.read()
    for i in range(1,len(list_c)):
        customer = list_c[i].split(",")
        if customer[0] == customer_code:
            amount = float(customer[3]) + money
            customer[3] = str(amount)
            list_c[i] = ",".join(customer)

    fileio.write(list_c)     
            
                   

        
            
