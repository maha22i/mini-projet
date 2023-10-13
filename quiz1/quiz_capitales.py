import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

class QuizCapitales:
    def __init__(self,root):
        self.root = root
        self.current_question = 0
        self.score = 0             # Initialiser le score à 0

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

        questions_capitales=[
            "Quelle est la capitale de la France ?",
            "Quelle est la capitale de l'Espagne ?",
            "Quelle est la capitale de l'Inde ?",
            "Quelle est la capitale de l'Australie ?",
            "Quelle est la capitale de l'Égypte ?",
            "Quelle est la capitale de l'Argentine ?",
            "Quelle est la capitale de la Suède ?",
            "Quelle est la capitale de la Russie ?",
            "Quelle est la capitale de la Turquie ?",
            "Quelle est la capitale de l'Afrique du Sud ?",
            "Quelle est la capitale du Canada ?",
            "Quelle est la capitale de la Norvège ?",
            "Quelle est la capitale du Kazakhstan ?",
            "Quelle est la capitale du Vietnam ?",
            "Quelle est la capitale du Luxembourg ?"
        ]
        reponses_capitales = [
            "Paris",
            "Madrid",
            "New Delhi",
            "Canberra",
            "Le Caire",
            "Buenos Aires",
            "Stockholm",
            "Moscou",
            "Ankara",
            "Pretoria",  # Afrique du Sud a plusieurs capitales
            "Ottawa",
            "Oslo",
            "Noursoultan",  # Anciennement Astana
            "Hanoï",
            "Luxembourg"
        ]

        choix_reponses_capitales = [
            ["Paris","Marseille","Lyon","Nice"],
            ["Madrid","Barcelone","Marbella","Séville"],
            ["New Delhi","NewYork","Istanbul","Alger"],
            ["Canberra","Berlin","Bogota","Dallas"],
            ["Le Caire","Colombo","Toronto","Dublin"],
            ["Buenos Aires","Manille","Oslo","Amsterdam"],
            ["Stockholm","Vancouver","Lima","Lisbonne"],
            ["Moscou","Marrakech","Prague","Rome"],
            ["Ankara","Tokuo","Sydney","Mexico","Pekin"],
            ["Pretoria","Lagos","Mumbai","Athènes"],  
            ["Ottawa","Budapest","Tanger","Djibouti"],
            ["Oslo","Shanghai","Chicago","Cancun"],
            ["Noursoultan","Dubai","Jakarta","Téhéran"], 
            ["Hanoï","Helsinki","Houston","Bangkok"],
            ["Luxembourg","Rabat","Strasbourg","Valenciennes"]
        ]

        self.questions = questions_capitales
        self.reponses = reponses_capitales
        self.choix_reponses = choix_reponses_capitales

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
