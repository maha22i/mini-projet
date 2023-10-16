import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import quiz1
from quiz_foot import QuizFoot
from quiz_capitales import QuizCapitales
from quiz_animaux import QuizAnimaux
from quiz_histoire_france import QuizHistoire
from perso import Perso

# Créez la fenêtre principale
root = tk.Tk()
root.title("MrQuiz")

#Taille de la fenetre d'acceuil
root.geometry("800x500")

# Chargez l'image à afficher en arrière-plan
img_acceuil=Image.open('fond_ecran_acceuil.gif')
photo_acceuil = ImageTk.PhotoImage(img_acceuil)
# Créez un widget Label pour afficher l'image en arrière-plan
background_label = tk.Label(root, image=photo_acceuil)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Créez le titre en haut et centre
bienvenu_label = tk.Label(root, text="Bienvenu sur MrQuiz !", font=(20))
bienvenu_label.pack(side=tk.TOP, pady=10)  # Placez le titre en haut avec un espacement en bas

# Fonction pour le choix du theme du quiz
def afficher_fenetre_quiz():
    # Fermez la fenêtre principale
    root.destroy()
    
    # Créez une nouvelle fenêtre pour le quiz
    fenetre_quiz = tk.Tk()
    fenetre_quiz.title("MrQuiz")
    fenetre_quiz.geometry("800x500")
    # Chargez l'image à afficher en arrière-plan
    img_quiz=Image.open('fond_ecran_quiz.gif')
    photo_quiz = ImageTk.PhotoImage(img_quiz)
    # Créez un widget Label pour afficher l'image en arrière-plan
    background_label = tk.Label(fenetre_quiz, image=photo_quiz)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Fonctions pour gérer les actions lorsque les boutons pour le choix des thèmes sont cliqués
    def foot():
        label.config(text="Vous avez choisi de jouer sur le football !!")
        if afficher_bouton_confirmation("le football")==1:
            QuizFoot(fenetre_quiz)

    def capitales():
        label.config(text="Vous avez choisi de jouer sur les capitales !!")
        if afficher_bouton_confirmation("les capitales")==1 :
            QuizCapitales(fenetre_quiz)

    def animaux():
        label.config(text="Vous avez choisi de jouer sur les animauxl !!")
        if afficher_bouton_confirmation("les animaux")==1  :
            QuizAnimaux(fenetre_quiz)

    def his_Fr():
        label.config(text="Vous avez choisi de jouer sur l'histoire de France !!")
        if afficher_bouton_confirmation("l'histoire de France") :
            QuizHistoire(fenetre_quiz)

    def perso():
        label.config(text="Vous avez choisi de créer votre quiz !!")
        if afficher_bouton_confirmation("un choix perso") == 1:
            Perso(fenetre_quiz)

    # Créez un label pour afficher le résultat des sélections
    label = tk.Label(fenetre_quiz, text="Faites un choix !!", font=(20))
    label.pack(pady=10)

    # Créez un cadre (Frame) pour contenir les boutons et les centrer
    button_frame = tk.Frame(fenetre_quiz)
    button_frame.pack(expand=True)

    # Créez les boutons pour les différentes options
    button1 = tk.Button(button_frame, text="Capitales",width=20, height=2, command=capitales)
    button1.pack(side="left", padx=20, pady=20)

    button2 = tk.Button(button_frame, text="Football",width=20, height=2, command=foot)
    button2.pack(side="left", padx=20, pady=20)
    
    button3 = tk.Button(button_frame, text="Histoire française",width=20, height=2, command=his_Fr)
    button3.pack(side="left", padx=20, pady=20)

    button4 = tk.Button(button_frame, text="Animaux",width=20, height=2, command=animaux)
    button4.pack(side="left", padx=20, pady=20)

    # Créez le bouton "Commencer" et liez-le à la fonction afficher_fenetre_quiz
    perso_button = tk.Button(fenetre_quiz, text="Personaliser", width=20, height=3, command=perso)

    # Placez le bouton au milieu en bas de la fenêtre principale
    perso_button.pack(side=tk.BOTTOM, padx=10, pady=50)

    def afficher_bouton_confirmation(message):
        confirmation = messagebox.askyesno("Confirmation", "Voulez-vous confirmer votre choix pour un quiz sur "+message+" ?")
        indicateur=0
        if confirmation:
            label.config(text="Choix confirmée")
            indicateur=1
        return indicateur

    # Exécutez la boucle principale pour la fenêtre du quiz
    fenetre_quiz.mainloop()


# Créez le bouton "Commencer" et liez-le à la fonction afficher_fenetre_quiz
commencer_button = tk.Button(root, text="Commencer", width=20, height=3, command=afficher_fenetre_quiz)

# Placez le bouton au milieu en bas de la fenêtre principale
commencer_button.pack(side=tk.BOTTOM, padx=10, pady=50)


root.mainloop()
