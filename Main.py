choice = 0
message ="" # bass värden, så att programmet inte krashar.
delet = 0



while choice !=4:  #en loop som fortsätter sålänge man inte anger 3
    
    try: # gör så att man måste ha en siffra
        choice = int(input("Välkommen till loggboken. \n 1. Läs loggar \n 2. Skriv en logg. \n 3. För att rensa loggen. \n 4. Avsluta \n"))
    except: #loopar om ifall det inte är en siffra i inputen
        print("Använd siffra!")
        choice = 0 # återställer värdet till 0 varje gång det loopas
    if choice == 1: # när man trycker 1 kör den det här
        f = open('log.txt', 'r') #öppnar text fil med Read behörighet
        for line in f: #tar texten och gör något 
            print(line)#skriver ut texten
        print("")
        f.close() #stänger txt filen
        
    elif choice == 2: 
        message = input("Skriv ett meddelande: ")
        f = open('log.txt', 'a+')
        f.write("\n" + message) #skriver in meddelandet i filen
        f.close()# och stänger den sen.
    
    elif choice == 3:
        try:
            delet = int(input("Är du säker? Tryck 1 för att bekräfta. 0 för att avbryta \n"))# säkerhets fråga
        except:
            print("Använd siffra!")
            delet = 0
        if delet == 1:
            f = open ('log.txt', 'w')
            f.write("")
            f.close()
            print("Logg rensad")
        if delet == 0:
            print("Rensning avbruten.")