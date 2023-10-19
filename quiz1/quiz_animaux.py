import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox
import json

class QuizAnimaux :
    def __init__(self,root):
        self.root = root
        self.current_question = 0
        self.score = 0             # Initialiser le score à 0
        self.rep=False                 #Etat de réponse

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_animaux
        self.quizanimaux = tk.Tk()
        self.quizanimaux.title("Quiz sur les animaux")
        self.quizanimaux.geometry("1000x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(self.quizanimaux, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #Ajout du timer
        self.timer_seconds = 15  # Set the timer to 15 seconds
        self.timer_var = StringVar()
        self.timer_var.set(f"Time: {self.timer_seconds} seconds")

        self.timer_label = tk.Label(self.quizanimaux, textvariable=self.timer_var)
        self.timer_label.pack()
        self.update_timer()

        #Lecture du fichier .json pour récuperer les données du quiz
        with open('question_quiz.json', 'r', encoding='utf-8') as file: 
            data = json.load(file)

        self.questions = data["questions_animaux"]
        self.reponses = data["reponses_animaux"]
        self.choix_reponses = data["choix_reponses_animaux"]


        # Créez un label pour afficher la question
        self.question_label = tk.Label(self.quizanimaux, text="", font=(20))
        self.question_label.pack(pady=10)

       # Créez des boutons pour les choix de réponses
        self.radio_var = tk.StringVar()  # Pour suivre la réponse sélectionnée
        self.buttons = []

        for i in range(4):
            button = tk.Radiobutton(self.quizanimaux, text="", variable=self.radio_var, value=i, command=lambda i=i: self.verifier_reponse(i))
            button.pack(pady=5)
            self.buttons.append(button)
        
        # Bouton pour passer à la question suivante
        self.suivant_button = tk.Button(self.quizanimaux, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        # Initialiser le quiz
        self.question_suivante()

        #Execution de la boucle pour la fenêtre du quiz des animaux
        self.quizanimaux.mainloop()

    def question_suivante(self):
        if self.current_question < len(self.questions):
            self.timer_seconds=15 # Call your custom function            
            self.timer_var.set(f"Time: {self.timer_seconds} seconds")
            self.question_label.config(text=self.questions[self.current_question])
            for i in range(4):
                self.buttons[i].config(text=self.choix_reponses[self.current_question][i])
            self.radio_var.set(-1)  # Désélectionnez tous les boutons radio
            self.current_question += 1
            if self.rep==True:
                self.score+=1
                self.rep=False
        else:
            self.suivant_button.config(text="Terminer le quiz",command=self.terminer_quiz)
            if self.rep==True:
                self.score+=1
                self.rep=False

    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_var.set(f"Time: {self.timer_seconds} seconds")
            self.quizanimaux.after(1000, self.update_timer)  # Call update_timer after 1000 ms (1 second)
        else:
            response = messagebox.showinfo("Time's up!", "Temps écoulé !")
            if self.current_question < len(self.questions):
                if response == "ok":
                    self.question_suivante() 
                    self.update_timer()
            else :
                if response == "ok":
                    self.question_suivante()
                    self.terminer_quiz()

    def verifier_reponse(self,choix):
        if self.current_question <= len(self.reponses):
            if choix != -1 :
                reponse_utilisateur = self.choix_reponses[self.current_question - 1][choix]
                reponse_correcte = self.reponses[self.current_question - 1]
                if reponse_utilisateur.lower() == reponse_correcte.lower():
                    self.rep=True
                else:
                    self.rep=False
            
    def terminer_quiz(self):
        #fermeture de la fenêtre du quiz
        self.quizanimaux.destroy()

        # Créez une nouvelle fenêtre pour le quiz
        fenetre_res = tk.Tk()
        fenetre_res.title("Résultats")
        fenetre_res.geometry("800x500")
        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(fenetre_res, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Créez un label pour annoncer le résultat du quiz
        label = tk.Label(fenetre_res, text="Voici votre résultat", font=(20))
        label.place(x=400,y=100,anchor="center")

        #Annoncer le résulat
        label1 = tk.Label(fenetre_res, text="Vous avez obtenu "+str(self.score)+" point(s) à ce quiz.", font=(20))
        label1.place(x=400,y=200,anchor="center")

        #Commentaire de notre part
        if self.score<8:
            label2 = tk.Label(fenetre_res, text="Mauvais score vous n'avez pas réussi le test", font=(20))
            label2.place(x=400,y=300,anchor="center")
        else:
            label2 = tk.Label(fenetre_res, text="Bravo ! Vous êtes bien présent dans l'univers des animaux !!", font=(20))
            label2.place(x=400,y=300,anchor="center")

        #Execution de la boucle pour la fenêtre des résultats
        fenetre_res.mainloop() 