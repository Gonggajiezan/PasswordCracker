from brute_force import brute_force_attack
from dictionary_attack import dictionary_attack
from rainbow_attack import rainbow_attack
from bruteforce_option import Option
import os

attack_mode = input("Attack mode(bf, dic, rainbow):")
# wordlist = input("File name: ")
result = False
wordlist = "dictonary10k.txt"
if attack_mode == "dic":
    pass_hash = input("Enter md5 hash: ")

    result = dictionary_attack(wordlist, pass_hash)
elif attack_mode == "bf":
    pass_hash = input("Enter md5 hash: ")
    options = [Option.num, Option.letter,Option.spec_char, Option.num_letter, Option.num_spec_char, Option.letter_spec_char, Option.num_letter_spec_char]
    i = input("Enter charset \n num = 0  letter = 1 spec_char = 2 \n num_letter = 3 num_spec_char = 4 letter_spec_char = 5 \n num_letter_spec_char = 6\n :")
    result = brute_force_attack(pass_hash, options[int(i)],0, wordlist)
else:
    os.system(r"rcrack C:\Users\69563\Documents\rainbowcrack-1.7-win64\rt -l .\md5\Rttestcase.txt")
    quit()
    

print (result)
if result != False:
    print("Password found")
    print("Password is "+ result)
else:
    print("Password is not found in the dictionary.")


