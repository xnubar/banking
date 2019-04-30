def send_money(sender_code,receiver_code,amount):
    filename = "customers.csv"
    #with open(filename,"a") as f:
        
def check_balance(customer_code):    
        with open('customers.csv', 'r') as f:
            customers = f.readlines()   
            customers.pop(0) 
            
            for i in customers:
                customer = i.split(',')
                if customer_code == customer[0]:
                    return customer[3]

