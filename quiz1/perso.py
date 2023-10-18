import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import json
from tkinter import *
import PIL.Image
import os.path


from PIL import Image, ImageTk

class Perso:
    def __init__(self, root):
        self.root = root

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_foot
        self.quizperso = tk.Tk()
        self.quizperso.title("Quiz personaliser")
        self.quizperso.geometry("800x500")

        self.form_values =   {}
        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(self.quizperso, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Créez un label pour afficher un titre d'information
        label = tk.Label(self.quizperso, text="Faites un choix !!", font=(20))
        label.pack(pady=10)

        # Créez un cadre (Frame) pour contenir les boutons et les centrer
        button_frame = tk.Frame(self.quizperso)
        button_frame.pack(expand=True)
        

        # Créez les boutons pour les différentes options
        button1 = tk.Button(button_frame, text="Nouveau Quiz",width=20, height=2,command = self.displayForm)
        button1.pack(side="left", padx=20, pady=20)

        button2 = tk.Button(button_frame, text="Récuperer un quiz",width=20, height=2, command=self.importer_json)
        button2.pack(side="left", padx=20, pady=20)

    def importer_json(self):
        try:
            # Ouvrir une boîte de dialogue pour sélectionner un fichier JSON
            json_file = tk.filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])

            if json_file:
                with open(json_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.questions = data.get("questions", [])
                    self.reponses = data.get("reponses", [])
                    self.choix_reponses = data.get("choix_reponses", [])

                self.quizperso.destroy()
                # Créez la fenêtre quiz_perso
                self.quizchoix = tk.Tk()
                self.quizchoix.title("Quiz personaliser")
                self.quizchoix.geometry("800x500")

                # Chargez l'image à afficher en arrière-plan
                img_quiz=Image.open('fond_ecran_quiz.gif')
                photo_quiz = ImageTk.PhotoImage(img_quiz)
                # Créez un widget Label pour afficher l'image en arrière-plan
                background_label = tk.Label(self.quizchoix, image=photo_quiz)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Créez un label pour afficher la question
                self.question_label = tk.Label(self.quizchoix, text="", font=(20))
                self.question_label.pack(pady=10)

                # Créez des boutons pour les choix de réponses
                self.radio_var = tk.StringVar()  # Pour suivre la réponse sélectionnée
                self.buttons = []

                for i in range(4):
                    button = tk.Radiobutton(self.quizchoix, text="", variable=self.radio_var, value=i, command=lambda i=i: self.verifier_reponse(i))
                    button.pack(pady=5)
                    self.buttons.append(button)
        
                # Bouton pour passer à la question suivante
                self.suivant_button = tk.Button(self.quizchoix, text="Question suivante", command=self.question_suivante)
                self.suivant_button.pack()

                # Initialiser le quiz
                self.question_suivante()

                #Execution de la boucle pour la fenêtre du quiz du foot
                self.quizfootball.mainloop()


        except Exception as e:
            messagebox.showerror("Erreur lors de l'importation", str(e))

    

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
        self.quizfootball.destroy()

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
            label2 = tk.Label(fenetre_res, text="Bravo ! Vous êtes bien présent dans l'univers du football !!", font=(20))
            label2.place(x=400,y=300,anchor="center")

        #Execution de la boucle pour la fenêtre des résultats
        fenetre_res.mainloop()
        
    def displayForm(self):
        q_frame = Frame(self.quizperso, padx=10, pady=10,bg='white',width=1000,height=1000)
        q_frame.place(x=0, y=0)

        form_lab = Label(q_frame, text="Question",font=("bold", 20),bg="white")  
        form_lab.place(x=90,y=200)


        question = StringVar
        theme = Entry(q_frame,text="Question",textvariable = question)
        theme.place(x=90,y=245,width=500,height=50)


        ans1_lab = Label(q_frame, text="Réponse 1",font=("bold", 20),bg="white")  
        ans1_lab.place(x=90,y=300)


        reponse1 = StringVar
        ans1 = Entry(q_frame,text="Réponse 1",width=30,textvariable = reponse1)
        ans1.place(x=90,y=345,width=500,height = 50)

        ans2_lab = Label(q_frame, text="Réponse 2",font=("bold", 20),bg="white")  
        ans2_lab.place(x=90,y=400)

        reponse2 = StringVar
        ans2 = Entry(q_frame,text="Réponse 2",width=30,textvariable = reponse2)
        ans2.place(x=90,y=445,width=500,height = 50)

        ans3_lab = Label(q_frame, text="Réponse 3",font=("bold", 20),bg="white")  
        ans3_lab.place(x=90,y=500)



        reponse3 = StringVar
        ans3 = Entry(q_frame,text="Réponse 3",width=30,textvariable = reponse3)
        ans3.place(x=90,y=545,width=500,height = 50)

        ans4_lab = Label(q_frame, text="Réponse 4",font=("bold", 20),bg="white")  
        ans4_lab.place(x=90,y=600)


        reponse4 = StringVar
        ans4 = Entry(q_frame,text="Réponse 4",width=30,textvariable = reponse4)
        ans4.place(x=90,y=645,width=500,height = 50)

        ans5_lab = Label(q_frame, text="Réponse Correcte",font=("bold", 20),bg="white")  
        ans5_lab.place(x=90,y=700)


        reponse5 = StringVar
        ans5 = Entry(q_frame,text="Réponse Correcte",width=30,textvariable = reponse5)
        ans5.place(x=90,y=745,width=500,height = 50)


        self.form_values['question'] = theme
        self.form_values['ans1'] = ans1
        self.form_values['ans2'] = ans2
        self.form_values['ans3'] = ans3
        self.form_values['ans4'] = ans4
        self.form_values['ans5'] = ans5



        submit = tk.Button(q_frame,text="Ajouter",font=('Verdana',20),bg="skyblue",fg="white",width=10,height=1,command = self.submit_quiz )
        submit.place(x=90,y=815)
    
    
    def quizFormIsCorrectlyFilled(self):
        return True
    
    def submit_quiz(self):
        
        if self.quizFormIsCorrectlyFilled():
            if os.path.isfile('./perso_quiz.json'):
              with open('./perso_quiz.json','r') as file:
                  file_data = json.load(file)
                  
              file_data["questions"].append(self.form_values['question'].get())
              file_data["choix_reponses"].append(self.form_values['ans1'].get())
              file_data["choix_reponses"].append(self.form_values['ans2'].get())
              file_data["choix_reponses"].append(self.form_values['ans3'].get())
              file_data["choix_reponses"].append(self.form_values['ans4'].get())
              file_data["reponses"].append(self.form_values['ans5'].get())
              
              
              with open('./perso_quiz.json','w') as file:
                  json.dump(file_data,file)
            else :
                data = {
                    "questions" : [self.form_values['question'].get()],
                    "reponses" : [self.form_values['ans5'].get()],
                    "choix_reponses" : [self.form_values['ans1'].get(),self.form_values['ans2'].get(),self.form_values['ans3'].get(),self.form_values['ans4'].get()]
                    }
                with open('./perso_quiz.json','w') as file:
                    file.write(json.dumps(data))