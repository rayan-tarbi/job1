programEnd = 0
while programEnd == 0:
    Selection = int(input("Selectionne l'exo : "))
    if Selection == 0:
        programEnd = 1
    elif Selection == 1:
        def My_print_hello():
            print("Hello")
        My_print_hello()
    elif Selection == 2:
        def My_print_name():
            name = input("Entrez votre nom : ")
            print(f"Vous vous appellez {name} ")
        My_print_name()
    elif Selection == 3:
        def Add(a, b):
            print(f"La somme de {a} + {b} = {a + b}")
        Add(4, 8)
        Add(12, 5)
        Add(128, 488)
    elif Selection == 4:
        def GetHello():
            return ("Hello la plateforme")
        resultat = GetHello()
        print(resultat)
    elif Selection == 5:
        def Calcule(num1, operator, num2):
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            elif operator == "/":
                if num2 != 0:
                    return num1 / num2
                else:
                    print("Erreur suite a une division par 0 : ")
            else:
                print("Calcule impossible !")
        num1 = int(input("Entrez la valeur 1 : "))
        operator = input("Entrez l'operateur (* ,/ ,+ ou -) : ")
        num2 = int(input("Entrez la deuxième valeur du calcul."))
        resultat = Calcule(num1, operator, num2)
        print((f"Le résultat de votre calcul est {resultat} !"))
    elif Selection == 6:
        def nombre():
            Nana = int(input("Entrez le nombre que vous voulez vérifié : "))
            if Nana >= 0:
                print("Le nombre est égal ou supérieur a 0")
            else:
                print("Le nombre est infèrieur a 0")
        nombre()
    elif Selection == 7:
        def langage(prout):
            if prout == "javascript":
                return "Tu es un développeur Web"
            elif prout == "python":
                return "Tu es un développeur IA"
            elif prout == "java":
                return "Tu es un développeur logiciel"
            elif prout == "reactjs":
                return "Tu es un développeur mobile"
            else:
                return "Un jour je serrais le meilleur développeur !"
        print(langage ("javascript"))
        print(langage ("python"))
        print(langage ("java"))
        print(langage ("reactjs"))
        print(langage ("salut"))
    elif Selection == 8:
        def job8(Type, saison):
            if Type == "fruits" and saison == "hiver":
                return("orange mandarine et kiwi")
            elif Type == "fruits" and saison == "été":
                return("Poire fraise cassis")
            elif Type == "légume" and saison == "hiver":
                return("Carotte Topinambour endive")
            elif Type == "légume" and saison == "été":
                return("artichaut aubergine navet")
        print(job8("fruits", "hiver"))
        print(job8("fruits", "été"))
        print(job8("légume", "hiver"))
        print(job8("légume", "été"))
    elif Selection == 9:
        def moyen(note1, note2, note3):
            return (note1 + note2 + note3) / 3
        note1 = float(input("Entrez la note 1 : "))
        note2 = float(input("Entrez la note 2 : "))
        note3 = float(input("Entrez la note 3 : "))

        moyenne_etudiant = moyen(note1, note2, note3)

        if 15 <= moyenne_etudiant <= 20:
            print("Très bon élève")
        elif 11 <= moyenne_etudiant <= 14:
            print("Bon élève")
        elif 8 <= moyenne_etudiant <= 10:
            print("Élève moyen")
        elif 0 <= moyenne_etudiant <= 7:
            print("Élève devant faire des efforts")
        else:
            print("Erreur : Les notes doivent être entre 0 et 20.")
    elif Selection == 10:
        def job10(nombre):
            if not isinstance(nombre, int):
                return "Le nombre dois être un entier."
            if nombre < 0:
                return " le nombre dois être positif"
            if nombre % 2 == 0:
                return f"{nombre} est un nombre pair."
            else:
                return f"{nombre} est un nombre impair."
        print(job10(10))
        print(job10(-5))
        print(job10(7))
    elif Selection == 11:
        def time_to_text(minute):
            if not isinstance(minute, int) or minute < 0:
                print("Entrez un nombre entier positif.")
            heures = minute // 60
            minutes_restantes = minute % 60
            print(f"{heures} heure et {minutes_restantes} minutes")
        time_to_text(7)
        time_to_text(150)
        time_to_text(43)
        time_to_text(52)
    elif Selection == 12:
        def chips(texte):
            return texte[::-1]
        mot = "nikana"
        mot_inverser = chips(mot)
        print(mot_inverser)
