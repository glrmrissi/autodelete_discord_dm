import tkinter as tk
from threading import Thread, Event
import pyautogui
import time
import keyboard

stop_event = Event()


def play_deleted():
    count = 0
    notfound_count = 0
    scroll_amount = 366
    
    while not stop_event.is_set():
        try:
            notfound = pyautogui.locateCenterOnScreen("imgs/user.png", confidence=0.95)
            if notfound:
                x, y = notfound
                notfound_count += 1
                
                if notfound_count > 3:
                    pyautogui.scroll(abs(10))
                pyautogui.mouseDown(x + 300, y + -10)  
                pyautogui.mouseUp(x + 300, y + -10)  
                pyautogui.keyDown("shift")
                time.sleep(0.2) 
                # print(f"Ícone 'notfound' encontrado em: {notfound}")
                icon = pyautogui.locateCenterOnScreen("imgs/icone.png", confidence=0.95) \
                or pyautogui.locateCenterOnScreen("imgs/half_trash.png", confidence=0.95)
                if icon:
                    x2, y2 = icon 
                    count += 1
                    print(f"Quantos ja foram apagados: {count}")
                    pyautogui.mouseDown(x2, y2)  
                    time.sleep(0.2)  
                    pyautogui.mouseUp(x2, y2)
                    pyautogui.keyUp("shift")
                else:
                    # print("Icon não encontrado rolando para cima")
                    pyautogui.keyUp("shift")
                    time.sleep(0.1)
            else:
                pyautogui.keyUp("shift")
                # print("Ícone 'bab.png' não encontrado, rolando a tela pra cima...")
                time.sleep(0.1)
        except Exception as e:
            pyautogui.scroll(scroll_amount)
            pyautogui.keyUp("shift")
            # print("Erro:", e)
            time.sleep(0.1)

def start_play():
    stop_event.clear()
    thread = Thread(target=play_deleted, daemon=True)
    thread.start()
    print("Play iniciado")

def stop_play():
    stop_event.set()
    print("Play parado")
    
def listen_hotkey():
    keyboard.add_hotkey('ctrl+0', stop_play)
    keyboard.wait() 

root = tk.Tk()
root.title("Controlador Play/Stop")

btn_play = tk.Button(root, text="Play", command=start_play, bg="green", fg="white", font=("Arial", 16))
btn_play.pack(padx=10, pady=10)

btn_stop = tk.Button(root, text="Stop", command=stop_play, bg="red", fg="white", font=("Arial", 16))
btn_stop.pack(padx=10, pady=10)

hotkey_thread = Thread(target=listen_hotkey, daemon=True)
hotkey_thread.start()


root.mainloop()
