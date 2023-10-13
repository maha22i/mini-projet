import json
import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

with open('quiz.json', 'r', encoding='utf-8') as file: 
        data = json.load(file)

class QuizFoot:
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0             # Initialiser le score à 0

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_foot
        quizfootball = tk.Tk()
        quizfootball.title("Quiz de football")
        quizfootball.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(quizfootball, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        """
        questions_football = [
            "Qui est généralement considéré comme le meilleur joueur de football de tous les temps ?",
            "Quelle équipe nationale a remporté le plus de Coupes du Monde de la FIFA ?",
            "Qui est le meilleur buteur de tous les temps en Ligue des Champions de l'UEFA ?",
            "Dans quelle ville se trouve le stade Santiago Bernabéu, qui abrite le Real Madrid ?",
            "Qui est le capitaine actuel de l'équipe nationale de football du Brésil ?",
            "Quel pays a remporté la dernière Copa America ?",
            "Qui a remporté le Ballon d'Or en 2021 ?",
            "Quel joueur de football est surnommé 'La Pulga' ?",
            "Quelle équipe a remporté le plus de titres de la Premier League anglaise ?",
            "Quel numéro à porter Neymar avec le Barça ?",
            "Qui a remporté la Coupe d'Afrique des Nations (CAN) en 2019 ?",
            "Quel joueur de football est connu sous le surnom 'CR7' ?",
            "Qui est le manager actuel de l'équipe nationale d'Allemagne ?",
            "Quel pays a remporté la médaille d'or en football masculin lors des Jeux Olympiques de Tokyo 2020 ?",
            "Qui est le meilleur buteur de l'histoire de la Coupe du Monde de la FIFA ?"
        ]
        reponses_football = [
            "Pelé",
            "Brésil",
            "Cristiano Ronaldo",
            "Madrid",
            "Casemiro (en 2021)",
            "Argentine",
            "Lionel Messi",
            "Lionel Messi",
            "Manchester United",
            "11",
            "Algérie",
            "Cristiano Ronaldo",
            "Joachim Löw",
            "Brésil",
            "Miroslav Klose"
        ]

        choix_reponses_football = [
            ["Pelé","Neymar","Hakimi","Ziyech"],
            ["Brésil","France","Italie","Argentine"],
            ["Cristiano Ronaldo","Messi","Mbappe","Zidane"],
            ["Madrid","Barcelone","Paris","Londres"],
            ["Casemiro","Neymar","Silva","Marcelo"],
            ["Argentine","Uruguay","Chili","Mexique"],
            ["Lionel Messi","Cristiano Ronaldo","Neymar","Benzema"],
            ["Lionel Messi","Haaland","Ozil","Veratti"],
            ["Manchester United","Manchester City","Chelsea","Arsenal"],
            ["11","10","9","7"],
            ["Algérie","Maroc","Egypte","Sénégal"],
            ["Cristiano Ronaldo","Cesar Raton","Charly Rompero","Carlos Rachel"],
            ["Joachim Löw","Martin Luther","Boris Becker","Karl Lagerfeld"],
            ["Brésil","France","Etats-Unis","Italie"],
            ["Miroslav Klose","Cristiano Ronaldo","Lionel Messi","Diegp Maradona"]
        ]
        """
        self.questions = data["questions_football"]
        self.reponses = data["reponses_football"]
        self.choix_reponses = data["choix_reponses_football"]


        # Créez un label pour afficher la question
        self.question_label = tk.Label(quizfootball, text="")
        self.question_label.pack(pady=10)

       # Créez des boutons pour les choix de réponses
        self.buttons = []

        for i in range(4):
            button = tk.Button(quizfootball, text="", command=lambda i=i: self.verifier_reponse(i))
            button.pack(pady=5)
            self.buttons.append(button)
        
        # Bouton pour passer à la question suivante
        self.suivant_button = tk.Button(quizfootball, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        # Initialiser le quiz
        self.question_suivante()

        #Execution de la boucle pour la fenêtre du quiz du foot
        quizfootball.mainloop()



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
                messagebox.showinfo("Score","Bravo ! Vous êtes bien présent dans l'univers du football !!")


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
