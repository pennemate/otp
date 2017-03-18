import sys, random, string, binascii,os.path

def read(name):
    if os.path.isfile(name):
        with open(name, 'r') as r:
            return r.read().strip()
    else:
        print "Somethihng is seriously wrong."
        sys.exit(1)
def write(name, text):
    with open(name, 'w') as w:
        w.write(text)
def keygen(keylen):
    return ''.join([random.SystemRandom().choice(string.ascii_letters)
         for k in range(keylen)])
def encrypt(m,k):
    c= xor(m,k)
    return (binascii.hexlify(c.encode())).decode()
def decrypt(c,k):
    c=(binascii.unhexlify(c.encode())).decode()
    return xor(c,k)
def xor(x,y):
    return ''.join([chr(ord(a)^ord(b)) for a,b in zip(x,y)])
def menu():
    print("\tThe (O)ne (T)ime (P)ad:\n"+
          "\tSelect an option from the menu: \n"+
          "\t1. (E)ncrypt \n" +
          "\t2. (D)ecrypt \n" +
          "\t3. (Q)uit\n" )
def main():
    menu()
    ans=raw_input("Choice:\n")
    while not(ans =='q' or ans== 'Q'):
        if (ans=='E' or ans=='e'):
            ptfile=raw_input("Please enter the name of your plaintext file\n")
            msg=read(ptfile)
            key=keygen(len(msg))
            write("key.txt", key)
            cipher=encrypt(msg,key)
            write("cipher.txt",cipher)
            print("Your message has been encrypted in :'cipher.txt' with the "
                +"corresponding key: 'key.txt'\n")
        elif (ans=='D' or ans=='d'):
            key=raw_input("Please enter the name of your key file\n") 
            cipher=raw_input("Please enter the name of your ciphertext file\n")
            write("decrypted.txt", decrypt(read(cipher), read(key)))
            print("Your message has been decrypted in: 'decrypted.txt'")
        
        else:
            print("Error- that option does not exist. Please choose again\n")
        menu()
        ans=raw_input("Choice\n")
    print("Thank you for using the OTP\n")
         
if __name__=="__main__":
    main()
    
