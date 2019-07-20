import hashlib
def dictionary_attack(wordlist, pass_hash):
    try:
        pass_file = open(wordlist, "r")
    except:
        print("No file found")
        quit()
    for word in pass_file:
        encypt_word = word.encode('utf-8')
        digest = hashlib.md5(encypt_word.strip()).hexdigest()

        if digest == pass_hash:
            return word
    
    pass_file.close()
    return False
