import os
import time
os.system("pip install -r requirements.txt")
print()


print("Packages have been installed successfully.")

choice = input("Do you want to launch the menu now? (y/n) : ")

if choice == 'y':
    print("Launching the menu...")
    os.system("python Butcher.py")
elif choice == 'n':
    print("See you soon...")
    time.sleep(1)
    exit()
else:
    exit()

