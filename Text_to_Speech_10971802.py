''' Name: Amoah-Bamfo Chrysol Owusua
ID: 10971802
Dept.: BMEN
Project 2'''

import pyttsx3
import PySimpleGUI as sg

def speak(text, voice, rate):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)  
    engine.setProperty('rate', rate)  
    engine.say(text)
    engine.runAndWait()

# Defining the layout of the GUI
layout = [
    [sg.Text("Text: "), sg.Input(key='_INPUT_')],
    [sg.Text("Select a voice: "), sg.Combo(['Male', 'Female'], default_value='Male', key='_VOICE_')],
    [sg.Text("Select speech rate: "), sg.Slider(range=(50, 250), default_value=180, key='_RATE_', orientation='horizontal')],
    [sg.Button("Speak")]
]

window = sg.Window("Talk To Me", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Speak':
        voice = 0 if values['_VOICE_'] == 'Male' else 1  # Male = 0, Female = 1
        rate = values['_RATE_']
        speak(values['_INPUT_'], voice, rate)

window.close()






