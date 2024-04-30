import string
# Name :- George Hatem  ID :- 19104121
main=string.ascii_lowercase
def encryption_key_generation(key):
    # initializing all and generating key_matrix
    main=string.ascii_lowercase.replace('j','.')
    # convert all alphabets to lower
    key=key.lower()
    
    key_matrix=['' for i in range(5)]
    # if we have spaces in key, those are ignored automatically
    i=0;j=0
    for c in key:
        if c in main:
            # putting into matrix
            key_matrix[i]+=c

            main=main.replace(c,'.')

            j+=1
            if(j>4):
                i+=1
                j=0

    for c in main:
        if c!='.':
            key_matrix[i]+=c

            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)
def decryption_key_generation(key):
    main=string.ascii_lowercase.replace('j','.')
    key=key.lower()
    key_matrix=['' for i in range(5)]
    i=0;j=0
    for c in key:
        if c in main:
            key_matrix[i]+=c


            main=main.replace(c,'.')
            j+=1
            if(j>4):
                i+=1
                j=0


    for c in main:
        if c!='.':
            key_matrix[i]+=c

            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)
print("Hello, my name is George Hatem.")
print("Welcome to my Encryption and Decryption System.")
print("Please follow the steps below:")
key=input("Please Enter the key: ")
encrypted_key_matrix=encryption_key_generation(key)
decrypted_key_matrix=decryption_key_generation(key)
def vigenerConversion(plain_text,key):
    index=0
    cipher_text=""
    plain_text=plain_text.lower()
    key=key.lower()
    

    for c in plain_text:
        if c in main:
            off=ord(key[index])-ord('a')
            encrypt_num=(ord(c)-ord('a')+off)%26
            encrypt=chr(encrypt_num+ord('a'))
            cipher_text+=encrypt
            index=(index+1)%len(key)
        else:
            cipher_text+=c

    print("plain text: ",plain_text)
    print("cipher text: ",cipher_text)
def callVigenereConversion():
    plain_text=input("Enter the message: ")
    vigenerConversion(plain_text,key)
def vigener_De_Conversion(cipher_text,key):
    index=0
    plain_text=""

    cipher_text=cipher_text.lower()
    key=key.lower()
    
    for c in cipher_text:
        if c in main:
            off=ord(key[index])-ord('a')
            positive_off=26-off
            decrypt=chr((ord(c)-ord('a')+positive_off)%26+ord('a'))
            plain_text+=decrypt
            index=(index+1)%len(key)
        else:
            plain_text+=c

    print("cipher text: ",cipher_text)
    print("plain text (message): ",plain_text)
def callVigener_De_Conversion():
   cipher_text=input("Enter the message to be decrypted: ")
   vigener_De_Conversion(cipher_text,key)
def playFairConversion(plain_text):

    plain_text_pairs=[]
    cipher_text_pairs=[]
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.lower()


    i=0
    while i<len(plain_text):
        # i=0,1,2,3
        a=plain_text[i]
        b=''

        if((i+1)==len(plain_text)):
            b='x'
        else:
            b=plain_text[i+1]

        if(a!=b):
            plain_text_pairs.append(a+b)
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            i+=1
            
    print("plain text pairs: ",plain_text_pairs)


    for pair in plain_text_pairs:

        flag=False
        for row in encrypted_key_matrix:
            if(pair[0] in row and pair[1] in row):

                j0=row.find(pair[0])
                j1=row.find(pair[1])
                cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

                
        for j in range(5):
            col="".join([encrypted_key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=encrypted_key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        cipher_text_pair=encrypted_key_matrix[i0][j1]+encrypted_key_matrix[i1][j0]
        cipher_text_pairs.append(cipher_text_pair)
        
    print("cipher text pairs: ",cipher_text_pairs)
    # final statements
    print('plain text: ',plain_text)
    print('cipher text: ',"".join(cipher_text_pairs))
def callPlayFairEncryption():
    # calling first function
    print("Key Matrix for encryption:")
    print(encrypted_key_matrix)
    plain_text=input("Enter the message: ")

    playFairConversion(plain_text)
def playFairDeConversion(cipher_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]

    cipiher_text=cipher_text.lower()

    i=0
    while i<len(cipher_text):
        # i=0,1,2,3
        a=cipher_text[i]
        b=cipher_text[i+1]

        cipher_text_pairs.append(a+b)
        i+=2
            
    print("cipher text pairs: ",cipher_text_pairs)


    for pair in cipher_text_pairs:
        flag=False
        for row in decrypted_key_matrix:
            if(pair[0] in row and pair[1] in row):
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                plain_text_pair=row[(j0+4)%5]+row[(j1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue

        for j in range(5):
            col="".join([decrypted_key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                plain_text_pair=col[(i0+4)%5]+col[(i1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=decrypted_key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        plain_text_pair=decrypted_key_matrix[i0][j1]+decrypted_key_matrix[i1][j0]
        plain_text_pairs.append(plain_text_pair)
        
    print("plain text pairs: ",plain_text_pairs)
    
    print('cipher text: ',"".join(cipher_text_pairs))
    print('plain text (message): ',"".join(plain_text_pairs))
def callPlayFairDecryption():

    print("Key Matrix for encryption:")
    print(decrypted_key_matrix)
    cipher_text=input("Enter the encrypted message: ")

    playFairDeConversion(cipher_text)
print("Please choose an operation:")
print("1. Encryption")
print("2. Decryption")

operation_choice = input("Enter the operation number (1 or 2): ")

if operation_choice == "1":
    print("Choose an encryption method:")
    print("1. Vigenere")
    print("2. Playfair")

    encryption_method = input("Enter the encryption method number (1 or 2): ")

    if encryption_method == "1":
        # Vigenere Encryption
        callVigenereConversion()

    elif encryption_method == "2":
        # Playfair Encryption
        callPlayFairEncryption()

    else:
        print("Invalid input. Please enter a valid number.")

elif operation_choice == "2":
    print("Choose a decryption method:")
    print("1. Vigenere")
    print("2. Playfair")

    decryption_method = input("Enter the decryption method number (1 or 2): ")

    if decryption_method == "1":
        # Vigenere Decryption
        callVigener_De_Conversion()

    elif decryption_method == "2":
        # Playfair Decryption
        callPlayFairDecryption()

    else:
        print("Invalid input. Please enter a valid number.")

else:
    print("Invalid input. Please enter a valid number.")
