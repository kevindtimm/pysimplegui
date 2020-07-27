# the import
import PySimpleGUI as sg

# layout definition
layout = [
    [sg.Text('My Layout')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('OK', bind_return_key=True), sg.Button('Cancel')]
]

# create the window
window = sg.Window(title='Design Pattern 3 - Persistent Window', layout=layout)

# event loop
while True:
    event, values = window.read()
    print (event, values)
    if event in (None, 'Cancel'):
        break
    if event == 'OK':
        sg.Popup(f'values', values['-INPUT-'])

# close the window
window.close()

exit()
