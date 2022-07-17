import PySimpleGUI as sg

appLayout = [[
    sg.Column(layout=[[
        sg.Drop(values=['Starcraft', 'Diablo', 'Overwatch']),
        sg.VerticalSeparator(),
        sg.Image(key='-Image-'),
    ]])
], [sg.Column(layout=[[sg.Button('Play')], [sg.HSep()], [sg.Exit()]])]]

window: sg.Window = sg.Window(title='Choose My Game',
                              layout=appLayout,
                              auto_size_buttons=True,
                              auto_size_text=True,
                              resizable=True,
                              text_justification='Center',
                              element_justification='center')
