choice = 0
message =""




while choice !=3: 
    
    try:
        choice = int(input("Välkommen till loggboken. \n 1. Läs Loggar \n 2. Skriv en logg. \n 3. Avsluta \n"))
    except:
        print("Använd siffra!")
        choice = 0
    if choice == 1:
        print("")
        f = open('log.txt', 'r')
        for line in f:
            print(line)
        print("")
        f.close()
        
    elif choice == 2: 
        message = input("Skriv ett meddelande: ")
        f = open('log.txt', 'a+')
        f.write("\n" + message)
        f.close()
        
    
