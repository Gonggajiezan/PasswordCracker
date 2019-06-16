import time
import string

maxattempts = 100000000000000000000000000000
start       = time.time()
# chars       = list(string.printable)[:95]
# base        = len(chars)
n           = 0
solved      = False
password    = input("Enter your password:")

chars = ['0','1','2','3','4','5','6','7','8','9']
base        = len(chars)

print(chars)

# converts number N base 10 to a list of digits base b
def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


# check edge cases like empty, or 0
if password == '':
    print('Your password is empty')
    solved = True
    
elif password == chars[n]:
    print('Your password is ' + chars[n])
    solved = True
    
else:
    n = 1






# begin systematically checking passwords
if not solved:
    while n < maxattempts:
        lst = numberToBase(n, base)
        print(lst)
        word = ''
        for x in lst:
            word += str(chars[x])
        print(word)
        if password == word:
            solved = True
            print('-Stats-')
            print('Pass: ' + word)
            print('Attempts: ' + str(n))
            print('time: ' + str((time.time() - start)) + ' sec')
            break
        else:
            n += 1

# the password is beyond our maxattempts
if not solved:
    print('Unsolved after ' + str(n) + ' attempts!')