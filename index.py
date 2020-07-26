import PySimpleGUI as sg
import sys
import os

class Screen():
  def __init__(self):
    # Layout
    layout = [
      [sg.Text('Username:', size=(10,0)), sg.Input(key='-USERNAME-', size=(35,0))],
      [sg.Text('Password:', size=(10,0)), sg.Input(key='-PASSWORD-', size=(35,0), password_char='*')],
      [sg.Button('Submit'), sg.Exit()]
    ]
    # Window
    self.window = sg.Window('Login').layout(layout)

  def Start(self):
    retries = 3
    while True:
      # collect info
      self.Button, self.values = self.window.Read()

      if self.Button in (None, 'Exit'):
        exit()
      elif self.Button == 'Submit':
        sg.Popup('Username {}\nPassword {}'.format(self.values['-USERNAME-'], self.values['-PASSWORD-']))

      retries -= 1
      if retries == 0:
        sg.PopupError('No Valid Username/Password')
        exit(0)

load = Screen()
load.Start()