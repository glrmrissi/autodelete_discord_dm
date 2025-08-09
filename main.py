import tkinter as tk
from threading import Thread, Event
import pyautogui
import time
import keyboard

stop_event = Event()

def play_deleted():
    scroll_amount = 355
    
    while not stop_event.is_set():
        try:
            nencontrado = pyautogui.locateCenterOnScreen("imgs/user.png", confidence=0.9)
            if nencontrado:
                x, y = nencontrado
                deslocamento = 299  
                pyautogui.mouseDown(x + deslocamento, y)  
                pyautogui.mouseUp(x + deslocamento, y)  
                pyautogui.keyDown("shift")
                time.sleep(0.2) 
                print(f"Ícone 'nencontrado' encontrado em: {nencontrado}")
                icone = pyautogui.locateCenterOnScreen("imgs/icone.png")
                if icone:
                    print(f"Ícone principal encontrado em: {icone}")
                    x2, y2 = icone 
                    pyautogui.mouseDown(x2, y2)  
                    time.sleep(0.2)  
                    pyautogui.mouseUp(x2, y2)
                    pyautogui.keyUp("shift")
                else:
                    time.sleep(0.5)
            else:
                pyautogui.keyUp("shift")
                print("Ícone 'bab.png' não encontrado, rolando a tela pra cima...")
                time.sleep(0.2)
        except Exception as e:
            pyautogui.scroll(scroll_amount)
            pyautogui.keyUp("shift")
            print("Erro:", e)
            time.sleep(0.2)

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

btn_play = tk.Button(root, text="▶ Play", command=start_play, bg="green", fg="white", font=("Arial", 16))
btn_play.pack(padx=10, pady=10)

btn_stop = tk.Button(root, text="■ Stop", command=stop_play, bg="red", fg="white", font=("Arial", 16))
btn_stop.pack(padx=10, pady=10)

hotkey_thread = Thread(target=listen_hotkey, daemon=True)
hotkey_thread.start()


root.mainloop()

