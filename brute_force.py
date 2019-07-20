from itertools import product
from bruteforce_option import Option
import string
import hashlib
from dictionary_attack import dictionary_attack
nums = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sepc_chars = '!@#$%^&*()-_+=~`[]{\}|\:;"\'<>,.?/'
num_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
num_spec_chars = '0123456789!@#$%^&*()-_+=~`[]{\}|\:;"\'<>,.?/'
letter_spec_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+=~`[]{\}|\:;"\'<>,.?/'
chars       = list(string.printable)[:95]
MAX = 11 # the max length of the target password
def search(charset,pass_hash):
    for i in range(MAX):
             
            for item in product(charset, repeat=i):
                #print (''.join(item))
                encypt_word = ''.join(item).encode('utf-8')
                digest = hashlib.md5(encypt_word.strip()).hexdigest()
                # print (encypt_word)
                if digest == pass_hash:
                    return ''.join(item)
    return False
def brute_force_attack(pass_hash, option, possible_len, word_list):
    result = dictionary_attack(word_list, pass_hash)
    if result != False:
        return result
    if option.value == 0:
        return search(nums,pass_hash)
    elif option.value == 1:
        return search(letters,pass_hash)
    elif option.value == 2:
        return search(sepc_chars,pass_hash)
    elif option.value == 3:
        return search(num_letters,pass_hash)
    elif option.value == 4:
        return search(num_spec_chars,pass_hash)
    elif option.value == 5:
        return search(letter_spec_chars,pass_hash)
    else:
        return search(chars,pass_hash)


# pass_hash = input("Enter md5 hash: ")
# result = brute_force_attack(pass_hash, Option.spec_char, 0)

# if result != False:
#     print("Password found")
#     print("Password is "+ result)
# else:
#     print("Password is not found in the dictionary.")


# for item in permutations(nums,2):
#     # encypt_word = ''.join(item).encode('utf-8')
#     # digest = hashlib.md5(encypt_word.strip()).hexdigest()
#     # print (encypt_word)
#     print(''.join(item))
#     if ''.join(item) == "0000000":
#         print("checker works")
#     if ''.join(item) == "2114803":    
#         print(''.join(item))