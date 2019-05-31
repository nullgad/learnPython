import re


encoderTable={
    "a":"2, ",
    "b":"22, ",
    "c":"222, ",
    "d":"3, ",
    "e":"33, ",
    "f":"333, ",
    "g":"4, ",
    "h":"44, ",
    "i":"444, ",
    "j":"5, ",
    "k":"55, ",
    "l":"555, ",
    "m":"6, ",
    "n":"66, ",
    "o":"666, ",
    "p":"7, ",
    "q":"77, ",
    "r":"777, ",
    "s":"7777, ",
    "t":"8, ",
    "u":"88, ",
    "v":"888, ",
    "w":"9, ",
    "x":"99, ",
    "y":"999, ",
    "z":"9999, "

}

decoderTable={
    "2":"a",
    "22":"b",
    "222":"c",
    "3":"d",
    "33":"e",
    "333":"f",
    "4":"g",
    "44":"h",
    "444":"i",
    "5":"j",
    "55":"k",
    "555":"l",
    "6":"m",
    "66":"n",
    "666":"o",
    "7":"p",
    "77":"q",
    "777":"r",
    "7777":"s",
    "8":"t",
    "88":"u",
    "888":"v",
    "9":"w",
    "99":"x",
    "999":"y",
    "9999":"z"

}

##prompt


print("1: ENCODE \n")
print("2: DECODE \n")
    


#selection of option

e=input("Select a number : ")

if e is "1" :
    en=input("Input the text to encode : \n ")
        #lower or upper check 

    '''if en.islower() is False:
       ene=en.lower()
    else :
       ene = en'''
elif e is "2":
    #print("decoder is mot working yet")
    de=input("\nInput the code to decode : \n ")
else:
    print("\n\n++++++++++++++++++++++++++++++\nMake a Selection\n++++++++++++++++++++++++++++++")


#encode 

def encode(a):
    encd=""
    print("\n Your encoded string is ")
    for letter in a :
                
        #debud_print(letter)

        if letter in "aA"  :
             encd = encd + encoderTable.get("a")
        elif letter in "bB":
            encd = encd + encoderTable.get("b")
        elif letter in "cC":
            encd = encd + encoderTable.get("c")
        elif letter in "dD":
            encd = encd + encoderTable.get("d")
        elif letter in "eE":
            encd = encd + encoderTable.get("e")
        elif letter in "fF":
            encd = encd + encoderTable.get("f")
        elif letter in "GG":
            encd = encd + encoderTable.get("g")
        elif letter in "hH":
            encd = encd + encoderTable.get("h")
        elif letter in "iI":
            encd = encd + encoderTable.get("i")
        elif letter in "jJ":
            encd = encd + encoderTable.get("j")
        elif letter in "kK":
            encd = encd + encoderTable.get("k")
        elif letter in "lL":
            encd = encd + encoderTable.get("l")
        elif letter in "mM":
            encd = encd + encoderTable.get("m")
        elif letter in "nN":
            encd = encd + encoderTable.get("n")
        elif letter in "oO":
            encd = encd + encoderTable.get("o")
        elif letter in "pP":
            encd = encd + encoderTable.get("p")
        elif letter in "qQ":
            encd = encd + encoderTable.get("q")
        elif letter in "rR":
            encd = encd + encoderTable.get("r")
        elif letter in "sS":
            encd = encd + encoderTable.get("s")
        elif letter in "tT":
            encd = encd + encoderTable.get("t")
        elif letter in "uU":
            encd = encd + encoderTable.get("u")
        elif letter in "vV":
            encd = encd + encoderTable.get("v")
        elif letter in "wW":
            encd = encd + encoderTable.get("w")
        elif letter in "xX":
            encd = encd + encoderTable.get("x")
        elif letter in "yY":
            encd = encd + encoderTable.get("y")
        elif letter in "zZ":
            encd = encd + encoderTable.get("z")
        elif letter is " ":
            encd = encd + "0, "    
    return encd


#decoder function 

def decode(b):
    dec=""
    space=""
    print("\n Your decoded valu is : ")
    '''for letter in b:
        if letter is " ":
            space=space+""
        else:
            space=space + letter'''
    #print(space)
    #print(re.split(",",space))
    for index in re.split(",",de):
        index = "'"+index+"'"
        #print(index)
        if "' 2'" in index :
            dec=dec +  decoderTable.get("2")
        if  "'2'" in index :
            dec=dec +  decoderTable.get("2")
        elif "' 22'" in index :
            dec= dec + decoderTable.get("22")
        elif "' 222'" in index :
            dec= dec + decoderTable.get("222")
        elif "' 3'" in index :
            dec= dec + decoderTable.get("3")
        elif "' 33'" in index :
            dec= dec + decoderTable.get("33")             
        elif "' 333'" in index :
            dec= dec + decoderTable.get("333") 
        elif "' 4'" in index :
            dec= dec + decoderTable.get("4") 
        elif "' 44'" in index :
            dec= dec + decoderTable.get("44") 
        elif "' 444'" in index :
            dec= dec + decoderTable.get("444") 
        elif "' 5'" in index :
            dec= dec + decoderTable.get("5") 
        elif "' 55'" in index :
            dec= dec + decoderTable.get("55") 
        elif "' 555'" in index :
            dec= dec + decoderTable.get("555") 
        elif "' 6'" in index :
            dec= dec + decoderTable.get("6") 
        elif "' 66'" in index :
            dec= dec + decoderTable.get("66") 
        elif "' 666'" in index :
            dec= dec + decoderTable.get("666") 
        elif "' 7'" in index :
            dec= dec + decoderTable.get("7") 
        elif "' 77'" in index :
            dec= dec + decoderTable.get("77") 
        elif "' 777'" in index :
            dec= dec + decoderTable.get("777") 
        elif "' 7777'" in index :
            dec= dec + decoderTable.get("7777") 
        elif "' 8'" in index :
            dec= dec + decoderTable.get("8") 
        elif "' 88'" in index :
            dec= dec + decoderTable.get("88") 
        elif "' 888'" in index :
            dec= dec + decoderTable.get("888") 
        elif "' 9'" in index :
            dec= dec + decoderTable.get("9") 
        elif "' 99'" in index :
            dec= dec + decoderTable.get("99") 
        elif "' 999'" in index :
            dec= dec + decoderTable.get("999") 
        elif "' 9999'" in index :
            dec= dec + decoderTable.get("9999")     
        elif "' 0'" in index :
            dec= dec + " "
        else :
            dec = dec 
            for  character in dec:
                if character is " ":
                    space = space + ""
                else:
                    space = dec   
    return space


# input check for output


if e is "1" :
    print(encode(en))
elif e is "2" :
    print(decode(de))
