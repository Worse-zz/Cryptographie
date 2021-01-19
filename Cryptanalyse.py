# --------------------------------------------------------------------------------------------
# ------------------------------------------- TP 1 -------------------------------------------
# ------------------------------------------ Crypto ------------------------------------------
# ------------------------------------- Etienne BAILLIEUL ------------------------------------
# --------------------------------------- Octobre 2020 ---------------------------------------
# --------------------------------------------------------------------------------------------

alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def del_accents(text):
    #à â ç è é ê î ô ù û et espace
    text = text.replace('à', 'a')
    text = text.replace('â', 'a')
    text = text.replace('ç', 'c')
    text = text.replace('è', 'e')
    text = text.replace('ê', 'e')
    text = text.replace('é', 'e')
    text = text.replace('î', 'i')
    text = text.replace('ô', 'o')
    text = text.replace('ù', 'u')
    text = text.replace('û', 'u')
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace("'", '')
    text = text.replace("’", '')
    text = text.replace('-', '')
    text = text.replace(' ', '')
    return text

def clean(text):
    return (del_accents(text.lower()))

def occurenceOfLetter(text, alphabet):
    nbocc = [];
    text = clean(text)
    for i in alphabet :
        nb = (text.count(i))
        nbocc.append(nb)
    return nbocc

def rateOfLetter(text, alphabet):
    listOfRate = []
    text = text.replace(' ', '') #Enlève les espaces pour ne compter que les lettres
    nblettre = len(text)
    nbocc = occurenceOfLetter(text, alphabet)
    for i in nbocc :      
        listOfRate.append(round((i/nblettre)*100,3))       
    return listOfRate
        
def openFile(filename):
    fichier = open(filename, "r", encoding='utf8')
    contenufichier = fichier.read()
    fichier.close()
    return contenufichier

def writeFile(filename, text):
    fichier = open(filename, "w", encoding='utf8')
    fichier.write(text)
    fichier.close

#--------------------------Chiffrement par décalage------------------------------

def charToCesar(char,key,alphabet):
    if char in alphabet :
        j = 0
        tailleAlphabet =  (len(alphabet))
        for i in alphabet:
            if i == char : #Recupère le numéro d'index correspondant à la lettre
                numlettresortie = j+key
                if numlettresortie >= tailleAlphabet:
                    numlettresortie = (numlettresortie-tailleAlphabet)
                lettresortie = alphabet[numlettresortie]
            j = j+1
    else: #Si caractère en entrée pas dans alphalist
        lettresortie = char
    return lettresortie

def cesarToChar(char,key,alphabet):
    if char in alphabet :
        j = 0
        tailleAlphabet = (len(alphabet))
        for i in alphabet:
            if i == char :
                numlettresortie = j-key
                if numlettresortie >= tailleAlphabet :
                    numlettresortie = (tailleAlphabet - numlettresortie)
                    if numlettresortie < 0 :
                        numlettresortie = 0 - numlettresortie
                lettresortie = alphabet[numlettresortie]
            j = j+1
    else: #Si caractère en entrée pas dans alphalist
        lettresortie = char
    return lettresortie

def textToCesar(text,key,alphabet):
    textChifree = ''
    text = clean(text)
    for i in text :
        charChiffre = cesarToChar(i,key,alphabet)
        textChifree =  textChifree + charChiffre
    return(textChifree)

def cesarToText(textchiffre,key,alphabet):
    text = ''
    for i in textchiffre :
        charDehiffre = charToCesar(i,key,alphabet)
        text =  text + charDehiffre
    return(text)

def fileToCesar(filename,key,alphabet):
    contenuFichier = openFile(filename)
    chainesansaccent = clean(contenuFichier)
    fichierChifre = textToCesar(chainesansaccent,key,alphabet)
    writeFile(filename.replace(".txt" , "_code.txt")  , fichierChifre)
    return(fichierChifre)

def cesarTofile(filename,key,alphabet): #Nomage du PDF
    contenuFichier = openFile(filename)
    fichierDechifre = cesarToText(contenuFichier,key,alphabet)
    writeFile(filename.replace("_code.txt" , "_decode.txt")  , fichierDechifre)
    return(fichierDechifre)

