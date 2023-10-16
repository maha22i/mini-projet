import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('500x500')

questions = [...]
options = [...]

# Liste des réponses correctes
reponses_correctes = ['4', 'Kenya', 'Tagine', 'Golfe du Mexique', 'Dakar', 'Ramadan', 'CO2', 'Egypte', 'Masenqo', 'Alger', 'Djibouti', 'Nigéria', 'Énergie solaire', 'Sénégal', 'Sahara', 'Arabe', 'lac Tanganyika', 'Christianisme', 'Djibouti', 'mer Rouge', 'Lac Assal', 'Casablanca', 'Atlas', 'Mohammed VI', '1999']

frame = tk.Frame(root, padx=10, pady=10, bg='#fff')
question_label = tk.Label(frame, height=5, width=28, bg='grey', fg="#fff", font=('Verdana', 20), wraplength=500)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20), command=lambda: checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), command=lambda: checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), command=lambda: checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), command=lambda: checkAnswer(option4))

button_next = tk.Button(frame, text='Next', bg='Orange', font=('Verdana', 20), command=lambda: displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky='W', row=1, column=0)
option2.grid(sticky='W', row=2, column=0)
option3.grid(sticky='W', row=3, column=0)
option4.grid(sticky='W', row=4, column=0)

button_next.grid(row=6, column=0)

index = 0
correct = 0

# Créez une fonction pour désactiver les boutons radio
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

# Modifiez la fonction pour vérifier la réponse
def checkAnswer(radio):
    global correct, index

    # Compare la réponse de l'utilisateur avec la réponse correcte
    if radio['text'] == reponses_correctes[index]:
        correct += 1
        feedback = "Correct !"
    else:
        feedback = "Incorrect. La réponse correcte est : " + reponses_correctes[index]

    index += 1
    disableButtons('disable')

    # Affiche le feedback
    question_label.config(text=feedback)

# Modifiez la fonction pour afficher la réponse correcte à la fin
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
        question_label['text'] = "Résultat : " + str(correct) + " / " + str(len(options))
        button_next['text'] = 'Restart The Quiz'
        if correct >= len(options) / 2:
            question_label['bg'] = 'green'
        else:
            question_label['bg'] = 'red'
    else:
        question_label['text'] = questions[index]
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Voir les résultats'

displayNextQuestion()

root.mainloop()
