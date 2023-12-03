import hashlib
import getpass 

password_manager = {}

def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter you password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password 
    print("Account Created")
    
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successfully")
    else:
        print("Invalid username or password")
        
def main():
    while True:
        choice = input("Enter 1 to create, 2 to login, 0 to exit: ")    
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid Choice")
main()
if __name__ == "__main__":
    main()