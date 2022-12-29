import pyfiglet
d = '\033[1;34m'
ascii_banner = pyfiglet.figlet_format("number system conversion", width=90)
print(ascii_banner)
print( ''' \033[34m
    +-----------------------------------------------+
    | [+]         Sufyan Hussein | CS          [+]  |
    | [+]     https://github.com/SufyanCS      [+]  |  
    | [+]   https://buymeacoffee.com/SufyanCS  [+]  |
    | [+]         Insta: @Suf.2002             [+]  |
    +-----------------------------------------------+
''')

def BinToDecF(BinToDec):
    BinToDecList = [] #empty list [1,1,0,0,1]
    for i in BinToDec: 
        BinToDecList.append(i)
    BinToDecList.reverse() 
    power = 0
    Binary_Base = 2
    BinToDec_Exp = [] 
    SumBinary = []
    BinToDecList = list(map(int, BinToDecList))
    for i in BinToDecList:
        if i <= 1: # Only 0 | 1 numbers
            SumBinary.append((Binary_Base**power)*i) #mathmatic equasion
            BinToDec_Exp.extend(["( (",Binary_Base,"**",power," ) * ",i," ) " ,"+ " ]) #Expletion
            power +=1 #rase the power up after each cycle
        else: # Break the condition if number out of range (0,1)
            break
    global FinalResualt_BinToDec
    FinalResualt_BinToDec = sum(SumBinary) #sum all entegers in list
    
    if FinalResualt_BinToDec != 0:
        print ("Resualt after converting the binary to decimal => ",FinalResualt_BinToDec)

    elif FinalResualt_BinToDec == 0:
        print ("Enter only 0 | 1 Numbers!") # تعديل
    else:
        print ("Enter only 0 | 1 !")   
    
    if FinalResualt_BinToDec != 0 :
        BinToDec_Ex_Choise = int(input(("If you want to see the Explenation press 1: ")))
        if BinToDec_Ex_Choise == 1:
            BinToDec_Exp.pop()
            for i in BinToDec_Exp:
                print(i, end = "")
            print(" = ",FinalResualt_BinToDec) 
        elif BinToDec_Ex_Choise != 1:
            print ("Thanks for your time :)")

def DecTobinF(DecToBin):
    DecToBinList = list()
    DecToBin_Exp = []
    Binary_Base = 2
    while DecToBin >= 1: 
        DecToBin_Rem = DecToBin%2 #get remainder
        
        if DecToBin_Rem != 0:
            DecToBinList.append("1")
            DecToBin_Exp.extend([DecToBin , "/", Binary_Base ,"=",DecToBin/2,"Reminder 1 \n"])

        elif DecToBin_Rem==0:
            DecToBinList.append('0') 
            DecToBin_Exp.extend([DecToBin , "/", Binary_Base ,"=",DecToBin/2,"Reminder 0 \n"])
        
        
        DecToBin=DecToBin/2
        DecToBin=int(DecToBin) 
    DecToBinList.reverse() 
    FinalResualt_DecToBin = print('The Binary value is: ',''.join(map(str, DecToBinList))) #output value
    if FinalResualt_DecToBin != 0 :
        DecToBin_Ex_choise = int(input(("If you want to see the Explenation press 1: ")))
        if DecToBin_Ex_choise == 1:
            
            for i in DecToBin_Exp:
                print(i, end = "  ")

        elif DecToBin_Ex_choise != 1:
            print ("Thanks for your time :)")

def DecToOctF(DecToOct):
    DecToOctList = list()
    DecToOct_Exp = []
    Octal_Base = 8
    while DecToOct >= 1: 
        DecToOct_Rem = DecToOct%8 #get remainder
        if DecToOct_Rem != 0:
            DecToOctList.append(DecToOct_Rem)
            DecToOct_Exp.extend([DecToOct , "/", Octal_Base ,"=",DecToOct/8,"Reminder",DecToOct_Rem,"\n"])
        
        DecToOct=DecToOct/8
        DecToOct=int(DecToOct) 
    DecToOctList.reverse() #reverse the list
    FinalResault_DecToOct = print('The Octal value is: ',''.join(map(str, DecToOctList))) #output value
    if FinalResault_DecToOct != 0 :
        DecToOct_Ex_choise = int(input(("If you want to see the Explenation press 1: ")))
        if DecToOct_Ex_choise == 1:
            
            for i in DecToOct_Exp:
                print(i, end = " ")

        elif DecToOct_Ex_choise != 1:
            print ("Thanks for your time :)")

