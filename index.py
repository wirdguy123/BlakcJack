import PySimpleGUI as pys 
from the_hands import  phand, chand
pys.theme()
Start_Set = [[pys.Text('Christopher\'s Black Jack', )],
             [pys.Button('Start')],
             [pys.Text('Exit', enable_events='True')]]
start_window = pys.Window('Start Menu', Start_Set, size=(500, 500) )