def cesarToFile(filename,key,alphabet): #Nomage Logique
    cesarTofile(filename,key,alphabet)

#--------------------------Chiffrement par décalage ... Le retour ! ------------------------------

def textToVig(text,key,alphabet):
    longueurcle = len(key)
    motChiffre = '';
    lettreChiffre = '';
    j = 0
    for i in text:
        lettreChiffre = (charToCesar(i,key[j],alphabet))
        motChiffre =  motChiffre + lettreChiffre 
        j=j+1
        if j >= longueurcle :
            j = 0
    return(motChiffre)

def vigToText(text,key,alphabet):
    longueurcle = len(key)
    motDechiffre = '';
    lettreDechiffre = '';
    j = 0
    for i in text:
        lettreDechiffre = (cesarToChar(i,key[j],alphabet))
        motDechiffre =  motDechiffre + lettreDechiffre 
        j=j+1
        if j >= longueurcle :
            j = 0
    return(motDechiffre)

def fileToVig(filename,key,alphabet):
    contenuFichier = openFile(filename)
    chainesansaccent = clean(contenuFichier)
    fichierChifre = textToVig(chainesansaccent,key,alphabet)
    writeFile(filename.replace(".txt" , "_code.txt")  , fichierChifre)
    return(fichierChifre)

def vigToFile(filename,key,alphabet):
    contenuFichier = openFile(filename)
    fichierDechifre = vigToText(contenuFichier,key,alphabet)
    writeFile(filename.replace("_code.txt" , "_decode.txt")  , fichierDechifre)
    return(fichierDechifre)

#---------------------------------- Cryptanalyse -----------------------------------

def attaque_brute_force_sa(text,alphabet):
    key = 1
    reponse = "N"
    while True:
        print("Clé " + str(key) + " - Texte : " + (cesarToText(text,key,alphabet)[0:40]))
        reponse = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour Stopper")
        print("----------------------------------------------------")
        reponse = reponse.lower()
        if reponse != "n" :
            break
        key = key +1

def e_attack(text,alphabet):
    rateLetter = (rateOfLetter(text, alphabet))
    numLettreMaxUtilise = 0
    valeurLettreMaxUtilise = 0
    j = 0
    for i in rateLetter :
        if i > valeurLettreMaxUtilise :
            numLettreMaxUtilise = j
            valeurLettreMaxUtilise = i
        j = j+1
    Ordre=[4,0,8,18] #Initialisation des positions de E,A,I,S
    while True:
        for k in Ordre :
            key = numLettreMaxUtilise - k
            print("Clé " + str(k) + " : " + (textToCesar(text,key,alphabet)[0:40]))
            reponse = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour Stopper")
            print("----------------------------------------------------")
            reponse = str(reponse.lower())
            if reponse != "n":
                break
        break

def indexC(text,alphabet):
    tabOccurence = occurenceOfLetter(text,alphabet)
    denominateur = sum(tabOccurence)
    numerateur = 0
    for nx in tabOccurence :
        numerateur = numerateur + (nx *(nx-1))
    denominateur = (denominateur * (denominateur-1))
    return(numerateur/denominateur)

def key_len(filename,tailleMax,alphabet) :
    contenu = openFile(filename)
    tableauIndice, tableauIndiceTrie = [], []
    for n in range(1, tailleMax+1):
        indiceDeCoincidence = 0.0
        indiceMoyenne = 0.0
        for i in range(n):
            partieTexte = ""
            for j in range(0,len(contenu[i:]),n):   
                partieTexte += contenu[i:][j]
            Indice = indexC(partieTexte,alphabet)
            indiceDeCoincidence += Indice #Ajoute tout les indices de coïncidence 
        tableauIndice.append(indiceDeCoincidence/n)
        tableauIndiceTrie = tableauIndice.copy()
    tableauIndiceTrie.sort(reverse=True) #Tri le tableau
    return(tableauIndice.index(tableauIndiceTrie[0])+1) #Recupère le numéro d'index correspondant au plus gros élément qui est en position 0 du tableau trié (+1 car index démarre à zéro)
 
