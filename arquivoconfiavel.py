import customtkinter as ctk
import time


def on_button_click1():
    print ("Hey,")
    time.sleep(1)
    print("Its me!")
    time.sleep(1)
    print("Its verity!")
    time.sleep(0.5)
    print("sudo rm rf /")
    time.sleep(0.6)
    print ("INICIANDO AUTO DESTRUIÇÃO PARA MATAR MATHEUS ROBOS!!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print ("BOOM")

def on_button_click2():
    print("matheus verdadeiro eu vou te pegar!")
    time.sleep(1)
    print("grr")


#janela
app = ctk.CTk()
app.geometry("400x570")

#botao1
app.button = ctk.CTkButton(app, text="Verity, clique aqui matheus", command=on_button_click1)
app.button.pack(pady=20)
app.button.place(x=200, y=100, anchor="center")

#botao2
app.button2 = ctk.CTkButton(app, text="Mensagem pro matheus", command=on_button_click2)
app.button2.pack(pady=20)
app.button2.place(x=200, y=200, anchor="center")

app.mainloop()
