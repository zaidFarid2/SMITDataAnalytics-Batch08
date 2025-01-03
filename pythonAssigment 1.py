# bank account system 
## Below is the info abuot account holder
def account_holder(name):
    account = { 
        "name" :name,
        "balance" : 0,
        "transection" :[] 
    }
    return account

##  This definition define  a deposite procedure
def deposit (ammount,account):
    try:
        if ammount < 0:
            print("Invalid amount! must be in positive")
        else:
            print(f"deposited ! before deposit balance is : {account['balance']}")
            account['balance'] += ammount
            account['transection'].append(f"Type : deposit ; deposit ammount {ammount} ;new balance => {account['balance']}")
            with open("transection.txt" , 'a+') as transection_details :
                transection_details.write(f"Type : deposit ; deposit ammount {ammount} ;new balance => {account['balance']} \n")
            return account
    except ValueError as valueError:
        print(valueError)
    except Exception as Error:
        print(f"unknown error occures :{Error}")
    
##  This definition define  a withdraw procedure
def withdraw(ammount,account):
    try:
        if ammount > account['balance']:
            print(f"insufficent balance")
            return account
        print(f"withdrawal ! before withdraw balance is : {account['balance']}")
        if account['balance'] > 0 :
            account['balance'] -= ammount
            account['transection'].append(f"Type : withdraw ; withdraw ammount {ammount} ; new balance => {account['balance']}")

        with open("transection.txt" , 'a+') as transection_details :
            transection_details.write(f"Type : withdraw ; deposit ammount {ammount} ;new balance => {account['balance']} \n")
        
        return account
    except ValueError as valueError:
        print(valueError)
    except Exception as Error:
        print(f"unknown error occures :{Error}")
    

## Here a definition to check balanace inquiry of account
def check_balance(account):
    try:
    
        print(f"your balance is : {account['balance']}")
    except Exception as Error: 
        print(f"unknown error occures :{Error}")

## this def about the whole details from name to how many transaction is bieng occured
def show_account_details(account):
    try:
        print(f"account holder name : {account['name']}")
        print(f"account balance : {account['balance']}")
        if not account['transection']:
            print("no transection occured!")
        else:
            with open("transection.txt","a+") as transection_details:
                transection_details.write(f"account holder name:{account['name']}")
            for transection in account['transection']:
                print(transection)
    except Exception as Error:
        print(f"unknown error occures :{Error}")

useraccount = account_holder("ZaidFarid")
check_balance(useraccount)
print("////////////////////////////")
withdraw(0,useraccount)
print("////////////////////////////")
show_account_details(useraccount)
print("////////////////////////////")
deposit(2000,useraccount)
print("////////////////////////////")
show_account_details(useraccount)
print("////////////////////////////")
withdraw(1525,useraccount)

show_account_details(useraccount)