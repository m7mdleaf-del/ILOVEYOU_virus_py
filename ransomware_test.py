# the orighnal goal is  to learn so im gonna wrrite it all my own with the help of
#  ai to only and only teach me and make me learn better not to Cntl C+V
import os
from cryptography.fernet import Fernet 
key = Fernet.generate_key() # create a key 
# Change directory to your test folder
os.chdir(r"C:\Users\M\Desktop\testtty") #! the folder for testing 

fernet = Fernet(key)

# item=os.path.isfile(".")
All = os.listdir()
print(type(All))
# print (All,type(All))
for item in All:
    full_path = os.path.join(os.getcwd(), item)
    # if item.endswith(".jpg"):
    #     print ("its photo ")
    if os.path.isfile(full_path) and item.endswith(".jpg") :
        print (f" {item} >> photo file")
    elif os.path.isfile(full_path):
        print (f"{item} >> file ")
    else:
        print (f"{item} >> folder ")

    if os.path.isfile(full_path) and item.endswith(".jpg"):
        with open(full_path,'rb') as f:
            data=f.read()
            print (f"size of {item} and {data} bytes ")

    # Run this ONCE before the loop
        with open("the_secret_key.txt", "wb") as f:
             f.write(key)
             print("[KEY] Saved to disk!")

        # Inside your loop for each .jpg file:
        with open(full_path, 'rb') as f:
            data = f.read() # 1. Read

        encrypted_data = fernet.encrypt(data) # 2. Encrypt

        with open(full_path, 'wb') as f:
            f.write(encrypted_data) # 3. Write (Overwrite original)

        if input() == "yes " and item.endswith(".jpg") :
                with open("the_secret_key.txt",'rb') as f:
                    data=f.read(key)
                    print ("read the coded data  ")

                with open(full_path, 'wb') as f:#? whats the full path wantrs here 
                    dncrypted_data = fernet.decrypt(key)
                    f.write(encrypted_data) # 3. Write (Overwrite original)