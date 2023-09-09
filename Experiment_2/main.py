def save_Logs(holder_Account, holder_Name, amount):
    transaction_Info.update({account_No: {0: {}}})
    id_Value = list((transaction_Info[account_No]).keys())[-1]
    id = id_Value + 1
    transaction_Info[account_No].update({
        account_No: {
            id: {
                'To': holder_Account + " " + "-" + " " + holder_Name,
                'From': account_No + " " + "-" + " " + user_Accounts_Info[account_No]['First Name'] + " " + user_Accounts_Info[account_No]['Last Name'],
                'Amount': amount,
            },
        },
    })


def user_Choice_Action():
    print('Choose Following Options:')
    print("1. Account Details")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transfer Money")
    print("5. Change Password")
    print("6. Delete Account")
    print("7. Transactions History")
    print("X. Quit")

    print("-------------------------------------------")
    user_Choice = input("Enter Choice -> ")

    return user_Choice


def create_User():
    first_Name = input("Add First Name -> ")
    last_Name = input("Add Last Name -> ")
    address = input("Add Address -> ")

    check_Contact_No = None
    while check_Contact_No is None:
        contact_No = input("Add Contact Number -> ")
        try:
            check_Contact_No = int(contact_No)
        except ValueError:
            print("-------------------------------------------")
            print("** Add Proper Phone Number **")
            print("-------------------------------------------")

    account_No = input("Add 2 Number for Account Number -> ")
    account_No = 'SPIT' + account_No
    password = input("Add Password -> ")

    deposit_Balance = None
    while deposit_Balance is None:
        deposit_Money = input("Add Deposit Money -> ")
        try:
            deposit_Balance = int(deposit_Money)
        except ValueError:
            print("-------------------------------------------")
            print("** Add Proper Amount **")
            print("-------------------------------------------")

    user_Accounts_Info.update({
        account_No: {
            "First Name": first_Name,
            "Last Name": last_Name,
            "Address": address,
            "Phone Number": contact_No,
            "Password": password,
            "Balance": deposit_Money,
        }
    })
    print("-------------------------------------------")
    print(f"{account_No} ({first_Name} {last_Name}) is Created")


# user_Accounts_Info = {'SPIT01': {'First Name': 'Aniket',
#                                  'Last Name': 'Dohale',
#                                  'Address': 'Badlapur',
#                                  'Phone Number': 8180003641,
#                                  'Password': 'Aniket@123',
#                                  'Balance': 5999},
#                       'SPIT02': {'First Name': 'Shubham',
#                                  'Last Name': 'Mhatre',
#                                  'Address': 'Taloja',
#                                  'Phone Number': 9696969696,
#                                  'Password': 'Shubham@123',
#                                  'Balance': 105000}}
user_Accounts_Info = {}

transaction_Info = {
    'SPIT01': {
        1: {
            'To': 'SPIT02 - Shubham Mhatre',
            'From': 'SPIT01 - Aniket Dohale',
            'Amount': 8000,
        },
        2: {
            'To': 'SPIT02 - Shubham Mhatre',
            'From': 'SPIT01 - Aniket Dohale',
            'Amount': 40
        },
        3: {
            'To': 'SPIT03 - Vaibhav Wagh',
            'From': 'SPIT01 - Aniket Dohale',
            'Amount': 40
        },
        4: {
            'To': 'SPIT04 - Praniket Tandel',
            'From': 'SPIT01 - Aniket Dohale',
            'Amount': 40
        },
    },
    'SPIT02': {
        1: {
            'To': 'SPIT02 - Aniket Dohale',
            'From': 'SPIT01 - Shubham Mhatre',
            'Amount': 81000,
        },
        2: {
            'To': 'SPIT01 - Aniket Dohale',
            'From': 'SPIT02 - Shubham Mhatre',
            'Amount': 2000
        },
    }
}

