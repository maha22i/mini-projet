import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

class QuizFoot:
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0             # Initialiser le score à 0

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_foot
        self.quizfootball = tk.Tk()
        self.quizfootball.title("Quiz de football")
        self.quizfootball.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(self.quizfootball, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
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
            "Casemiro",
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

        self.questions = questions_football
        self.reponses = reponses_football
        self.choix_reponses = choix_reponses_football


        # Créez un label pour afficher la question
        self.question_label = tk.Label(self.quizfootball, text="", font=(20))
        self.question_label.pack(pady=10)

       # Créez des boutons pour les choix de réponses
        self.buttons = []

        for i in range(4):
            button = tk.Button(self.quizfootball, text="", command=lambda i=i: self.verifier_reponse(i))
            button.pack(pady=5)
            self.buttons.append(button)
        
        # Bouton pour passer à la question suivante
        self.suivant_button = tk.Button(self.quizfootball, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        # Initialiser le quiz
        self.question_suivante()

        #Execution de la boucle pour la fenêtre du quiz du foot
        self.quizfootball.mainloop()


    #button.config(text="terminer le test")
    def question_suivante(self):
        if self.current_question < len(self.questions):
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
    

    def terminer_quiz(self):
        #fermeture de la fenêtre du quiz
        self.quizfootball.destroy()

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
            label2 = tk.Label(fenetre_res, text="Bravo ! Vous êtes bien présent dans l'univers du football !!", font=(20))
            label2.grid(row=6, column=3, columnspan=2, sticky="s")

        #Execution de la boucle pour la fenêtre des résultats
        fenetre_res.mainloop()

