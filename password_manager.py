from cryptography.fernet import Fernet

# function that generates encryption key,should be run only once
def write_key():
    key = Fernet.generate_key()
    with open("key1.key" , "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key1.key", "rb")
    key = file.read()
    file.close()
    return key

encyrption_password = "choose_your_key"
key = load_key() + encyrption_password.encode()
fer = Fernet(key)


# main loop
while True:
    user_input = input("Enter encryption password:\n")
    if user_input == encyrption_password:

        # function that adds new account and password to the file
        def add():
            acc_name = input("Enter account name:\n")
            acc_password = input("Enter the password:\n")

            with open('passwords.txt ', 'a') as file:
                file.write(acc_name + "|" + fer.encrypt(acc_password.encode()).decode() + "\n")

        # function to view the saved passwords
        def view():
            with open('passwords.txt ', 'r') as file:
                for each in file.readlines():
                    data = each.rstrip()
                    user,passw = data.split("|")
                    print("Username: " +user +" ,Password:" + fer.decrypt(passw.encode()).decode())

        user_name = input("What is your name: \n").upper()
        print("WElCOME ", user_name + "\n")

        while True:
            mode = input("what would you like to do today? View passwords or add a new password(view/add ||quit to quit)\n ").lower()

            if mode == "quit":
                break

            if mode == "add":
                add()
            elif mode == "view":
                view()
            else:
                print("INVALID OPTION,PLEASE ENTER OPTION AGAIN!!!")
                continue

        print("Thankyou for using the password manager,GOODBYE")
        break

    else:
        print("invalid password!!! Try again")