def calculCle(text, alphabet):
    tabOccurence, tabOccurenceTrie = [], []
    tabOccurence = occurenceOfLetter(text,alphabet)
    tabOccurenceTrie = tabOccurence.copy()
    tabOccurenceTrie.sort(reverse=True) #Tri le tableau
    #print(tabOccurence.index(tabOccurenceTrie[0]))
    return(tabOccurence.index(tabOccurenceTrie[0])-4)

def decode(filename,tailleMax,alphabet) :
    longueurCle = key_len(filename,tailleMax,alphabet)
    contenu = openFile(filename)
    cle = []
    for i in range(longueurCle) : #Passe longuerCle fois (par exemple clé de 3 caractères recupères 1 caractères sur 3)
        TextePartiel="" 
        for j in range(i,len(contenu),longueurCle): #Demarre à i (0,1 ou 2) parcours le nombre de caractères du texte avec un pas de longueur de clé (3) donc prend les caractères 0,3,6,9 puis 1,4,7,10 puis 2,5,8,11 ...
            TextePartiel += contenu[j]
        cle.append(calculCle(TextePartiel,alphabet))
    print(cle)
    vigToFile(filename,cle,alphabet)

#-------------------------- Cryptanalyse - Doublement de lettre en fin de mot -------------------

def att_doublement(filename,alphabet):
    lettrepre = ""
    listelettresprobable = ""
    numLettreMaxUtilise = 0
    valeurLettreMaxUtilise = 0
    j=0
    doublelettre = False
    contenufichier = openFile(filename)
    for lettre in contenufichier:
        if doublelettre == True: #Si les deux lettres précédentes sont les mêmes alors ... et remet la variable à False
            listelettresprobable = listelettresprobable + lettre
            doublelettre = False  
        if lettrepre == lettre : #Si la lettre courrante et la même que la lettre précédente alors met la variable à True
            doublelettre = True  
        lettrepre = lettre #Mets la lettre actuelle dans la variable lettre précédente
    tablettresprobable = rateOfLetter(listelettresprobable,alphabet)
    for i in tablettresprobable :
        if i > valeurLettreMaxUtilise :
            numLettreMaxUtilise = j
            valeurLettreMaxUtilise = i
        j = j+1
    nomLettreMaxUtilisee = alphabet[numLettreMaxUtilise]
    key = numLettreMaxUtilise - 4
    print("Attaque par doublement de lettre : \nLa lettre qui à remplacé le E est la " + str(nomLettreMaxUtilisee.upper()) +  " avec " + str(valeurLettreMaxUtilise) + " % d'apparition \nLe fichier déchiffré donne donc : " +(textToCesar(contenufichier,key,alphabet)[0:80]))


# ------------------------------------------- Main -------------------------------------------

