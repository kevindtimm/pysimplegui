# http://www.PySimpleGUI.org

import PySimpleGUI as sg

layout = [
  [sg.Text('Enter something:'), sg.Input(key='-IN-')],
  [sg.Text('Output will go here', key='-OUT')],
  [sg.Button('Ok'), sg.Button('Exit')],
]

window = sg.Window('Scratch0722', layout)

while True:
  event, values = window.Read()
  if event in (None, 'Exit'):
    break

  window['-OUT'].update(values['-IN-'])

window.close()