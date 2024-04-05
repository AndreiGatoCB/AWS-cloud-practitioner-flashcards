from tkinter import *
import random
import pandas as pd
import pyperclip
import tkinter as tk
from tkinter import ttk

BACKGROUND_COLOR = "dark slate grey"
BACKGROUND_COLOR1 = "#B1DDC6"
BACKGROUND_COLOR2 = 'steel blue'

data_en = pd.read_csv('data/data_en.csv')
data_es = pd.read_csv('data/data_es.csv')
data_de = pd.read_csv('data/data_de.csv')
data_fr = pd.read_csv('data/data_fr.csv')
data_it = pd.read_csv('data/data_it.csv')
data_pt = pd.read_csv('data/data_pt.csv')

data_en_dict = data_en.to_dict(orient='records')
data_es_dict = data_es.to_dict(orient='records')
data_de_dict = data_de.to_dict(orient='records')
data_fr_dict = data_fr.to_dict(orient='records')
data_it_dict = data_it.to_dict(orient='records')
data_pt_dict = data_pt.to_dict(orient='records')

preguntas_idiomas = {
    'español': data_es_dict,
    'inglés': data_en_dict,
    'alemán': data_de_dict,
    'francés': data_fr_dict,
    'italiano': data_it_dict,
    'portugués': data_pt_dict
}

carta_actual = {}
correctas = 0
botones_habilitados = True
idioma_seleccionado = None
window = None
rta_user = []
cant_preguntas = 65

def mostrar_resumen():
    global correctas
    window.destroy()

    ventana_resumen = Tk()
    ventana_resumen.title("Fin del juego")
    ventana_resumen.config(pady=20, padx=20, bg=BACKGROUND_COLOR2)

    etiqueta_correctas = Label(ventana_resumen, text=f"Respuestas Correctas: {correctas}/{cant_preguntas}",
                               font=("Ariel", 16, "bold"), bg=BACKGROUND_COLOR2)
    etiqueta_correctas.pack()

    agradecimientos = Label(ventana_resumen,
                            text=f"Gracias por jugar.\nEste juego fue desarrollado por AndreiGatoCB.\nPara comentarios, dudas y agradecimientos:",
                            font=("Ariel", 16, "bold"), bg=BACKGROUND_COLOR2)
    agradecimientos.pack()

    contacto = Label(ventana_resumen,
                     text=f"github: https://github.com/AndreiGatoCB\nlinkedin: https://www.linkedin.com/in/brandon-andrei-albornoz-lizarazo/",
                     font=("Ariel", 16, "bold"), bg=BACKGROUND_COLOR2)
    contacto.pack()

    etiqueta_agradecimiento = Label(ventana_resumen, text="¡Gracias por jugar!", font=("Ariel", 14),
                                    bg=BACKGROUND_COLOR2)
    etiqueta_agradecimiento.pack()

    ventana_resumen.mainloop()


def iniciar_programa():
    global idioma_seleccionado
    idioma_seleccionado = idioma_var.get()
    cuestionario = random.sample(preguntas_idiomas.get(idioma_seleccionado), k=cant_preguntas)
    ventana_seleccion.destroy()
    # print(idioma_seleccionado)
    if idioma_seleccionado is not None:
        preguntas_idioma = preguntas_idiomas.get(idioma_seleccionado)
        if preguntas_idioma is not None:
            iniciar_interfaz(cuestionario)