def DecToHexF(DecToHex):
    DecToHexList = list()
    DecToHex_Exp = []
    Hex_Base = 16
    while DecToHex >= 1: #convert to octal
        DecToHex_Rem = DecToHex%16 #get remainder
        
        if DecToHex_Rem != 0:

            DecToHexList.append(DecToHex_Rem)

            DecToHex_Exp.extend([DecToHex , "/", Hex_Base ,"=",DecToHex/16,"Reminder",DecToHex_Rem,"\n"])
        
        DecToHex=DecToHex/16
        DecToHex=int(DecToHex)
        for i, n in enumerate(DecToHexList):
            if n == 10:
                DecToHexList[i] = "A"
            elif n == 11:
                DecToHexList[i] = "B"
            elif n == 12:
                DecToHexList[i] = "C"
            elif n == 13:
                DecToHexList[i] = "D"
            elif n == 14:
                DecToHexList[i] = "E"
            elif n == 11:
                DecToHexList[i] = "F"

    DecToHexList.reverse() #reverse the list
    FinalResault_HexToDec = print('The HexaDecimal value is: ',''.join(map(str, DecToHexList))) #output value
    if FinalResault_HexToDec != 0 :
        DecToHex_Ex_choise = int(input(("If you want to see the Explenation press 1: ")))
        if DecToHex_Ex_choise == 1:
            
            for i in DecToHex_Exp:
                print(i, end = " ")

        elif DecToHex_Ex_choise != 1:
            print ("Thanks for your time :)")

def OctToDecF(OctToDec):
    
    OctToDecList = [] #empty list
    for i in OctToDec: #To move data from user input user input To reversed list
        OctToDecList.append(i)
    OctToDecList.reverse() #List reversed
    power = 0 #First power
    Octal_Base = 8 #Base of System
    OctToDec_Exp = [] # only for Exeption
    OctToDec_Sum = []
    OctToDecList = list(map(int, OctToDecList)) # convert Element in list From strings To Integers
    for i in OctToDecList:
        if i <= 7: # Only From 0 To 7 numbers
            OctToDec_Sum.append((Octal_Base**power)*i) #mathmatic equasion
            OctToDec_Exp.extend(["( ( ",Octal_Base,"**",power," ) * ",i," ) + " ]) #Expletion
            power +=1 #rase the power up after each cycle

        else: 
            break
    global FinalResualt_OctToDec
    FinalResualt_OctToDec = sum(OctToDec_Sum) #sum all entegers in list


    if FinalResualt_OctToDec != 0:
        print ("Resualt after converting the Octal to decimal => ",FinalResualt_OctToDec)


    else:
        print ("Numbers accepted only From 0 To 7")   
    if FinalResualt_OctToDec != 0 :
        OctToDec_Ex_choise = int(input(("If you want to see the Explenation press 1: ")))
        if OctToDec_Ex_choise == 1:
            OctToDec_Exp.pop()
            for i in OctToDec_Exp:
                print(i, end = "")
            print(" = ",FinalResualt_OctToDec) 
        elif OctToDec_Ex_choise != 1:
            print ("Thanks for your time :)")

