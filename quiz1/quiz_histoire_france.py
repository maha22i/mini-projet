import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

class QuizHistoire :
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0

        self.root.destroy()

        self.quizhistoire = tk.Tk()
        self.quizhistoire.title("Quiz d'histoire de France")
        self.quizhistoire.geometry("800x500")

        # Create a StringVar to display the timer

       

        # Start the timer

        # Load the image to display as a background
        img_quiz = Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        background_label = tk.Label(self.quizhistoire, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
 # Create a label to display the timer
        self.timer_seconds = 5  # Set the timer to 60 seconds
        self.timer_var = StringVar()
        self.timer_var.set(f"Time: {self.timer_seconds} seconds")

        self.timer_label = tk.Label(self.quizhistoire, textvariable=self.timer_var)
        self.timer_label.pack()
        self.update_timer()

        questions_histoire_france = [
            "Qui était le roi de France pendant la Révolution française ?",
            "Quelle célèbre bataille napoléonienne a eu lieu en 1815, marquant la fin de l'ère napoléonienne ?",
            "Qui était le roi de France pendant la construction de la cathédrale de Notre-Dame de Paris ?",
            "Quelle reine de France était la femme de Louis XVI ?",
            "Quel traité a mis fin à la Guerre de Cent Ans entre la France et l'Angleterre en 1453 ?",
            "Qui a dirigé le gouvernement provisoire de la France après la fin de la Seconde Guerre mondiale en 1945 ?",
            "Quel roi de France est également connu sous le nom de Louis le Grand et a étendu les frontières de la France au XVIIe siècle ?",
            "Qui a écrit le célèbre livre 'Les Trois Mousquetaires' qui se déroule en partie en France au XVIIe siècle ?",
            "Quelle reine de France a été surnommée 'Madame Déficit' en raison de ses dépenses excessives ?",
            "Quelle bataille de la Première Guerre mondiale a été témoin de l'utilisation de la toute première attaque de gaz toxique en 1915 ?",
            "Quel empereur français est souvent associé au Code civil, également connu sous le nom de Code Napoléon ?",
            "Quelle dynastie a régné sur la France pendant la majeure partie de la période médiévale ?",
            "Quelle révolution sociale et politique a eu lieu en France en 1789, conduisant à la chute de la monarchie ?",
            "Qui était le président de la France lors de l'abolition de la peine de mort en 1981 ?",
            "Quelle célèbre bataille de la Première Guerre mondiale a vu l'utilisation massive de tanks par l'armée française en 1917 ?"
        ]
        reponses_histoire_france = [
            "Louis XVI",
            "La bataille de Waterloo",
            "Louis VII",
            "Marie-Antoinette",
            "Le traité de Bordeaux",
            "Charles de Gaulle",
            "Louis XIV",
            "Alexandre Dumas",
            "Marie-Antoinette",
            "La bataille de Ypres",
            "Napoléon Bonaparte",
            "La dynastie des Capétiens",
            "La Révolution française",
            "François Mitterrand",
            "La bataille de Cambrai"
        ]
        choix_reponses_histoire_france = [
            ["Louis XVI","Louis XV","Louis XI","Louis XIV"],
            ["La bataille de Waterloo","La bataille de Poitier","La bataille de de Troyes","La bataille de 40 jours"],
            ["Louis VII","Louis VIII","Louis XVI","Charlemagne"],
            ["Marie-Antoinette","Marie-Therèse","Véronique","Marie-Helène"],
            ["Le traité de Bordeaux","Le traité de Versailles","Le traité de Londres","Le traité de Genève"],
            ["Charles de Gaulle","François Mitterrand","Jacques Chirac","Emmanuelle Macron"],
            ["Louis XIV","Louis XVI","Louis XV","Louis XI"],
            ["Alexandre Dumas","Voltaire","Baudelaire","Molière"],
            ["Marie-Antoinette","Marie de Médicis","Jeanne de Valois","Clotilde"],
            ["La bataille de Ypres","La bataille de la Somme","La bataille de Verdun","La bataille de Cambrai"],
            ["Napoléon Bonaparte","Charlemagne","Clovis","Capet"],
            ["La dynastie des Capétiens","La dynastie des Mérovingiens","La dynastie des Carolingiens","La dynastie des Bourbons"],
            ["La Révolution française","La Révolution parisienne","La Révolution du Nord","La Révolution marseillaise"],
            ["François Mitterrand","Jacques Chirac","François Hollande","Charles de Gaulle"],
            ["La bataille de Cambrai","La bataille de Verdun","La bataille de la Marne","La bataille de la Somme"]
        ]

        self.questions = questions_histoire_france
        self.reponses = reponses_histoire_france
        self.choix_reponses = choix_reponses_histoire_france


        # Créez un label pour afficher la question
        self.question_label = tk.Label(self.quizhistoire, text="", font=(20))
        self.question_label.pack(pady=10)

       # Créez des boutons pour les choix de réponses
        self.buttons = []

        for i in range(4):
            button = tk.Button(self.quizhistoire, text="", command=lambda i=i: self.verifier_reponse(i))
            button.pack(pady=5)
            self.buttons.append(button)
        
        # Bouton pour passer à la question suivante
        self.suivant_button = tk.Button(self.quizhistoire, text="Question suivante", command=self.question_suivante)
        self.suivant_button.pack()

        # Initialiser le quiz
        self.question_suivante()

        #Execution de la boucle pour la fenêtre du quiz de l'histoire de France
        self.quizhistoire.mainloop()

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
            self.quizhistoire.after(1000, self.update_timer)  # Call update_timer after 1000 ms (1 second)
        else:

            response = messagebox.showinfo("Time's up!", "Temps écoulé !")
            if response == "ok":
                self.question_suivante() 
              
              
                self.update_timer()
    
    def terminer_quiz(self):
        #fermeture de la fenêtre du quiz
        self.quizhistoire.destroy()

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
            label2 = tk.Label(fenetre_res, text="Bravo ! Vous êtes bien présent dans l'univers de l'histoire de France !!", font=(20))
            label2.grid(row=6, column=3, columnspan=2, sticky="s")

        #Execution de la boucle pour la fenêtre des résultats
        fenetre_res.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizHistoire(root)
    root.mainloop()