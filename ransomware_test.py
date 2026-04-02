# the orighnal goal is  to learn so im gonna wrrite it all my own 
import os
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

        with open(full_path,'wb') as f:
            data = b'JPG' + data[1:]  # made the pic not reachubel i dont know changed byts and shit 

            res=f.write(data)
            print(f"Locked {item}: {res} bytes written")
