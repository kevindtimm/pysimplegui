# the import
import PySimpleGUI as sg

# layout definition
layout = [
  [sg.Text('My Layout')],
  [sg.Input(key='-INPUT-')],
  [sg.Button('OK', bind_return_key=True), sg.Button('Cancel')]
]

# create the window
window = sg.Window('Design Pattern 3 - Persistent Window', layout)

# event loop
while True:
  event, values = window.read()
  print (event, values)
  if event in (None, 'Cancel'):
    break

# close the window
window.close()

exit()