def HexToDecF(HexToDec):
    
    HexToDexList = [] #empty list
    for i in HexToDec: #To move data from user input user input To reversed list
        if i == "A":
            i = 10
        elif i == "B":
            i = 11
        elif i == "C":
            i = 12
        elif i == "D":
            i = 13
        elif i == "E":
            i = 14
        elif i == "F":
            i = 15
        
        HexToDexList.append(i)
    HexToDexList.reverse() #List reversed
    power = 0 #First power
    HexaDecimal_Base = 16 #Base of System
    HexToDec_Exp = [] # only for Exeption
    SumHex = []
    HexToDexList = list(map(int, HexToDexList)) # convert Element in list From strings To Integers
    for i in HexToDexList:
        if i <= 15: # Only 0 | 1 numbers
            SumHex.append((HexaDecimal_Base**power)*i) #mathmatic equasion
            HexToDec_Exp.extend(["( (",HexaDecimal_Base,"**",power," ) * ",i," ) " ,"+ " ]) #Expletion
            power +=1 #rase the power up after each cycle

        else: # Break the condition if number out of range (0,1)
            break
    global FinalResualt_HexToDec
    FinalResualt_HexToDec = sum(SumHex) #sum all entegers in list

    if FinalResualt_HexToDec != 0:
        print ("Resualt after converting the Hexadecimal to decimal => ",FinalResualt_HexToDec)


    else:
        print ("only Numbers From  0 To 9 AND From A To F accepted!")   
    if FinalResualt_HexToDec != 0 :
        HexToDec_Ex_Choise = int(input(("If you want to see the Explenation press 1: ")))
        if HexToDec_Ex_Choise == 1:
            HexToDec_Exp.pop()
            for i in HexToDec_Exp:
                print(i, end = "")
            print(" = ",FinalResualt_HexToDec) 
        elif HexToDec_Ex_Choise != 1:
            print ("Thanks for your time :)")

i = 1
while i == 1 :
    
    choise =  (input("\n\n=> 01- From Binary to Decimal\n=> 02- From Binary to Octal\n=> 03- From Binary To Hexadecimal\n-----------------------------------\n=> 04- From Decimal to Binary\n=> 05- From Decimal to Octal\n=> 06- From Decimal To HexaDecimal\n-----------------------------------\n=> 07- From Octal to Binary\n=> 08- From Octal to Decimal\n=> 09- From Octal To HexDecimal\n-----------------------------------\n=> 10- From HexaDecimal to Binary\n=> 11- From HexaDecimal to Decimal\n=> 12- From HexaDeimal To Octal\n=> 00 -Exit\n=> Choose Number of Operation 0-12 : "))

    if choise == "1" or choise == "01":
        try:
            BinToDec = (list(input("Enter Binary Number: ")))
            BinToDecF(BinToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "2" or choise == "02":
        BinToOct = (list(input("Enter Binary Number: ")))
        try:
            BinToDecF(BinToOct)
            DecToOctF(FinalResualt_BinToDec)
        except ValueError:
                print('Invalid input. Please try again.')    

    elif choise == "3" or choise == "03":
        BinToDec = (list(input("Enter Binary Number: "))) 
        try:
            BinToDecF(BinToDec)
            DecToHexF(FinalResualt_BinToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "4" or choise == "04":
        try:
            DecToBin = int(input("Enter Decimal Number: "))
            DecTobinF(DecToBin)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "5" or choise == "05":
        try:
            DecToOct = int(input("Enter Decimal Number: "))
            DecToOctF(DecToOct)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "6" or choise == "06":
        try:
            DecToHex = int(input("Enter Decimal Number: "))
            DecToHexF(DecToHex)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "7" or choise == "7":
        try:
            OctToBin = (list(input("Enter Octal Number: "))) 
            OctToDecF(OctToBin)
            DecTobinF(FinalResualt_OctToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "8" or choise == "08":
        try:
            OctToDec = (list(input("Enter Octal Number: "))) 
            OctToDecF(OctToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "9" or choise == "09":
        try:
            OctToHex = (list(input("Enter Octal Number: ")))
            OctToDecF(OctToHex)
            DecToHexF(FinalResualt_OctToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "10":
        try:
            HexToBin = (list(input("Enter HexaDecimal Number: ").strip().upper()))  
            HexToDecF(HexToBin)
            DecTobinF(FinalResualt_HexToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "11":
        try:
            HexToDec = (list(input("Enter HexaDecimal Number: ").strip().upper())) 
            HexToDecF(HexToDec)
        except ValueError:
                print('Invalid input. Please try again.')

    elif choise == "12":
        try:
            HexToOct = (list(input("Enter HexaDecimal Number: ").strip().upper())) 
            HexToDecF(HexToOct)
            DecToOctF(FinalResualt_HexToDec)
        except ValueError:
                print('Invalid input. Please try again.')    
    elif choise == "0" or choise == "00":
        i +=1
    else:
        print("Wronge Choise! ")