import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('500x500')

questions = ["Combien de piliers de l'islam y a-t-il ?",
             "Quel pays est souvent appelé la perle de l'Afrique de l'Est en raison de ses paysages impressionnants ?",
             "Quel est le plat traditionnel marocain à base de viande d'agneau et de couscous ?",
             "Quel est le nom de la grande étendue d'eau salée qui sépare l'Afrique de l'Arabie Saoudite ?",
             "Quelle capitale est située sur la côte atlantique du Sénégal ?",
             "Quel est le mois saint du jeûne musulman ?",
             "Quel est le gaz à effet de serre le plus abondant dans l'atmosphère terrestre ?",
             "Quel pays est situé à l'extrême nord de l'Afrique et partage sa frontière sud avec la Méditerranée ?",
             "Quel instrument de musique traditionnel est souvent associé à la musique éthiopienne ?",
             "Quelle est la plus grande ville d'Algérie ?",
             "Dans quel pays africain se trouve la ville de Djibouti, la capitale du pays ?",
             "Quel pays africain est le plus peuplé ?",
             "Quelle est la principale source d'énergie renouvelable produite à partir de la lumière du soleil ?",
             "Quel est le nom du fleuve qui traverse la ville de Dakar au Sénégal ?",
             "Quel désert occupe une grande partie du nord de l'Afrique ?",
             "Quelle est la langue officielle de l'Égypte ?",
             "Quel est le nom du lac le plus profond d'Afrique ?",
             "Quelle est la plus grande religion en Éthiopie ?",
             "Quel pays est souvent appelé la porte de l'Afrique en raison de sa position géographique ?",
             "Quel est le nom de la mer qui borde la côte est de l'Afrique ?",
             "Quel est le point le plus bas du continent africain ?",
             "Quelle est la plus grande ville du Maroc ?",
             "Quel est le nom de la chaîne de montagnes qui traverse le Maroc et est célèbre pour sa beauté naturelle ?",
             "Qui est le roi actuel du Maroc en 2023 ?",
             "En quelle année Mohammed VI est-il devenu roi du Maroc ?"
             ]
options = [['4','5','6','7','2'],['Kenya','Maroc','Tanzanie','Algerie','Djibouti'],
           ['Sushi','Paella','Tagine','Pizza','Burger'],['Golfe du Mexique','Golfe Aden','Golfe Persique','Golfe du Lion','Lac assal'],
           ['Dakar','Nairobi','Somalie','Addiss Abeba','Tunis'],
           ['Ramadan','Shawwal','Dhul-Hijjah','Safar','karem'],
           ['Azote','oxygène','CO2','Méthane','H2O'],
           ['Tunisie','Maroc','Egypte','libye','Congo'],
           ['Guitare','Violon','Saxophone','Masenqo','Piano'],
           ['Oran','Ouganda','Tadjourah','Arta','Alger'],
           ['Djibouti','Somalie','Erythrée','Soudan','Cap vert'],
           ['Nigéria','Ethiopie','Afrique du Sud','Egypte','Niger'],
           ['nergie solaire','Énergie géothermique','Énergie hydraulique','Énergie éolienne','Charpon'],
           
           ]


frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=28,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
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
            button_next['text'] = 'Check the Results'





displayNextQuestion()

root.mainloop()