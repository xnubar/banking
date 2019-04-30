import fileio 


def add_money(customer_code,money):
    list_c = fileio.read("customers.csv")

    for i in range(1,len(list_c)):
        customer = list_c[i].split(",")
        if customer[0] == customer_code:
            amount = float(customer[3]) + money
            customer[3] = str(amount)
            list_c[i] = ",".join(customer)

    fileio.write("customers.csv",list_c)

def withdraw(customer_code,money):
    list_b=fileio.read("customers.csv")

    for i in range(1,len(list_b)):
        customer = list_b[i].split(",")
        if customer[0] == customer_code:
            if float(customer[3])>=money:
                amount = float(customer[3]) - money
                customer[3] = str(amount)
                list_b[i] = ",".join(customer)
    
    fileio.write("customers.csv",list_b)


            
                   
withdraw('1234',50)

        
            
def check_balance(customer_code):    
    with open('customers.csv', 'r') as f:
        customers = f.readlines()   
        customers.pop(0) 

        for i in customers:
            customer = i.split(',')
            if customer_code == customer[0]:
                return customer[3]

