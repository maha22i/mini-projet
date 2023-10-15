
import json
import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox
import time

with open('quiz.json', 'r', encoding='utf-8') as file: 
        data = json.load(file)


class QuizCapitales:
    def __init__(self,root):
        self.root = root
        self.current_question = 0
        self.score = 0             # Initialiser le score à 0
        self.questions = data["questions-cap"]
        self.reponses = data["reponses-cap"]
        self.choix_reponses = data["choix_reponses-cap"]
        
        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_capitales
        quizcapitales = tk.Tk()
        quizcapitales.title("Quiz sur les capitales")
        quizcapitales.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(quizcapitales, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
       
# Créez un label pour afficher le temps écoulé
        self.temps_label = tk.Label(quizcapitales, text="Temps écoulé: 0s")
        self.temps_label.pack()
        
# Mémorisez l'heure de début
        self.temps_debut = time.time()
        
            
 
# Exécutez la fonction pour mettre à jour le chronomètre
        self.mettre_a_jour_chronometre()
     
        # Mélangez les questions au début du jeu
        self.melanger_questions()    
            


        # Créez un label pour afficher la question
        self.question_label = tk.Label(quizcapitales, text="")
        self.question_label.pack(pady=10)

       # Créez des boutons pour les choix de réponses
        self.buttons = []

        for i in range(4):
            button = tk.Button(quizcapitales, text="", command=lambda i=i: self.verifier_reponse(i))
            button.pack(pady=5)
            self.buttons.append(button)
        
        # Bouton pour passer à la question suivante
        self.suivant_button = tk.Button(quizcapitales, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        # Initialiser le quiz
        self.question_suivante()

        #Execution de la boucle pour la fenêtre du quiz des capitales
        quizcapitales.mainloop()

            #///////////////////////////////////////////////////////

    def melanger_questions(self):
        combined = list(zip(self.questions, self.reponses, self.choix_reponses))
        random.shuffle(combined)
        self.questions, self.reponses, self.choix_reponses = zip(*combined)
        self.questions = list(self.questions)
        self.reponses = list(self.reponses)
        self.choix_reponses = list(self.choix_reponses)
        
        
    def question_suivante(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            for i in range(4):
                self.buttons[i].config(text=self.choix_reponses[self.current_question][i])
            self.current_question += 1
        else:
            messagebox.showinfo("Fin du quiz", "Quiz terminé. Score final : "+self.score+" points")
            if self.score < 8 :
                messagebox.showinfo("Score","Mauvais score vous n'avez pas réussi le test ")
            else :
                messagebox.showinfo("Score","Bravo ! Vous êtes bien présent dans l'univers des capitaless !!")


    def verifier_reponse(self, choix):
        if self.current_question <= len(self.reponses):
            reponse_utilisateur = self.choix_reponses[self.current_question - 1][choix]
            reponse_correcte = self.reponses[self.current_question - 1]
            if reponse_utilisateur.lower() == reponse_correcte.lower():
                self.score += 1
                messagebox.showinfo("Bonne réponse", "C'est correct!")
            else:
                messagebox.showerror("Mauvaise réponse", "La réponse correcte était : "+reponse_correcte+" .")
        else:
            messagebox.showerror("Toutes les questions ont déjà été posées.")
    
    
    def mettre_a_jour_chronometre(self):
            temps_actuel = time.time()
            temps_ecoule = temps_actuel - self.temps_debut
            self.temps_label.config(text="Temps écoulé: {:.1f}s".format(temps_ecoule))
            self.root.after(100, self.mettre_a_jour_chronometre)  # Appel récursif pour mettre à jour le temps