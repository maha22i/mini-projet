import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox
import quiz1

class QuizFoot:
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quizz_foot
        quizfootball = tk.Tk()
        quizfootball.title("Quiz de football")
        quizfootball.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(quizfootball, image=photo_quiz)
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

        self.frame = tk.Frame(root, padx=10, pady=10,bg='#fff')

        # Créez un label pour afficher la question
        self.question_label = tk.Label(self.frame,height=5, width=28,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=500)
        #self.question_label.pack(pady=10)

        # Créez un choix de réponses pour l'utilisateur
        v1 = StringVar(self.frame)
        v2 = StringVar(self.frame)
        v3 = StringVar(self.frame)
        v4 = StringVar(self.frame)

        option1 = tk.Radiobutton(self.frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
        option2 = tk.Radiobutton(self.frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
        option3 = tk.Radiobutton(self.frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
        option4 = tk.Radiobutton(self.frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))
        
        # Créez un bouton pour passer à la question suivante
        self.suivant_button = tk.Button(quizfootball, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        self.frame.pack(fill="both", expand="true")
        self.question_label.grid(row=0, column=0)

        option1.grid(sticky= 'W', row=1, column=0)
        option2.grid(sticky= 'W', row=2, column=0)
        option3.grid(sticky= 'W', row=3, column=0)
        option4.grid(sticky= 'W', row=4, column=0)

        self.suivant_button.grid(row=6, column=0)
    
        # create a function to disable radiobuttons
        def disableButtons(state):
            option1['state'] = state
            option2['state'] = state
            option3['state'] = state
            option4['state'] = state    
    
    
    
        # create a function to check the selected answer
        def checkAnswer(radio):
            # the 4th item is the correct answer
            # we will check the user selected answer with the 4th item
            if radio['text'] == self.choix_reponses_football[self.current_question][0]:
                self.score +=1

            self.current_question +=1
            disableButtons('disable')


    def question_suivante(self):
        if self.current_question < len(self.questions_football):
            self.question_label.config(text=self.questions_football[self.current_question])
            self.current_question += 1
        else:
            messagebox.showinfo("Fin du quiz", "Vous avez répondu à toutes les questions!")
            print("Votre score est de "+self.score)
            if self.score < 8 :
                messagebox.showinfo("Score","Mauvais score vous n'avez pas réussi le test ")
            else :
                messagebox.showinfo("Score","Bravo ! Vous êtes bien présent dans l'univers du football !!")
    
