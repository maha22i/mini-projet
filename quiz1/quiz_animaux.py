import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

class QuizAnimaux :
    def __init__(self,root):
        self.root = root
        self.current_question = 0
        self.score = 0             # Initialiser le score à 0

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_animaux
        self.quizanimaux = tk.Tk()
        self.quizanimaux.title("Quiz sur les animaux")
        self.quizanimaux.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(self.quizanimaux, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        questions_animaux = [
            "Quel est le plus grand animal terrestre ?",
            "Quel animal est souvent appelé 'le roi de la jungle' ?",
            "Quel est l'oiseau national des États-Unis ?",
            "Quel animal est capable de régénérer des parties de son corps, y compris des membres entiers ?",
            "Quel est le plus grand reptile au monde ?",
            "Quel insecte est connu pour produire de la lumière par bioluminescence ?",
            "Quel animal est capable de voler sans ailes, utilisant un mécanisme de lévitation ?",
            "Quel est le plus grand animal marin de tous les temps ?",
            "Quel mammifère est capable de voler et est souvent confondu avec les oiseaux ?",
            "Quel animal est considéré comme le plus rapide de la planète ?",
            "Quel reptile est réputé pour sa longévité, certaines espèces vivant pendant plus de 100 ans ?",
            "Quel est le plus grand félin du monde ?",
            "Quel est le plus grand animal terrestre après l'éléphant ?",
            "Quel animal est Nemo ?",
            "Quel animal est connu pour sa capacité à changer de couleur en fonction de son environnement ?"
        ]
        reponses_animaux = [
            "L'éléphant d'Afrique",
            "Le lion",
            "L'aigle chauve",
            "L'étoile de mer",
            "Le crocodile marin",
            "Le luciole",
            "La chauve-souris",
            "La baleine bleue",
            "La chauve-souris",
            "Le faucon pèlerin",
            "La tortue",
            "Le tigre",
            "Le rhinocéros",
            "Le poisson-clown",
            "Le caméléon"
        ]
        choix_reponses_animaux = [
            ["L'éléphant d'Afrique","Girafe","Zebre","Gorille"],
            ["Le lion","Panda","Singe","Ours"],
            ["L'aigle chauve","Hirondelle",'Hibou',"Chouette"],
            ["L'étoile de mer","Lezard","Serpent","Arraignée"],
            ["Le crocodile marin","Cobra","Iguane","Tortue"],
            ["Le luciole","Mouche","Sauterelle","Chenille"],
            ["La chauve-souris","Papillon","Hibou","Corbeau"],
            ["La baleine bleue","Morse","Requin blanc","baleine à bosse"],
            ["La chauve-souris","Ecureuil volant","Murène volante","Kagou volant"],
            ["Le faucon pèlerin","Léopard","Panthère","Aigle royal"],
            ["La tortue","Baleine","Requin","Anaconda"],
            ["Le tigre","Guepard","Jaguar","Puma"],
            ["Le rhinocéros","Hippopotame","Girafe","Bufle"],
            ["Le poisson-clown","Saumon","Carpe","Truite"],
            ["Le caméléon","Iguane","Lezard","Serpent"]
        ]

        self.questions = questions_animaux
        self.reponses = reponses_animaux
        self.choix_reponses = choix_reponses_animaux


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
            self.question_label.config(text=self.questions[self.current_question])
            for i in range(4):
                self.buttons[i].config(text=self.choix_reponses[self.current_question][i])
            self.radio_var.set(-1)  # Désélectionnez tous les boutons radio
            self.current_question += 1
        else:
            self.suivant_button.config(text="Terminer le quiz",command=self.terminer_quiz)


    def verifier_reponse(self,choix):
        if self.current_question <= len(self.reponses):
            if choix != -1 :
                reponse_utilisateur = self.choix_reponses[self.current_question - 1][choix]
                reponse_correcte = self.reponses[self.current_question - 1]
                if reponse_utilisateur.lower() == reponse_correcte.lower():
                    self.score += 1
            else:
                messagebox.showerror("Sélectionnez une réponse", "Veuillez sélectionner une réponse.")

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

        # Créez un label pour annoncer le résultat du quizz
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