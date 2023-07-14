import tkinter as tk
from tkinter.ttk import *
from pynput.mouse import Button, Listener, Controller
import speech_recognition as sr


def calibration():
    def on_click(x, y, button, pressed):
        # przechwytywanie kliknięcia myszki
        global z
        z = [str(x), str(y)]
        if not pressed:
            # Stop listener
            return False

    def corner(state):
        # zapisywanie koordynatów do pliku
        global z
        with Listener(on_click=on_click) as listener:
            listener.join()
            f.write(z[0] + " " + z[1] + "\n")
            # sprawdzanie, czy zaznaczono pierwszy koordynat
            if not state:
                lewygorny.config(state="disabled")
                prawydolny.config(state="normal")
            else:
                cal_window.destroy()

    # otwarcie pliku z koordynatami
    f = open("Coordinates.txt", "w")
    f.truncate(0)

    # definiowanie okienka Kalibracji
    cal_window = tk.Toplevel(master)
    cal_window.resizable(False, False)
    cal_window.title("Kalibracja")
    cal_window.geometry("320x115")
    Label(cal_window, text="Kalibracja").pack()

    lewygorny = tk.Button(cal_window, text="Lewy GÓRNY róg", command=lambda: corner(False), width="60", height="2",pady="5")
    lewygorny.pack()

    prawydolny = tk.Button(cal_window, text="Prawy DOLNY róg", command=lambda: corner(True), width="60", height="2",pady="5")
    prawydolny.config(state="disabled")
    prawydolny.pack()

# kolor do wyboru, jaką stroną aktualnie gra osoba
color = ""


