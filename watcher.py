import os
i=0
files = os.listdir(r"C:\Users\Saad\Pictures\Screenshots")
for file in files:
    if file.endswith(".png" ,".jpg" , ".jpeg"):
        print(file)
        i=i+1
print(f"Total number of screenshots {i}")