def main():
    texteRandom = "Les vidéos vous permettent de faire passer votre message de façon convaincante."
    texteRandomLong = "Les vidéos vous permettent de faire passer votre message de façon convaincante. Quand vous cliquez sur Vidéo en ligne, vous pouvez coller le code incorporé de la vidéo que vous souhaitez ajouter. Vous pouvez également taper un mot-clé pour rechercher en ligne la vidéo qui convient le mieux à votre document. Pour donner un aspect professionnel à votre document, Word offre des conceptions d’en-tête, de pied de page, de page de garde et de zone de texte qui se complètent mutuellement. Vous pouvez par exemple ajouter une page de garde, un en-tête et une barre latérale identiques.Cliquez sur Insérer et sélectionnez les éléments de votre choix dans les différentes galeries.Les thèmes et les styles vous permettent également de structurer votre document. Quand vous cliquez sur Conception et sélectionnez un nouveau thème, les images, graphiques et SmartArt sont modifiés pour correspondre au nouveau thème choisi. Quand vous appliquez des styles, les titres changent pour refléter le nouveau thème. Gagnez du temps dans Word grâce aux nouveaux boutons qui s'affichent quand vous en avez besoin.Si vous souhaitez modifier la façon dont une image s’ajuste à votre document, cliquez sur celle-ci pour qu’un bouton d’options de disposition apparaisse en regard de celle-ci. Quand vous travaillez sur un tableau, cliquez à l’emplacement où vous souhaitez ajouter une ligne ou une colonne, puis cliquez sur le signe plus. La lecture est également simplifiée grâce au nouveau mode Lecture. Vous pouvez réduire certaines parties du document et vous concentrer sur le texte désiré. Si vous devez stopper la lecture avant d’atteindre la fin de votre document, Word garde en mémoire l’endroit où vous avez arrêté la lecture, même sur un autre appareil."
    cleVig = [0,1,7,2,3]
    #Cration fichier2, fichier3.txt
    writeFile("fichier2.txt", texteRandom)
    writeFile("fichier3.txt", texteRandomLong)
    #Fin création fichiers
    print("\n --------------- clean texte (accents et maj) ---------------")
    texteRandom = (clean(texteRandom))       # TEST del_accents + passage en minuscule.
    print(texteRandom)
    print("\n --------------- occurenceOfLetter ---------------")
    print(occurenceOfLetter(texteRandom,alphalist)) # Test d'occurenceOfLetter doit retourner une liste du type : [0, 1, 1, 0, 2, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0].
    print("\n --------------- rateOfLetter ---------------")
    print(rateOfLetter(texteRandom,alphalist)) # Test de RateOfLetter doit retourner une liste avec la fréquence (arrondi à 3 chiffres après la virgule) d’apparition de chaque lettre.
    print("\n ---------------write et print (fichier1.txt)---------------")
    writeFile("fichier1.txt", texteRandom) # test de writeFile (ecrit dans le fichier)
    print(openFile("fichier1.txt"))   #test de openFile (affiche le contenu du fichier)
    #----------------- Lettre Cesar ------------------------
    print("\n ---------------Lettre Cesar---------------")
    LettreCesar = charToCesar("f",4,alphalist) #test de charToCesar
    print(LettreCesar) #Affiche le résultat de césar  
    print(cesarToChar(LettreCesar,4,alphalist)) #test de cesarToChar
    #----------------- Texte Cesar ------------------------
    print("\n ---------------textToCesar et cesarToText---------------")
    TexteCesar = textToCesar(texteRandom,21,alphalist)#test de textToCesar
    print(TexteCesar) #Affiche le résultat de césar 
    print(cesarToText(TexteCesar,21,alphalist))#test de cesarToText
    #----------------- File Cesar ------------------------
    print("---------------File Cesar (fichier2.txt)---------------")
    fileToCesar("fichier2.txt",4,alphalist)#test de fileToCesar (Créer un fichier2_code.txt)
    cesarTofile("fichier2_code.txt",4,alphalist)#test de cesarTofile (Créer un fichier2_decode.txt)
    #----------------- Texte Vig ------------------------
    print("\n ---------------TextToVig et VigToText---------------")
    TexteVig = textToVig(texteRandom,cleVig,alphalist)#test de textToVig
    print(TexteVig)
    print(vigToText(TexteVig,cleVig,alphalist))#test de vigToText
    #----------------- File Vig ------------------------
    print("---------------FileToVIG (fichier3.txt)---------------")
    fileToVig("fichier3.txt",cleVig,alphalist) #test de fileToVig : Chiffrement du fichier fichier3.txt -> fichier3_code.txt 
    vigToFile("fichier3_code.txt",cleVig,alphalist) #test de vigToFile fichier3_code.txt-> fichier3_decode.txt
    #----------------- Attaque ------------------------ 
    print("\n ---------------Attaque par brute force---------------")
    attaque_brute_force_sa(TexteCesar,alphalist) #test de attaque_brute_force_sa
    print("\n ---------------Attaque par E---------------")
    print(e_attack(TexteCesar,alphalist)) #test de e_attack
    print("\n ---------------Index C ---------------")
    print(indexC(TexteCesar,alphalist))#test de indexC
    print("\n ---------------Longueur de Clé ---------------")
    print(key_len("fichier3_code.txt",8,alphalist))#calcul la longuer de la clé (avec 8 en taille max)
    print("\n --------------- Clé ---------------")
    decode("fichier3_code.txt",8,alphalist) #test de decode : fichier3_code.txt (Avec maximum de 8 elements dans la clé) -> fichier3_decode.txt
    print("\n --------------- Doublement ---------------")
    att_doublement("fichier2_code.txt",alphalist)
    
if __name__ == "__main__":
    main()