def iniciar_interfaz(df):
    global window

    def next_card(eleccion):
        global carta_actual, correctas, botones_habilitados#, rta_user

        carta_actual = random.choice(df)
        opciones = carta_actual['opciones'].split("\r\n")
        respuestas = carta_actual['respuesta'].split("\r\n")
        boton_conocido.grid_forget()
        boton_desconocido.grid_forget()
        boton_turn.grid(column=2, row=5)

        a_opt.grid(column=0, row=4)
        b_opt.grid(column=1, row=4)
        c_opt.grid(column=2, row=4)
        d_opt.grid(column=3, row=4)
        if len(opciones) == 5:
            e_opt.grid(column=4, row=4)

        tiempo_de_giro = window.after(83076, func=flip_card)
        window.after_cancel(tiempo_de_giro)

        canvas.itemconfig(card_question, text=carta_actual['pregunta'], fill='black')
        canvas.itemconfig(card_options, text=carta_actual['opciones'])
        canvas.itemconfig(card_answer, text='')
        canvas.itemconfig(card_argument, text='')
        canvas.itemconfig(card_reference, text='')
        canvas.itemconfig(card_background, image=flashcard_img_front)

    def flip_card():
        global rta_user, correctas
        opciones = carta_actual['opciones'].split("\r\n")
        respuestas = carta_actual['respuesta'].split("\r\n")
        boton_conocido.grid(column=1, row=4)
        boton_desconocido.grid(column=3, row=4)
        boton_turn.grid_forget()
        a_opt.grid_forget()
        b_opt.grid_forget()
        c_opt.grid_forget()
        d_opt.grid_forget()
        if e_opt:
            e_opt.grid_forget()

        canvas.itemconfig(card_question, text=carta_actual['pregunta'], fill='white')
        canvas.itemconfig(card_options, text='')
        canvas.itemconfig(card_answer, text=carta_actual["respuesta"], fill='white')
        canvas.itemconfig(card_argument, text=carta_actual["argumento"], fill='white')
        canvas.itemconfig(card_reference, text=carta_actual["referencia"], fill='white')
        pyperclip.copy(carta_actual["referencia"])
        canvas.itemconfig(card_background, image=flashcard_img_back)

        if len(rta_user) > 0:
            if len(opciones) == 4:
                if rta_user[0] in respuestas:
                    correctas += 1
            elif len(opciones) == 5:
                if rta_user[0] in respuestas:
                    if rta_user[1] in respuestas:
                        correctas += 1
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()
        rta_user = []
        df.remove(carta_actual)
        if not df:
            mostrar_resumen()
            return

    def user_opt(respuesta):
        global rta_user
        if respuesta in rta_user:
            rta_user.remove(respuesta)
        else:
            rta_user.append(respuesta)
        return rta_user

    window = Tk()
    window.title("AWS Flash cards")
    window.config(pady=20, padx=20, bg=BACKGROUND_COLOR2)

    canvas = Canvas(width=720, height=480, bg=BACKGROUND_COLOR2, highlightthickness=0)
    flashcard_img_front = PhotoImage(file="images/Component 2.png")
    flashcard_img_back = PhotoImage(file="images/Component 1.png")
    card_background = canvas.create_image(360, 240, image=flashcard_img_front)
    card_background = canvas.create_image(360, 240, image=flashcard_img_back)

    card_question = canvas.create_text(360, 100, text='', font=("Ariel", 10, "bold"), justify='center', width=600)
    card_options = canvas.create_text(360, 300, text='', font=("Ariel", 12, "normal"), justify='center', width=600)
    card_answer = canvas.create_text(360, 200, text='', font=("Ariel", 10, "normal"), justify='center', width=600)
    card_argument = canvas.create_text(360, 300, text='', font=("Ariel", 8, "normal"), justify='center', width=600)
    card_reference = canvas.create_text(360, 380, text='', font=("Ariel", 8, "normal"), justify='center', width=500)

    canvas.grid(column=0, row=0, columnspan=5, rowspan=4)

    wrong_img = PhotoImage(file="images/wrong.png")
    boton_desconocido = Button(image=wrong_img, bg=BACKGROUND_COLOR2, highlightthickness=0, command=lambda: next_card('desconocidas'))

    right_img = PhotoImage(file="images/right.png")
    boton_conocido = Button(image=right_img, bg=BACKGROUND_COLOR2, highlightthickness=0, command=lambda: next_card('conocidas'))

    turn_card_img = PhotoImage(file='images/turn_arrow_.png')
    boton_turn = Button(image=turn_card_img, bg=BACKGROUND_COLOR2, highlightthickness=0, command=lambda: flip_card())

    a_opt = Button(text='A', bg=BACKGROUND_COLOR2, highlightthickness=0, width=5, height=2, command=lambda: user_opt(carta_actual['opciones'].split("\r\n")[0]))
    b_opt = Button(text='B', bg=BACKGROUND_COLOR2, highlightthickness=0, width=5, height=2, command=lambda: user_opt(carta_actual['opciones'].split("\r\n")[1]))
    c_opt = Button(text='C', bg=BACKGROUND_COLOR2, highlightthickness=0, width=5, height=2, command=lambda: user_opt(carta_actual['opciones'].split("\r\n")[2]))
    d_opt = Button(text='D', bg=BACKGROUND_COLOR2, highlightthickness=0, width=5, height=2, command=lambda: user_opt(carta_actual['opciones'].split("\r\n")[3]))
    e_opt = Button(text='E', bg=BACKGROUND_COLOR2, highlightthickness=0, width=5, height=2, command=lambda: user_opt(carta_actual['opciones'].split("\r\n")[4]))
    next_card('desconocidas')

    window.mainloop()


ventana_seleccion = tk.Tk()
ventana_seleccion.title("Selección de Idioma")

style = ttk.Style()
style.configure("TButton", background=BACKGROUND_COLOR2)
style.map("TButton", background=[('active', BACKGROUND_COLOR2)])

ventana_seleccion.configure(bg=BACKGROUND_COLOR2)
etiqueta_instrucciones = tk.Label(ventana_seleccion, text="Selecciona tu idioma:", bg=BACKGROUND_COLOR2, width=39)
etiqueta_instrucciones.pack()

idioma_var = tk.StringVar()

espanol_btn = ttk.Radiobutton(ventana_seleccion, text="Español", variable=idioma_var, value='español', style="TButton")
ingles_btn = ttk.Radiobutton(ventana_seleccion, text="Inglés", variable=idioma_var, value='inglés', style="TButton")
aleman_btn = ttk.Radiobutton(ventana_seleccion, text="Alemán", variable=idioma_var, value='alemán', style="TButton")
frances_btn = ttk.Radiobutton(ventana_seleccion, text="Francés", variable=idioma_var, value='francés', style="TButton")
italiano_btn = ttk.Radiobutton(ventana_seleccion, text="Italiano", variable=idioma_var, value='italiano', style="TButton")
portugues_btn = ttk.Radiobutton(ventana_seleccion, text="Portugués", variable=idioma_var, value='portugués', style="TButton")

espanol_btn.pack()
ingles_btn.pack()
aleman_btn.pack()
frances_btn.pack()
italiano_btn.pack()
portugues_btn.pack()

continuar_btn = tk.Button(ventana_seleccion, text="Continuar", command=iniciar_programa, bg=BACKGROUND_COLOR2)
continuar_btn.pack()

ventana_seleccion.mainloop()
