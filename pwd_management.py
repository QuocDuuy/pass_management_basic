from cryptography.fernet import Fernet

def load_key():
    try:
        with open('key.key', 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print("Key file not found. Make sure to generate a key.")
        exit()

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def view():
    try:
        with open('password.txt', 'r') as file:
            for line in file.readlines():
                data = line.rstrip()
                user, passw = data.split('|')
                try:
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print("Username:", user + "\n" + "Password:", decrypted_pass)
                except Exception as e:
                    print(f"Error decrypting password for user {user}: {e}")
            else:
                print("File is empty! Please add more data for view")
    except FileNotFoundError:
        print("Password file not found. No entries to view.")



def add():
    user = input("Enter your username: ")
    pwd = input("Enter your password: ")

    with open('password.txt', 'a') as file:
        file.write(user + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        print("Done adding")

def remove():
    user_to_remove = input("Enter the username to remove: ")

    try:
        with open('password.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Password file not found. No entries to remove.")
        return

    with open('password.txt', 'w') as file:
        for line in lines:
            user, _ = line.split('|')
            if user != user_to_remove:
                file.write(line)

    print(f"User {user_to_remove} removed successfully.")

if __name__ == "__main__":
    write_key()  # Uncomment to generate and save a key

    master_pwd = input("Enter your password: ")
    key = load_key()
    fer = Fernet(key + master_pwd.encode())

    while True:
        mode = input("What do you want to do? \n1. Add \n2. View \n3. Remove \n4. Quit the program \n")
        if mode == "1":
            add()
        elif mode == "2":
            view()
        elif mode == "3":
            remove()
        elif mode == "4":
            print("Exited successfully")
            break
        else:
            print("Invalid mode. Please enter a valid option.")
