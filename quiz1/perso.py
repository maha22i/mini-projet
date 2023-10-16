import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

class Perso:
    def __init__(self, root):
        self.root = root

        # Fermez la fenêtre des thèmes
        self.root.destroy()

        # Créez la fenêtre quiz_foot
        self.quizperso = tk.Tk()
        self.quizperso.title("Quiz personaliser")
        self.quizperso.geometry("800x500")

        # Chargez l'image à afficher en arrière-plan
        img_quiz=Image.open('fond_ecran_quiz.gif')
        photo_quiz = ImageTk.PhotoImage(img_quiz)
        # Créez un widget Label pour afficher l'image en arrière-plan
        background_label = tk.Label(self.quizfootball, image=photo_quiz)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Créez un label pour afficher le résultat des sélections
        label = tk.Label(self.quizperso, text="Faites un choix !!", font=(20))
        label.pack(pady=10)

        # Créez un cadre (Frame) pour contenir les boutons et les centrer
        button_frame = tk.Frame(self.quizperso)
        button_frame.pack(expand=True)

        # Créez les boutons pour les différentes options
        button1 = tk.Button(button_frame, text="Nouveau Quiz",width=20, height=2, command=capitales)
        button1.pack(side="left", padx=20, pady=20)

        button2 = tk.Button(button_frame, text="Récuperer un quiz",width=20, height=2, command=foot)
        button2.pack(side="left", padx=20, pady=20)