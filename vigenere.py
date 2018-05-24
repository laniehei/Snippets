import sys #imports the sys module

def main(): #starts the main function
    print(sys.argv) #shows the string of what was input
    en = sys.argv[1] #this assigns a variable to the value that specifies wherther we are encoding or decoding

    try:
        message1 = open(sys.argv[2],"r") #opens input file to be read
    except OSError: #if file doesn't exist, it produces an error
        print('File ' + sys.argv[2] + ' Does Not Exist') #prints error for user
        return
    msg = str(message1.read()) #reads message and converts it into a string
    message1.close() #closes message to free up space; we have what we wanted

    try:
        encode1 = open(sys.argv[3],"w") #opens file to write the output to
    except OSError:
        print('File ' + sys.argv[3] + ' Does Not Exist')
        return

    key = sys.argv[4] #this is our key to decode the message
    print(key)

    if len(sys.argv) != 5: #prints error if the number of arguments is not 5
        print('please enter 5 arguments to run code')
        return

    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:') #creates a list of strings of possible characters, since strings are immutable and so more difficult to work with

    if len(key) <= 3: #checks if the key's length is less than 3 (deliverable)
        print('please make your key at least 3 characters long')
        return

    table = sparse(characters,key) #calls sparse function to create sparse table

    if en == '-e': #encryption
        secretcode = encryptdecrypt(en,msg,characters,table)
        print('encoded: ' + secretcode) #deliverable
        encode = encode1.write(secretcode) #produces our output in the file specified
        encode1.close() #closes file
    elif en == '-d': #decryption
        actual = encryptdecrypt(en,msg,characters,table)
        print('decoded: ' + actual) #deliverable
        encode = encode1.write(actual) #produces our output in the file specified
        encode1.close() #closes file
    else:
        print('Please Choose Either -d (decrypt) Or -e (encrypt)') #if neither -d or -e is chosen
        return

def sparse(characters,key): #this function creates the sparse table
    i = 0 #counter of characters to 0
    x = 1 #counter of key spot to 1
    table = [] #creates empty table
    while x <= len(key): #journeys along the key
        if key[x-1] == characters[i]: #creates the string within the table function
            characters1 = characters[i:] #after the character
            characters2 = characters[:i] #before the character
            characters3 = characters1 + characters2 #combines the string
            table.append(''.join(characters3)) #puts our new string in the table at the end
            x += 1 #moves on the the next letter
            i = 0 #resets the counter
        else:
            i += 1 #moves to the next character if the current one is not equal to the key
    print(table) #deliverable -- sparse table
    return table

def encryptdecrypt(en,msg,characters,table): #this function encrypts or decrypts the specified string we've given it
    code = ''
    y = 0 #moves along our msg
    while y+1 <= len(msg):
        for x in range(len(table)): #chooses the correct instance of character string
            z = 0 #counter to zero
            if y+1 >= len(msg): #necessary in case the message is not a multiple of 3
                return code
            instance = table[x] #moves along the sparse table
            if en == '-d':
                while msg[y] != instance[z]: #checks if our message letter is equal to the letter in the augmented table
                    z += 1 #increments the augmented table
                else:
                    code += characters[z] #creates our decoded message!
                    y += 1
            elif en == '-e':
                while msg[y] != characters[z]: #checks if our message letter is equal to the letter in the character list
                    z += 1
                else:
                    code += instance[z] #creates our encoded message!
                    y += 1
    return code

if __name__ == '__main__': #checks if arguments are imported
    main()