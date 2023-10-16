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
        self.quizcapitales = tk.Tk()
        self.quizcapitales.title("Quiz sur les capitales")
        self.quizcapitales.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(self.quizcapitales, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.timer_seconds = 15  # Set the timer to 60 seconds
        self.timer_var = StringVar()
        self.timer_var.set(f"Time: {self.timer_seconds} seconds")

        self.timer_label = tk.Label(self.quizcapitales, textvariable=self.timer_var)
        self.timer_label.pack()
        self.update_timer()
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
        self.question_label = tk.Label(self.quizcapitales, text="", font=(20))
        self.question_label.pack(pady=10)

       # Créez des boutons pour les choix de réponses
        self.buttons = []

        for i in range(4):
            button = tk.Button(self.quizcapitales, text="", command=lambda i=i: self.verifier_reponse(i))
            button.pack(pady=5)
            self.buttons.append(button)
        
        # Bouton pour passer à la question suivante
        self.suivant_button = tk.Button(self.quizcapitales, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        # Initialiser le quiz
        self.question_suivante()

        #Execution de la boucle pour la fenêtre du quiz des capitales
        self.quizcapitales.mainloop()

    def question_suivante(self):
        if self.current_question < len(self.questions):
            self.timer_seconds=15 # Call your custom function            # self.quizhistoire.quit()
            self.timer_var.set(f"Time: {self.timer_seconds} seconds")
            self.question_label.config(text=self.questions[self.current_question])
            for i in range(4):
                self.buttons[i].config(text=self.choix_reponses[self.current_question][i])
            self.current_question += 1
        else:
            self.suivant_button.config(text="Terminer le quiz",command=self.terminer_quiz)



    def verifier_reponse(self, choix):
        if self.current_question <= len(self.reponses):
            reponse_utilisateur = self.choix_reponses[self.current_question - 1][choix]
            reponse_correcte = self.reponses[self.current_question - 1]
            if reponse_utilisateur.lower() == reponse_correcte.lower():
                self.score += 1
                messagebox.showinfo("Bonne réponse", "C'est correct!")
            else:
                messagebox.showerror("Mauvaise réponse", "La réponse correcte était : "+reponse_correcte+" .")
    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_var.set(f"Time: {self.timer_seconds} seconds")
            self.quizcapitales.after(1000, self.update_timer)  # Call update_timer after 1000 ms (1 second)
        else:
            response = messagebox.showinfo("Time's up!", "Your time is up.")
            if response == "ok":
                self.question_suivante() 
             
                self.update_timer()

    def terminer_quiz(self):
        #fermeture de la fenêtre du quiz
        self.quizcapitales.destroy()

        # Créez une nouvelle fenêtre pour le quiz
        fenetre_res = tk.Tk()
        fenetre_res.title("Résultas")
        fenetre_res.geometry("800x500")
        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(fenetre_res, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Créez un label pour annoncer le résultat du quizz
        label = tk.Label(fenetre_res, text="Voici votre résultat", font=(20))
        label.grid(row=0, column=3, columnspan=2, sticky="n")

        #Annoncer le résulat
        label1 = tk.Label(fenetre_res, text="Vous avez obtenu "+str(self.score)+" point(s) à ce quiz.", font=(20))
        label1.grid(row=5, column=3, columnspan=2, pady=10)

        #Commentaire de notre part
        if self.score<8:
            label2 = tk.Label(fenetre_res, text="Mauvais score vous n'avez pas réussi le test", font=(20))
            label2.grid(row=6, column=3, columnspan=2, sticky="s")
        else:
            label2 = tk.Label(fenetre_res, text="Bravo ! Vous êtes bien présent dans l'univers des capitales !!", font=(20))
            label2.grid(row=6, column=3, columnspan=2, sticky="s")

        #Execution de la boucle pour la fenêtre des résultats
        fenetre_res.mainloop()