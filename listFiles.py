import os

print("The files and folderes in {} are:" .format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)

    