import os
libs = {"numpy","pollow","requests"}
try:
    for lib in libs:
        os.system("pip3 install "+lib)
    print("Successful")
except:
    print("Failed somehow")