def start():
    def color_choose(side):
        # wybieranie koloru
        global color
        color = side
        start_window.destroy()
        loop()
    # główna pętla
    def loop():
        ruch = ""
        def voice():
            # przechwytywanie głosu z ruchem
            r = sr.Recognizer()

            with sr.Microphone() as source:
                r.pause_threshold = 0.7
                audio = r.listen(source)
                try:
                    Query = r.recognize_google(audio, language='pl-pl')
                    return Query
                except Exception as e:
                    print(e)

        while ruch != "szachmat":
            global color
            try:
                ruch = voice().lower().replace(" ", "").replace("-", "")
                print(ruch)
                mouse = Controller()
                if color == "white":
                    ruchod = Cords_white[ruch[0:2]]
                    ruchdo = Cords_white[ruch[2:4]]
                else:
                    ruchod = Cords_black[ruch[0:2]]
                    ruchdo = Cords_black[ruch[2:4]]
                print(ruchod, ruchdo)
                mouse.position = (ruchod[0], ruchod[1])
                mouse.press(Button.left)
                mouse.position = (ruchdo[0], ruchdo[1])
                mouse.release(Button.left)
            except:
                continue

    # otwarcie pliku z koordynatami, obliczanie koordynatów pól i definiowanie ich
    f = open("Coordinates.txt", "r")
    x, y, x2, y2 = map(int, f.read().split())
    zy = (y2 - y) / 8
    zx = (x2 - x) / 8

    Cords_white = {"a1": [x + 0.5 * zy, y + 7.5 * zx], "b1": [x + 1.5 * zy, y + 7.5 * zx],
                   "c1": [x + 2.5 * zy, y + 7.5 * zx], "d1": [x + 3.5 * zy, y + 7.5 * zx],
                   "e1": [x + 4.5 * zy, y + 7.5 * zx], "f1": [x + 5.5 * zy, y + 7.5 * zx],
                   "g1": [x + 6.5 * zy, y + 7.5 * zx], "h1": [x + 7.5 * zy, y + 7.5 * zx],

                   "a2": [x + 0.5 * zy, y + 6.5 * zx], "b2": [x + 1.5 * zy, y + 6.5 * zx],
                   "c2": [x + 2.5 * zy, y + 6.5 * zx], "d2": [x + 3.5 * zy, y + 6.5 * zx],
                   "e2": [x + 4.5 * zy, y + 6.5 * zx], "f2": [x + 5.5 * zy, y + 6.5 * zx],
                   "g2": [x + 6.5 * zy, y + 6.5 * zx], "h2": [x + 7.5 * zy, y + 6.5 * zx],

                   "a3": [x + 0.5 * zy, y + 5.5 * zx], "b3": [x + 1.5 * zy, y + 5.5 * zx],
                   "c3": [x + 2.5 * zy, y + 5.5 * zx], "d3": [x + 3.5 * zy, y + 5.5 * zx],
                   "e3": [x + 4.5 * zy, y + 5.5 * zx], "f3": [x + 5.5 * zy, y + 5.5 * zx],
                   "g3": [x + 6.5 * zy, y + 5.5 * zx], "h3": [x + 7.5 * zy, y + 5.5 * zx],

                   "a4": [x + 0.5 * zy, y + 4.5 * zx], "b4": [x + 1.5 * zy, y + 4.5 * zx],
                   "c4": [x + 2.5 * zy, y + 4.5 * zx], "d4": [x + 3.5 * zy, y + 4.5 * zx],
                   "e4": [x + 4.5 * zy, y + 4.5 * zx], "f4": [x + 5.5 * zy, y + 4.5 * zx],
                   "g4": [x + 6.5 * zy, y + 4.5 * zx], "h4": [x + 7.5 * zy, y + 4.5 * zx],

                   "a5": [x + 0.5 * zy, y + 3.5 * zx], "b5": [x + 1.5 * zy, y + 3.5 * zx],
                   "c5": [x + 2.5 * zy, y + 3.5 * zx], "d5": [x + 3.5 * zy, y + 3.5 * zx],
                   "e5": [x + 4.5 * zy, y + 3.5 * zx], "f5": [x + 5.5 * zy, y + 3.5 * zx],
                   "g5": [x + 6.5 * zy, y + 3.5 * zx], "h5": [x + 7.5 * zy, y + 3.5 * zx],

                   "a6": [x + 0.5 * zy, y + 2.5 * zx], "b6": [x + 1.5 * zy, y + 2.5 * zx],
                   "c6": [x + 2.5 * zy, y + 2.5 * zx], "d6": [x + 3.5 * zy, y + 2.5 * zx],
                   "e6": [x + 4.5 * zy, y + 2.5 * zx], "f6": [x + 5.5 * zy, y + 2.5 * zx],
                   "g6": [x + 6.5 * zy, y + 2.5 * zx], "h6": [x + 7.5 * zy, y + 2.5 * zx],

                   "a7": [x + 0.5 * zy, y + 1.5 * zx], "b7": [x + 1.5 * zy, y + 1.5 * zx],
                   "c7": [x + 2.5 * zy, y + 1.5 * zx], "d7": [x + 3.5 * zy, y + 1.5 * zx],
                   "e7": [x + 4.5 * zy, y + 1.5 * zx], "f7": [x + 5.5 * zy, y + 1.5 * zx],
                   "g7": [x + 6.5 * zy, y + 1.5 * zx], "h7": [x + 7.5 * zy, y + 1.5 * zx],

                   "a8": [x + 0.5 * zy, y + 0.5 * zx], "b8": [x + 1.5 * zy, y + 0.5 * zx],
                   "c8": [x + 2.5 * zy, y + 0.5 * zx], "d8": [x + 3.5 * zy, y + 0.5 * zx],
                   "e8": [x + 4.5 * zy, y + 0.5 * zx], "f8": [x + 5.5 * zy, y + 0.5 * zx],
                   "g8": [x + 6.5 * zy, y + 0.5 * zx], "h8": [x + 7.5 * zy, y + 0.5 * zx],
                   }

    Cords_black = {"h8": [x + 0.5 * zy, y + 7.5 * zx], "g8": [x + 1.5 * zy, y + 7.5 * zx],
                   "f8": [x + 2.5 * zy, y + 7.5 * zx], "e8": [x + 3.5 * zy, y + 7.5 * zx],
                   "d8": [x + 4.5 * zy, y + 7.5 * zx], "c8": [x + 5.5 * zy, y + 7.5 * zx],
                   "b8": [x + 6.5 * zy, y + 7.5 * zx], "a8": [x + 7.5 * zy, y + 7.5 * zx],

                   "h7": [x + 0.5 * zy, y + 6.5 * zx], "g7": [x + 1.5 * zy, y + 6.5 * zx],
                   "f7": [x + 2.5 * zy, y + 6.5 * zx], "e7": [x + 3.5 * zy, y + 6.5 * zx],
                   "d7": [x + 4.5 * zy, y + 6.5 * zx], "c7": [x + 5.5 * zy, y + 6.5 * zx],
                   "b7": [x + 6.5 * zy, y + 6.5 * zx], "a7": [x + 7.5 * zy, y + 6.5 * zx],

                   "h6": [x + 0.5 * zy, y + 5.5 * zx], "g6": [x + 1.5 * zy, y + 5.5 * zx],
                   "f6": [x + 2.5 * zy, y + 5.5 * zx], "e6": [x + 3.5 * zy, y + 5.5 * zx],
                   "d6": [x + 4.5 * zy, y + 5.5 * zx], "c6": [x + 5.5 * zy, y + 5.5 * zx],
                   "b6": [x + 6.5 * zy, y + 5.5 * zx], "a6": [x + 7.5 * zy, y + 5.5 * zx],

                   "h5": [x + 0.5 * zy, y + 4.5 * zx], "g5": [x + 1.5 * zy, y + 4.5 * zx],
                   "f5": [x + 2.5 * zy, y + 4.5 * zx], "e5": [x + 3.5 * zy, y + 4.5 * zx],
                   "d5": [x + 4.5 * zy, y + 4.5 * zx], "c5": [x + 5.5 * zy, y + 4.5 * zx],
                   "b5": [x + 6.5 * zy, y + 4.5 * zx], "a5": [x + 7.5 * zy, y + 4.5 * zx],

                   "h4": [x + 0.5 * zy, y + 3.5 * zx], "g4": [x + 1.5 * zy, y + 3.5 * zx],
                   "f4": [x + 2.5 * zy, y + 3.5 * zx], "e4": [x + 3.5 * zy, y + 3.5 * zx],
                   "d4": [x + 4.5 * zy, y + 3.5 * zx], "c4": [x + 5.5 * zy, y + 3.5 * zx],
                   "b4": [x + 6.5 * zy, y + 3.5 * zx], "a4": [x + 7.5 * zy, y + 3.5 * zx],

                   "h3": [x + 0.5 * zy, y + 2.5 * zx], "g3": [x + 1.5 * zy, y + 2.5 * zx],
                   "f3": [x + 2.5 * zy, y + 2.5 * zx], "e3": [x + 3.5 * zy, y + 2.5 * zx],
                   "d3": [x + 4.5 * zy, y + 2.5 * zx], "c3": [x + 5.5 * zy, y + 2.5 * zx],
                   "b3": [x + 6.5 * zy, y + 2.5 * zx], "a3": [x + 7.5 * zy, y + 2.5 * zx],

                   "h2": [x + 0.5 * zy, y + 1.5 * zx], "g2": [x + 1.5 * zy, y + 1.5 * zx],
                   "f2": [x + 2.5 * zy, y + 1.5 * zx], "e2": [x + 3.5 * zy, y + 1.5 * zx],
                   "d2": [x + 4.5 * zy, y + 1.5 * zx], "c2": [x + 5.5 * zy, y + 1.5 * zx],
                   "b2": [x + 6.5 * zy, y + 1.5 * zx], "a2": [x + 7.5 * zy, y + 1.5 * zx],

                   "h1": [x + 0.5 * zy, y + 0.5 * zx], "g1": [x + 1.5 * zy, y + 0.5 * zx],
                   "f1": [x + 2.5 * zy, y + 0.5 * zx], "e1": [x + 3.5 * zy, y + 0.5 * zx],
                   "d1": [x + 4.5 * zy, y + 0.5 * zx], "c1": [x + 5.5 * zy, y + 0.5 * zx],
                   "b1": [x + 6.5 * zy, y + 0.5 * zx], "a1": [x + 7.5 * zy, y + 0.5 * zx],
                   }

    # tworzenie okienka z wyborem koloru
    try:
        master.destroy()
    except:
        pass

    start_window = tk.Tk()
    start_window.resizable(False, False)
    start_window.title("Wybierz kolor: ")
    start_window.geometry("420x215")

    tk.Button(start_window, text="White", command=lambda: color_choose("white"), width="60", height="6", pady="5").pack()
    tk.Button(start_window, text="Black", command=lambda: color_choose("black"), width="60", height="6", pady="5").pack()

# tworzenie okienka startowego
master = tk.Tk()
master.geometry("420x215")
master.title("Szachy IRL")
master.resizable(False, False)

tk.Button(master, text="Resize", command=calibration, width="60", height="6", pady="5").pack()
tk.Button(master, text="Start", command=start, width="60", height="6", pady="5").pack()

master.mainloop()
