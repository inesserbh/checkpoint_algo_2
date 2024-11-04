 def analyser_phrase(phrase):
    longueur_phrase = 0
    nombre_mots = 0
    nombre_voyelles = 0
    voyelles = "aeiouyAEIOUY"
    
   
    dans_un_mot = False

    for caractere in phrase:
       
        longueur_phrase += 1

       
        if caractere in voyelles:
            nombre_voyelles += 1

       
        if caractere != ' ' and not dans_un_mot:
            dans_un_mot = True
            nombre_mots += 1
        elif caractere == ' ':
            dans_un_mot = False

        
        if caractere == '.':
            break

   
    print("Longueur de la phrase:", longueur_phrase - 1)  
    print("Nombre de mots:", nombre_mots)
    print("Nombre de voyelles:", nombre_voyelles)


phrase = "je suis ines."
analyser_phrase(phrase)