while True:
    print("-------------------------------------------")
    print("#### S.P.I.T Bank ####")
    print("-------------------------------------------")
    print("Choose Option Below:")
    print("1. Create User")
    print("2. Login to Account")
    print("X. Quit")
    print("-------------------------------------------")
    choice = input("Enter Choice -> ")
    print("-------------------------------------------")

    if choice == '1':
        create_User()

    elif choice == '2':
        account_No = input("Enter Account Number -> ")

        if account_No in user_Accounts_Info:
            password = input("Enter Password -> ")

            if password == user_Accounts_Info[account_No]['Password']:
                print("-------------------------------------------")
                print("Login Successfully.")
                print("-------------------------------------------")

                while True:
                    user_Choice = user_Choice_Action()

                    print("-------------------------------------------")

                    if user_Choice == '1':
                        print(f"Account Number: {account_No}")
                        print(
                            "Full Name:", user_Accounts_Info[account_No]['First Name'], user_Accounts_Info[account_No]['Last Name'])
                        print(
                            f"Address: {user_Accounts_Info[account_No]['Address']}")
                        print(
                            f"Phone Number: {user_Accounts_Info[account_No]['Phone Number']}")
                        print(
                            f"Balance: {user_Accounts_Info[account_No]['Balance']}")
                        print("-------------------------------------------")

                    elif user_Choice == '2':
                        withdraw_Amount = int(
                            input("Enter Amount to Withdraw -> "))

                        if withdraw_Amount > int(user_Accounts_Info[account_No]['Balance']):
                            print("-------------------------------------------")
                            print("Insufficient Balance")
                            print("-------------------------------------------")

                        else:
                            user_Accounts_Info[account_No]['Balance'] = int(
                                user_Accounts_Info[account_No]['Balance']) - withdraw_Amount
                            print("Successfully Withdraw Amount",
                                  withdraw_Amount)
                            print("-------------------------------------------")
                            print("Balance:",
                                  user_Accounts_Info[account_No]['Balance'])
                            print("-------------------------------------------")

                    elif user_Choice == '3':
                        deposit_Amount = int(
                            input("Enter Amount to Deposit -> "))
                        user_Accounts_Info[account_No]['Balance'] = int(
                            user_Accounts_Info[account_No]['Balance']) + deposit_Amount
                        print("Successfully Deposit Amount", deposit_Amount)
                        print("-------------------------------------------")
                        print("Balance:",
                              user_Accounts_Info[account_No]['Balance'])
                        print("-------------------------------------------")

                    elif user_Choice == '4':
                        print("Recipient Details:")
                        transfer_Account_Number = input(
                            "Enter Account Number -> ")

                        if transfer_Account_Number in user_Accounts_Info:
                            bank_Holder_Name = input(
                                "Bank Account Holder Name -> ")
                            transfer_Amount = int(input("Transfer Amount -> "))

                            if transfer_Amount > int(user_Accounts_Info[account_No]['Balance']):
                                print("-------------------------------------------")
                                print("Insufficent Balance")
                                print("-------------------------------------------")

                            else:
                                save_Logs(transfer_Account_Number,
                                          bank_Holder_Name, transfer_Amount)

                                user_Accounts_Info[account_No]['Balance'] = int(
                                    user_Accounts_Info[account_No]['Balance']) - transfer_Amount

                                user_Accounts_Info[transfer_Account_Number]['Balance'] = int(
                                    user_Accounts_Info[transfer_Account_Number]['Balance']) + transfer_Amount
                                print(f"{transfer_Amount} Amount Transferred")
                                print("-------------------------------------------")
                                print("Balance:",
                                      user_Accounts_Info[account_No]['Balance'])
                                print("-------------------------------------------")

                        else:
                            print("-------------------------------------------")
                            print("Account Not Found..")
                            print("-------------------------------------------")

                    elif user_Choice == '5':
                        previous_Password = input(
                            "Enter Previous Password -> ")

                        if previous_Password == user_Accounts_Info[account_No]['Password']:
                            new_Password = input("Enter New Password -> ")
                            retype_Password = input("Retype New Password -> ")

                            if new_Password == retype_Password:
                                user_Accounts_Info[account_No]['Password'] = new_Password
                                print("-------------------------------------------")
                                print("Password Changed Successfully")
                                print("-------------------------------------------")

                            else:
                                print("-------------------------------------------")
                                print("Password Not Matched.")
                                print("-------------------------------------------")

                        else:
                            print("-------------------------------------------")
                            print("Invalid Password")
                            print("-------------------------------------------")

                    elif user_Choice == '6':
                        surety = input("Are You Sure (Y/N): ")

                        if surety.capitalize() == 'Y' or surety.capitalize() == 'Yes':
                            user_Password = input("Enter Password -> ")

                            if user_Accounts_Info[account_No]['Password'] == user_Password:
                                del user_Accounts_Info[account_No]
                                print("-------------------------------------------")
                                print("Account Deleted")
                                break

                            else:
                                print("-------------------------------------------")
                                print("Wrong Password")
                                print("-------------------------------------------")

                        else:
                            print("-------------------------------------------")
                            print("Process Cancelled")
                            print("-------------------------------------------")

                    elif user_Choice == '7':
                        try:
                            for value in list(transaction_Info[account_No])[-3::1]:
                                print(transaction_Info[account_No][value])
                                print(
                                    "------------------------------------------------------------------------------------")
                        except KeyError:
                            print("No Transactions")
                            print("-------------------------------------------")

                    elif user_Choice == 'X':
                        break

                    else:
                        print("Invalid Input")
                        print("-------------------------------------------")

            else:
                print("-------------------------------------------")
                print("Invalid Password")

        else:
            print("-------------------------------------------")
            print("Account Not Found..")

    elif choice == 'X':
        print("Quitting..")
        break

    else:
        print("Invalid Input..")
