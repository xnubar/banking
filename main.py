import customer
import inquirer

customer_code = '1234'
customer_profile = customer.user_exists(customer_code)

def menu_customer():
    OPTION_1 = "1: Balansini yoxla"
    OPTION_2 = "2: Balansina pul elave et"
    OPTION_3 = "3: Balansindan pul chek"
    OPTION_4 = "4: Diger mushterinin balansina pul yolla"
    OPTION_5 = "Q: Chix"
    questions = [
    inquirer.List('customer_menu',
                  message="Enter a choice",
                  choices=[OPTION_1,OPTION_2,OPTION_3,OPTION_4,OPTION_5]),
   
]
    while True:
        answers = inquirer.prompt(questions)
        if answers["customer_menu"] == OPTION_1:
            customer.check_balance(customer_code)
        elif answers["customer_menu"] == OPTION_2:
            amount = float(input("Meblegi daxil edin: "))
            customer.add_money(customer_code,amount)
        elif answers["customer_menu"] == OPTION_5:
            print(f"{customer_profile[1]} {customer_profile[2]} sagolun!")
            break


menu_customer()
    

