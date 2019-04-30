import fileio 


def add_money(customer_code,money):
    list_c = fileio.read()

        for i in range(1,len(list_c)):
            customer = list_c[i].split(",")
            if customer[0] == customer_code:
                amount = float(customer[3]) + money
                customer[3] = str(amount)
                list_c[i] = ",".join(customer)

    fileio.write(list_c)     
            
                   

        
            