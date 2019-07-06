import hashlib

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    encypt_word = word.encode('utf-8')
    digest = hashlib.md5(encypt_word.strip()).hexdigest()

    if digest == pass_hash:
        print("Password found")
        print("Password is "+ word)
        flag = 1
        break

if flag == 0:
    print("Password is not in the list")