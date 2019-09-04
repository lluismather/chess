import gui


WIDTH = 800
HEIGHT = 600
FRAMERATE = 0.01

window = gui.gui(width=WIDTH, height=HEIGHT, framerate=FRAMERATE)

while True:
    window.update_frames()
