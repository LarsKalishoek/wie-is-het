cheese = input('Is de kaas geel?    Ja/Nee  : ')
cheese = cheese.lower()

#linker pad voor wie is het
if cheese == "ja":
    cheese1 = input('Zitten er gaten in?   Ja/Nee  : ')
    cheese1 = cheese1.lower()
    if cheese1 == 'nee':
        cheese2 = input('Is de kaas zo hard steen?  Ja/Nee  :')
        cheese2 = cheese2.lower()
        if cheese2 == 'ja':
            antwoord = print('Uw antwoord is Parmigiano Reggiano!')
        if cheese2 == 'nee':
            antwoord = print('Uw antwoord is Goudse Kaas! ')
         
    if cheese1 == 'ja':
        cheese2 = input('Is de kaas belachelijk duur?  Ja/Nee  :')
        cheese2 = cheese2.lower()
        if cheese2 == 'nee':
            antwoord1 = input('Uw antwoord is Leerdammer!')
        if cheese2 == 'ja':
            antwoord = print('Uw antwoord is Emmenthaler!')
            
            
           
#rechter pad voor wie is het
cheese = cheese.lower()
if cheese == 'nee':
        cheese1 = input('Heeft de kaas blauwe schimmel?  Ja/Nee  :')
        cheese1 = cheese1.lower()
        if cheese1 == 'nee':
            cheese2 = input('Heeft de kaas een korst?  Ja/Nee  :')
            cheese2 == cheese2.lower()
            if cheese2 == 'nee':
                antwoord = print('Uw antwoord is Mozzerella')
            if cheese2 == 'ja':
                antwoord = print('Uw antwoord is Camembert!')
        if cheese1 == 'ja':
            cheese2 = input('Heeft de kaas een korst?  Ja/Nee  :')
            cheese2 = cheese2.lower()
            if cheese2 == 'ja':
                antwoord = print('Uw antwoord is Bleu de Rochbaron!')
            if cheese2 == 'nee':
                antwoord1 = print('Uw antwoord is Foume d Ambert')