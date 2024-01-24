#Develope par Elwan Chollet 22 stMartin de france

import random

def initialiser_jeu():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  

def tirer_carte(jeu):
    carte = random.choice(jeu)
    jeu.remove(carte)
    return carte

def calculer_total(cartes):
    total = sum(cartes)
    if 11 in cartes and total > 21:
        total -= 10
    return total

def jeu_blackjack():
    jeu = initialiser_jeu()
    
    print("Entrez votre budget : ")
    while True:
        try:
            budget = int(input())
            if budget > 0:
                break
            else:
                print("Le budget doit etre un nombre positif. Reessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour le budget.")

    while budget > 0:
        print("Budget actuel:",budget)
        print("Entrez votre mise :")
        while True:
            try:
                mise = int(input())
                if mise > 0 and mise <= budget:
                    break
                else:
                    print("La mise doit etre un nombre positif et inferieur ou egale  votre budget. Reessayez.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour la mise.")
        budget -= mise
        joueur_cartes = [tirer_carte(jeu), tirer_carte(jeu)]
        croupier_cartes = [tirer_carte(jeu), tirer_carte(jeu)]

        joueur_total = calculer_total(joueur_cartes)
        croupier_total = calculer_total(croupier_cartes)
        print("Vos CRT :",joueur_cartes)
        print("Votre total :",joueur_total)
        print("Carte cr :",croupier_cartes[0])
      
        while True:
            if joueur_total == 21:
                print("Blackjack ! Vous avez gagne",mise*2.5)
                budget += mise*2.5
                joueur_cartes.clear()  # R  initialiser les cartes du joueur
                croupier_cartes.clear()
                break  # R  initialiser les cartes du croupier
                
            
            action = input("Tirer une carte ? (o/n): ")
            if action.lower() == 'o':
                joueur_cartes.append(tirer_carte(jeu))
            else:
                break

            joueur_total = calculer_total(joueur_cartes)
            croupier_total = calculer_total(croupier_cartes)
            print("Vos CRT :",joueur_cartes)
            print("Votre total :",joueur_total)
            print("Carte cr:",croupier_cartes[0])
            if joueur_total > 21 and joueur_total != 21:
                print("Vous avez depasser 21")
                print("Vous avez perdu.")
                joueur_cartes.clear()  # R  initialiser les cartes du joueur
                croupier_cartes.clear()  # R  initialiser les cartes du croupier
                break

        while croupier_total < 17 and joueur_total != 21:
            croupier_cartes.append(tirer_carte(jeu))
            croupier_total = calculer_total(croupier_cartes)
   

        
        print("Vos CRT :" ,joueur_cartes)        
        print("CRT cr :" ,croupier_cartes)
        
        
        if croupier_total > 21 and joueur_total < 21 and joueur_total != 21:
            print("Le cr a depasser 21.")
            print("Vous avez gagner",mise*2)
            budget += mise*2
            joueur_cartes.clear()  # R  initialiser les cartes du joueur
            croupier_cartes.clear()  # R  initialiser les cartes du croupier
            
        elif joueur_total > croupier_total and joueur_total < 21 and joueur_total != 21:
            print("Vous avez gagne",mise*2)
            budget += mise*2
            joueur_cartes.clear()  # R  initialiser les cartes du joueur
            croupier_cartes.clear()  # R  initialiser les cartes du croupier
        elif joueur_total == croupier_total and joueur_total < 21:
            print("Egalite. Remboursement de la mise.")
            budget += mise
            joueur_cartes.clear()  # R  initialiser les cartes du joueur
            croupier_cartes.clear()  # R  initialiser les cartes du croupier
            # Ne rien ajouter au budget en cas d'  galit  
        else :
          if joueur_total != 21 :
            print("Vous avez perdu",mise)
            

    print("Vous avez epuiser votre budget.")
    print("Fin du jeu.")

# Appel de la fonction principale
jeu_blackjack()