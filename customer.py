def check_balance(customer_code):    
        with open('customers.csv', 'r') as f:
            customers = f.readlines()   
            customers.pop(0) 
            
            for i in customers:
                customer = i.split(',')
                if customer_code == customer[0]:
                    return customer[3]

