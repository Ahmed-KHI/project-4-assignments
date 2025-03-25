from hashlib import sha256

def login(email, stored_logins, password_to_check):

    stored_hash = stored_logins.get(email) 
    if stored_hash is None:
        print(f"❌ Email '{email}' not found!")
        return False
    
    if stored_hash == hash_password(password_to_check):
        print(f"✅ Login successful for {email}")
        return True
    else:
        print(f"❌ Incorrect password for {email}")
        return False

def hash_password(password):

    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }
    
    print(login("example@gmail.com", stored_logins, "word"))         # ❌ Incorrect password
    print(login("example@gmail.com", stored_logins, "password"))     # ✅ Login successful
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))   # ✅ Login successful
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   # ❌ Incorrect password
    
    print(login("student@stanford.edu", stored_logins, "password"))  # ❌ Incorrect password
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # ✅ Login successful
    
    print(login("unknown@domain.com", stored_logins, "password"))    # ❌ Email not found!

if __name__ == '__main__':
    main()