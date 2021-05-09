from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# variables
estado = 1

def create_main_window():
    global root
    root = Tk()
    root.title("Resistor")
    root.resizable(0, 0)
    ancho_ventana = 550
    alto_ventana = 320
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.config(bg='#000')

    # ventana principal
    image_zero = Image.open(
        'imagenes/titulo.png')
    image_zero = image_zero.resize((300, 80), Image.ANTIALIAS)
    my_img_zero = ImageTk.PhotoImage(image_zero)
    Label(root, image=my_img_zero, font=('8514oem', 15),
          bg='#000000', fg='#ffffff').place(x=130, y=20)

    image = Image.open(
        'imagenes/boton_valor.png')
    image = image.resize((270, 40), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    Button(root, image=my_img, bd=0, padx=50, cursor='target',
           command=valor_resistencia).place(x=146, y=210)

    image_eq = Image.open(
        'imagenes/eq.png')
    image_eq = image_eq.resize((200, 40), Image.ANTIALIAS)
    my_img_eq = ImageTk.PhotoImage(image_eq)
    Button(root, image=my_img_eq, bd=0, cursor='target',
           command=equivalente).place(x=180, y=255)

    image_three = Image.open(
        'imagenes/leds_calculator.png')
    image_three = image_three.resize((300, 40), Image.ANTIALIAS)
    my_img_three = ImageTk.PhotoImage(image_three)
    Button(root, image=my_img_three, bd=0, cursor='target',
           command=calculadora_led).place(x=132, y=120)

    image_four = Image.open(
        'imagenes/voltage_divider.png')
    image_four = image_four.resize((300, 40), Image.ANTIALIAS)
    my_img_four = ImageTk.PhotoImage(image_four)
    Button(root, image=my_img_four, bd=0, cursor='target',
           command=divisor_tension).place(x=132, y=165)
    root.mainloop()

def valor_resistencia():
    root.destroy()
    bandas = ['black', 'brown', 'red', 'orange', 'yellow',
              'green', 'blue', 'purple', 'grey', 'white']
    bandas_error = ['brown', 'red', 'green',
                    'blue', 'purple', 'gold', 'silver']
    root_two = Tk()
    root_two.title("Resistance's value")
    root_two.config(padx=5, pady=5, bg='#000')
    root_two.resizable(0, 0)
    ancho_ventana = 700
    alto_ventana = 460
    x_ventana = root_two.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root_two.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root_two.geometry(posicion)

    messagebox.showinfo(
        'How to use', '1. Select the type of resistor\n2. Choose the color of each band\n3. Press the compute button')

    def cambio(numero):
        if estado == 1:
            if numero == 1:
                label_one.config(bg=clicked_primera_banda.get())
            elif numero == 2:
                label_two.config(bg=clicked_segunda_banda.get())
            elif numero == 3:
                label_three.config(bg=clicked_tercera_banda.get())
            elif numero == 4:
                label_five.config(bg=clicked_cuarta_banda.get())
            elif numero == 5:
                label_four.config(bg=clicked_quinta_banda.get())
        elif estado == 0:
            if numero == 1:
                label_one.config(bg=clicked_primera_banda.get())
            elif numero == 2:
                label_two.config(bg=clicked_segunda_banda.get())
            elif numero == 3:
                label_three.config(bg=clicked_tercera_banda.get())
            elif numero == 4:
                label_four.config(bg=clicked_cuarta_banda.get())

    def cuatro_bandas():
        global estado
        estado = 0
        boton_cuatro_bandas.config(cursor='X_cursor')
        boton_cinco_bandas.config(cursor='hand1')
        cuarta_banda = OptionMenu(
            datos_cuatro, clicked_cuarta_banda, *bandas_error, command=lambda numero: cambio(4))
        cuarta_banda.grid(row=3, column=1)
        cuarta_banda.config(width=20, height=1, bg='#000', fg='#fff')
        label_one.config(bg='black')
        label_two.config(bg='black')
        label_three.config(bg='black')
        label_four.config(bg='black')
        clicked_primera_banda.set('black')
        clicked_segunda_banda.set('black')
        clicked_tercera_banda.set('black')
        clicked_cuarta_banda.set('black')
        root_two.geometry('700x430')
        boton_cinco_bandas.config(state=NORMAL)
        boton_cuatro_bandas.config(state=DISABLED)
        quinta_banda.grid_forget()
        label_five.place_forget()
        label_quinto.grid_forget()

    def cinco_bandas():
        global estado
        estado = 1
        boton_cinco_bandas.config(cursor='X_cursor')
        boton_cuatro_bandas.config(cursor='hand1')
        cuarta_banda = OptionMenu(
            datos_cuatro, clicked_cuarta_banda, *bandas, command=lambda numero: cambio(4))
        cuarta_banda.grid(row=3, column=1)
        cuarta_banda.config(width=20, height=1, bg='#000', fg='#fff')
        label_one.config(bg='black')
        label_two.config(bg='black')
        label_three.config(bg='black')
        label_four.config(bg='black')
        label_five.config(bg='black')
        clicked_primera_banda.set('black')
        clicked_segunda_banda.set('black')
        clicked_tercera_banda.set('black')
        clicked_cuarta_banda.set('black')
        clicked_quinta_banda.set('black')
        root_two.geometry('700x460')
        boton_cuatro_bandas.config(state=NORMAL)
        boton_cinco_bandas.config(state=DISABLED)
        quinta_banda.grid(row=4, column=1)
        quinta_banda.config(width=20, height=1)
        label_five.place(x=376, y=74)
        label_quinto.grid(row=4, column=0)

    def calcular():
        global valor
        if clicked_primera_banda.get() == 'black':
            valor = 0
        elif clicked_primera_banda.get() == 'brown':
            valor = 1
        elif clicked_primera_banda.get() == 'red':
            valor = 2
        elif clicked_primera_banda.get() == 'orange':
            valor = 3
        elif clicked_primera_banda.get() == 'yellow':
            valor = 4
        elif clicked_primera_banda.get() == 'green':
            valor = 5
        elif clicked_primera_banda.get() == 'blue':
            valor = 6
        elif clicked_primera_banda.get() == 'purple':
            valor = 7
        elif clicked_primera_banda.get() == 'grey':
            valor = 8
        elif clicked_primera_banda.get() == 'white':
            valor = 9

        if clicked_segunda_banda.get() == 'black':
            valor = valor*10 + 0
        elif clicked_segunda_banda.get() == 'brown':
            valor = valor*10 + 1
        elif clicked_segunda_banda.get() == 'red':
            valor = valor*10 + 2
        elif clicked_segunda_banda.get() == 'orange':
            valor = valor*10 + 3
        elif clicked_segunda_banda.get() == 'yellow':
            valor = valor*10 + 4
        elif clicked_segunda_banda.get() == 'green':
            valor = valor*10 + 5
        elif clicked_segunda_banda.get() == 'blue':
            valor = valor*10 + 6
        elif clicked_segunda_banda.get() == 'purple':
            valor = valor*10 + 7
        elif clicked_segunda_banda.get() == 'grey':
            valor = valor*10 + 8
        elif clicked_segunda_banda.get() == 'white':
            valor = valor*10 + 9

        if estado == 1:
            if clicked_tercera_banda.get() == 'black':
                valor = valor*10 + 0
            elif clicked_tercera_banda.get() == 'brown':
                valor = valor*10 + 1
            elif clicked_tercera_banda.get() == 'red':
                valor = valor*10 + 2
            elif clicked_tercera_banda.get() == 'orange':
                valor = valor*10 + 3
            elif clicked_tercera_banda.get() == 'yellow':
                valor = valor*10 + 4
            elif clicked_tercera_banda.get() == 'green':
                valor = valor*10 + 5
            elif clicked_tercera_banda.get() == 'blue':
                valor = valor*10 + 6
            elif clicked_tercera_banda.get() == 'purple':
                valor = valor*10 + 7
            elif clicked_tercera_banda.get() == 'grey':
                valor = valor*10 + 8
            elif clicked_tercera_banda.get() == 'white':
                valor = valor*10 + 9

            if clicked_cuarta_banda.get() == 'black':
                valor = valor*1
            elif clicked_cuarta_banda.get() == 'brown':
                valor = valor*10
            elif clicked_cuarta_banda.get() == 'red':
                valor = valor*100
            elif clicked_cuarta_banda.get() == 'orange':
                valor = valor*1000
            elif clicked_cuarta_banda.get() == 'yellow':
                valor = valor*10000
            elif clicked_cuarta_banda.get() == 'green':
                valor = valor*100000
            elif clicked_cuarta_banda.get() == 'blue':
                valor = valor*1000000
            elif clicked_cuarta_banda.get() == 'purple':
                valor = valor*10000000
            elif clicked_cuarta_banda.get() == 'grey':
                valor = valor*100000000
            elif clicked_cuarta_banda.get() == 'white':
                valor = valor*1000000000

            if clicked_quinta_banda.get() == 'brown':
                valor = str(valor) + ' +/- 1%'
            elif clicked_quinta_banda.get() == 'red':
                valor = str(valor) + ' +/- 2%'
            elif clicked_quinta_banda.get() == 'green':
                valor = str(valor) + ' +/- 0.5%'
            elif clicked_quinta_banda.get() == 'blue':
                valor = str(valor) + ' +/- 0.25%'
            elif clicked_quinta_banda.get() == 'purple':
                valor = str(valor) + ' +/- 0.1%'
            elif clicked_quinta_banda.get() == 'gold':
                valor = str(valor) + ' +/- 5%'
            elif clicked_quinta_banda.get() == 'silver':
                valor = str(valor) + ' +/- 10%'
        elif estado == 0:
            if clicked_tercera_banda.get() == 'black':
                valor = valor*1
            elif clicked_tercera_banda.get() == 'brown':
                valor = valor*10
            elif clicked_tercera_banda.get() == 'red':
                valor = valor*100
            elif clicked_tercera_banda.get() == 'orange':
                valor = valor*1000
            elif clicked_tercera_banda.get() == 'yellow':
                valor = valor*10000
            elif clicked_tercera_banda.get() == 'green':
                valor = valor*100000
            elif clicked_tercera_banda.get() == 'blue':
                valor = valor*1000000
            elif clicked_tercera_banda.get() == 'purple':
                valor = valor*10000000
            elif clicked_tercera_banda.get() == 'grey':
                valor = valor*100000000
            elif clicked_tercera_banda.get() == 'white':
                valor = valor*1000000000

            if clicked_cuarta_banda.get() == 'brown':
                valor = str(valor) + ' +/- 1%'
            elif clicked_cuarta_banda.get() == 'red':
                valor = str(valor) + ' +/- 2%'
            elif clicked_cuarta_banda.get() == 'green':
                valor = str(valor) + ' +/- 0.5%'
            elif clicked_cuarta_banda.get() == 'blue':
                valor = str(valor) + ' +/- 0.25%'
            elif clicked_cuarta_banda.get() == 'purple':
                valor = str(valor) + ' +/- 0.1%'
            elif clicked_cuarta_banda.get() == 'gold':
                valor = str(valor) + ' +/- 5%'
            elif clicked_cuarta_banda.get() == 'silver':
                valor = str(valor) + ' +/- 10%'
        if (estado == 0 and clicked_primera_banda.get() == 'black' and clicked_segunda_banda.get() == 'black' and clicked_tercera_banda.get() == 'black') or (estado == 1 and clicked_primera_banda.get() == 'black' and clicked_segunda_banda.get() == 'black' and clicked_tercera_banda.get() == 'black' and clicked_cuarta_banda.get() == 'black'):
            messagebox.showwarning('Warning', 'please, put some values')
        else:
            messagebox.showinfo(
                'Result', 'the value of your resistor is: '+str(valor)+' Ohms (\u03A9)')
    botones = Frame(master=root_two)
    botones.pack()

    image_four = Image.open(
        'imagenes/4_bandas.png')
    image_four = image_four.resize((340, 38), Image.ANTIALIAS)
    my_img_four = ImageTk.PhotoImage(image_four)
    boton_cuatro_bandas = Button(
        botones, image=my_img_four, bd=0, cursor='hand1', command=cuatro_bandas)
    boton_cuatro_bandas.pack(side=LEFT)
    image_five = Image.open(
        'imagenes/5_bandas.png')
    image_five = image_five.resize((340, 38), Image.ANTIALIAS)
    my_img_five = ImageTk.PhotoImage(image_five)
    boton_cinco_bandas = Button(
        botones, image=my_img_five, state=DISABLED, bd=0, cursor='X_cursor', command=cinco_bandas)
    boton_cinco_bandas.pack(side=RIGHT)

    background = PhotoImage(
        file='imagenes/imagen_de_resistencia.png', master=root_two)
    fondo = Label(master=root_two, image=background, bg='#000')
    fondo.pack()
    fondo.image = background

    # Frame principal
    ancho = 20
    alto = 1

    datos_cuatro = Frame(master=root_two)
    datos_cuatro.pack()
    datos_cuatro.config(bg='#000')

    Label(datos_cuatro, text="Primera banda: ", width=ancho,
          height=alto, bg='#000', fg='#fff').grid(row=0, column=0)
    Label(datos_cuatro, text="Segunda banda: ", width=ancho,
          height=alto, bg='#000', fg='#fff').grid(row=1, column=0)
    Label(datos_cuatro, text="Tercera banda: ", width=ancho,
          height=alto, bg='#000', fg='#fff').grid(row=2, column=0)
    Label(datos_cuatro, text="Cuarta banda: ", width=ancho,
          height=alto, bg='#000', fg='#fff').grid(row=3, column=0)
    label_quinto = Label(datos_cuatro, text="Quinta banda: ",
                         width=ancho, height=alto, bg='#000', fg='#fff')
    label_quinto.grid(row=4, column=0)

    clicked_primera_banda = StringVar(root_two, value='black')
    clicked_segunda_banda = StringVar(root_two, value='black')
    clicked_tercera_banda = StringVar(root_two, value='black')
    clicked_cuarta_banda = StringVar(root_two, value='black')
    clicked_quinta_banda = StringVar(root_two, value='black')

    label_one = Label(root_two, padx=14, relief=RIDGE,
                      pady=52, bg=clicked_primera_banda.get())
    label_one.place(x=238, y=74)
    label_two = Label(root_two, padx=14, relief=RIDGE,
                      pady=52, bg=clicked_segunda_banda.get())
    label_two.place(x=284, y=74)
    label_three = Label(root_two, padx=14, relief=RIDGE,
                        pady=52, bg=clicked_tercera_banda.get())
    label_three.place(x=330, y=74)
    label_four = Label(root_two, padx=14, relief=RIDGE,
                       pady=52, bg=clicked_cuarta_banda.get())
    label_four.place(x=417, y=74)
    label_five = Label(root_two, padx=14, relief=RIDGE,
                       pady=52, bg=clicked_quinta_banda.get())
    label_five.place(x=376, y=74)

    primera_banda = OptionMenu(
        datos_cuatro, clicked_primera_banda, *bandas, command=lambda numero: cambio(1))
    primera_banda.grid(row=0, column=1)
    segunda_banda = OptionMenu(
        datos_cuatro, clicked_segunda_banda, *bandas, command=lambda numero: cambio(2))
    segunda_banda.grid(row=1, column=1)
    tercera_banda = OptionMenu(
        datos_cuatro, clicked_tercera_banda, *bandas, command=lambda numero: cambio(3))
    tercera_banda.grid(row=2, column=1)
    if estado == 1:
        cuarta_banda = OptionMenu(
            datos_cuatro, clicked_cuarta_banda, *bandas, command=lambda numero: cambio(4))
        cuarta_banda.grid(row=3, column=1)
        global quinta_banda
        quinta_banda = OptionMenu(
            datos_cuatro, clicked_quinta_banda, *bandas_error, command=lambda numero: cambio(5))
        quinta_banda.grid(row=4, column=1)
    elif estado == 0:
        quinta_banda.grid_forget()

    primera_banda.config(width=ancho, height=alto, bg='#000', fg='#fff')
    segunda_banda.config(width=ancho, height=alto, bg='#000', fg='#fff')
    tercera_banda.config(width=ancho, height=alto, bg='#000', fg='#fff')
    cuarta_banda.config(width=ancho, height=alto, bg='#000', fg='#fff')
    quinta_banda.config(width=ancho, height=alto, bg='#000', fg='#fff')

    image_compute = Image.open(
        'imagenes/compute.png')
    image_compute = image_compute.resize((270, 40), Image.ANTIALIAS)
    my_img_compute = ImageTk.PhotoImage(image_compute)
    Button(root_two, image=my_img_compute, cursor='target',
           command=calcular).pack(side=BOTTOM)

    root_two.mainloop()

def calculadora_led():
    colores = ['Red (1.63)', 'Orange (2.03v)', 'Yellow (2.1v)',
               'Blue (2.48v)', 'Green (1.9v)', 'Violet (2.76v)', 'UV (3.1v)', 'White (3.5v)']
    root.destroy()
    root_three = Tk()
    root_three.title("Calculator of resistance")
    root_three.config(padx=5, pady=5, bg='#000')
    root_three.resizable(0, 0)
    ancho_ventana = 400
    alto_ventana = 320
    x_ventana = root_three.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root_three.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root_three.geometry(posicion)

    check_buttons = Frame(root_three)
    check_buttons.pack()

    serie_check = IntVar(root_three, value=1)
    parallel_check = IntVar(root_three, value=0)

    def serie_clicked():
        serie_check.set(1)
        parallel_check.set(0)
        serie.config(cursor='X_cursor', state=DISABLED)
        paralelo.config(cursor='hand1', state=NORMAL)

    def parallel_clicked():
        parallel_check.set(1)
        serie_check.set(0)
        paralelo.config(cursor='X_cursor', state=DISABLED)
        serie.config(cursor='hand1', state=NORMAL)

    def compute():
        if source_entry.get() == '' or source_entry.get().isdigit() == False or int(source_entry.get()) <= 0:
            messagebox.showerror(
                'Invalid voltage', 'please put a correct voltage value')
            source_entry.delete(0, END)
        if current_entry.get() == '' or current_entry.get().isdigit() == False or int(current_entry.get()) <= 0:
            messagebox.showerror(
                'Invalid voltage', 'please put a correct current value')
            current_entry.delete(0, END)
        if number_elements.get() == '' or number_elements.get().isdigit() == False or int(number_elements.get()) <= 0:
            messagebox.showerror(
                'Invalid voltage', 'please put a correct amount of LEDs')
            number_elements.delete(0, END)
        else:
            if serie_check.get() == 1:
                seleccionado = clicked_menu.get().split('(')
                seleccionado_one = seleccionado[1].split('v')
                print(seleccionado_one)
                voltaje_necesario = round(
                    float(seleccionado_one[0])*int(number_elements.get()), 2)
                if int(current_entry.get()) < 20:
                    messagebox.showwarning(
                        'Insufficient', 'Your source must provide more than 20mA')
                if int(current_entry.get()) > 25:
                    messagebox.showwarning(
                        'Exceeded', 'Your source must provide less than 25mA')
                if int(source_entry.get()) < float(voltaje_necesario):
                    messagebox.showwarning(
                        'Insufficient', 'Your voltage source must provide more than {}v'.format(voltaje_necesario))
                if int(current_entry.get()) >= 20 and int(current_entry.get()) <= 25 and int(source_entry.get()) >= voltaje_necesario:
                    resistencia = round(
                        (int(source_entry.get())-voltaje_necesario)/(0.001*int(current_entry.get())), 2)
                    messagebox.showinfo(
                        'Result', 'Your LEDs need a {} \u03A9 resistor'.format(str(resistencia)))
            else:
                seleccionado = clicked_menu.get().split('(')
                seleccionado_one = seleccionado[1].split('v')
                corriente_necesaria = 20*int(number_elements.get())
                print(number_elements.get())
                if int(current_entry.get()) < corriente_necesaria:
                    messagebox.showwarning('Insufficient', 'Your source must provide more than {}mA'.format(
                        str(corriente_necesaria)))
                if int(current_entry.get()) > corriente_necesaria+(5*int(number_elements.get())):
                    messagebox.showwarning('Exceeded', 'Your source must provide less than {}mA'.format(
                        str(corriente_necesaria+(5*int(number_elements.get())))))
                if int(source_entry.get()) < float(seleccionado_one[0]):
                    messagebox.showwarning(
                        'Insufficient', 'Your voltage source must provide more than {}v'.format(seleccionado_one[0]))
                if int(current_entry.get()) > corriente_necesaria and int(current_entry.get()) <= corriente_necesaria+(5*int(number_elements.get())) and int(source_entry.get()) >= float(seleccionado_one[0]):
                    print(source_entry.get())
                    print(seleccionado_one[0])
                    print(corriente_necesaria)
                    resistencia = round(
                        (int(source_entry.get())-float(seleccionado_one[0]))/(0.001*corriente_necesaria), 2)
                    messagebox.showinfo(
                        'Result', 'Your LEDs need a {} \u03A9 resistor'.format(str(resistencia)))

    check_buttons_two = Frame(root_three)
    check_buttons_two.config(bd=1, bg='#000')
    check_buttons_two.pack()

    source = Frame(root_three, bg='#000')
    source.place(x=104, y=60)

    current = Frame(root_three, bg='#000')
    current.place(x=100, y=105)

    data = Frame(root_three, bg='#000')
    data.place(x=118, y=150)

    datos = Frame(root_three, bg='#000')
    datos.place(x=130, y=205)

    image_s = Image.open(
        'imagenes/series.png')
    image_s = image_s.resize((120, 37), Image.ANTIALIAS)
    my_img_s = ImageTk.PhotoImage(image_s)
    serie = Checkbutton(check_buttons_two, image=my_img_s, bg='#000', cursor='X_cursor',
                        state=DISABLED, variable=serie_check, command=serie_clicked)
    serie.grid(row=0, column=0)
    image_p = Image.open(
        'imagenes/parallel.png')
    image_p = image_p.resize((160, 38), Image.ANTIALIAS)
    my_img_p = ImageTk.PhotoImage(image_p)
    paralelo = Checkbutton(check_buttons_two, image=my_img_p, bg='#000',
                           cursor='hand1', variable=parallel_check, command=parallel_clicked)
    paralelo.grid(row=0, column=2)

    color = Label(data, text='Pick the color of the LEDs',
                  bg='#000', fg='#fff')
    color.grid(row=0, column=1)

    label_one = Label(datos, text='Amount of leds (1-100)',
                      bg='#000', fg='#fff')
    number_elements = Entry(datos)
    number_elements.config(justify=CENTER)
    image_in = Image.open(
        'imagenes/compute.png')
    image_in = image_in.resize((110, 25), Image.ANTIALIAS)
    my_img_in = ImageTk.PhotoImage(image_in)
    compute = Button(root_three, bd=1, image=my_img_in, command=compute)

    label_one.pack()
    number_elements.pack()
    compute.place(x=136, y=263)

    source_label = Label(
        source, text='Insert the voltage of the source (V)', bg='#000', fg='#fff')
    source_label.pack()
    source_entry = Entry(source)
    source_entry.config(justify=CENTER)
    source_entry.pack()

    current_label = Label(
        current, text='Insert the current of the source (mA)', bg='#000', fg='#fff')
    current_label.pack()
    current_entry = Entry(current)
    current_entry.config(justify=CENTER)
    current_entry.pack()

    clicked_menu = StringVar(root_three, value='Red (1.63v)')
    color_leds = OptionMenu(data, clicked_menu, *colores)
    color_leds.config(width=19)
    color_leds.grid(row=1, column=1)

    root_three.mainloop()

def equivalente():
    messagebox.showinfo('How to use', '1. Select the element\n2. Select the type of circuit\n3. Enter the amount of elements\n4. Press the insert button\n5. Enter the value of each element\n6. Press the insert value button\n7. Press the compute button')
    root.destroy()
    root_three = Tk()
    root_three.title("Equivalent")
    root_three.config(padx=5, pady=5, bg='#000')
    root_three.resizable(0, 0)
    ancho_ventana = 720
    alto_ventana = 380
    x_ventana = root_three.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root_three.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root_three.geometry(posicion)

    def resistor_clicked():
        capacitor_check.set(0)
        inductor_check.set(0)
        resistor_check.set(1)
        resistor.config(cursor='X_cursor', state=DISABLED)
        capacitor.config(cursor='hand1', state=NORMAL)
        inductor.config(cursor='hand1', state=NORMAL)

    def capacitor_clicked():
        capacitor_check.set(1)
        inductor_check.set(0)
        resistor_check.set(0)
        capacitor.config(cursor='X_cursor', state=DISABLED)
        resistor.config(cursor='hand1', state=NORMAL)
        inductor.config(cursor='hand1', state=NORMAL)

    def inductor_clicked():
        capacitor_check.set(0)
        inductor_check.set(1)
        resistor_check.set(0)
        inductor.config(cursor='X_cursor', state=DISABLED)
        capacitor.config(cursor='hand1', state=NORMAL)
        resistor.config(cursor='hand1', state=NORMAL)

    def serie_clicked():
        serie_check.set(1)
        parallel_check.set(0)
        serie.config(cursor='X_cursor', state=DISABLED)
        paralelo.config(cursor='hand1', state=NORMAL)

    def parallel_clicked():
        parallel_check.set(1)
        serie_check.set(0)
        paralelo.config(cursor='X_cursor', state=DISABLED)
        serie.config(cursor='hand1', state=NORMAL)

    def insertar():
        def insertar_valor():
            lista.insert(END, 'element #'+str(contador.get())+': '+valor.get())
            valores['text'] = 'Value of element {}: '.format(
                str(int(int(contador.get())+1)))
            contador.set(str(int(contador.get()) + 1))
            delete_button.config(cursor='hand1', state=NORMAL)
            if contador.get() == str(cantidad+1):
                messagebox.showinfo(
                    'Limit reached', 'You have inserted all the values')
                boton_ingresar.config(state=DISABLED)
                valor.config(state=DISABLED)
                boton_calcular.config(state=NORMAL)

        if number_elements.get() == "":
            messagebox.showwarning('Invalid amount', 'Please put some value')
        elif int(number_elements.get()) < 1 or int(number_elements.get()) > 100:
            messagebox.showerror(
                'Crossed Limits', 'You cannot exceed the limits')
        else:
            cantidad = int(number_elements.get())
            number_elements.config(state=DISABLED)
            insertar.config(state=DISABLED)
            valor = Entry(root_three)
            valor.config(justify=CENTER)
            valor.place(x=75, y=273)
            valores = Label(root_three, text='Value of element {}: '.format(
                contador.get()), bg='#000', fg='#fff')
            valores.place(x=80, y=250)
            image_v = Image.open(
                'imagenes/insert_value.png')
            image_v = image_v.resize((110, 20), Image.ANTIALIAS)
            my_img_v = ImageTk.PhotoImage(image_v)
            boton_ingresar = Button(
                root_three, image=my_img_v, bd=1, command=lambda: insertar_valor())
            boton_ingresar.image = my_img_v
            boton_ingresar.place(x=80, y=297)
        number_elements.delete(0, END)

    def compute():
        datos = [elemento for elemento in lista.get(0, END)]
        datos_two = [elemento[elemento.find(':')+2:] for elemento in datos]
        resultado = 0
        if serie_check.get() == 1:
            if resistor_check.get() == 1 or inductor_check.get() == 1:
                for elemento in datos_two:
                    resultado += int(elemento)
            elif capacitor_check.get() == 1:
                for elemento in datos_two:
                    resultado += 1/int(elemento)
                resultado = 1/resultado
        else:
            if resistor_check.get() == 1 or inductor_check.get() == 1:
                for elemento in datos_two:
                    resultado += 1/int(elemento)
                resultado = 1/resultado
            elif capacitor_check.get() == 1:
                for elemento in datos_two:
                    resultado += int(elemento)
        if resistor_check.get() == 1:
            messagebox.showinfo(
                'Result', 'Your equivalent resistance is: '+str(resultado)+' Ohms (\u03A9)')
        elif capacitor_check.get() == 1:
            messagebox.showinfo(
                'Result', 'Your equivalent capacitance is: '+str(resultado)+' MicroFarads uF')
        elif inductor_check.get() == 1:
            messagebox.showinfo(
                'Result', 'Your equivalent inductance is: '+str(resultado)+' Henrios H')

    contador = StringVar(root_three, value='1')
    serie_check = IntVar(root_three, value=1)
    parallel_check = IntVar(root_three, value=0)
    resistor_check = IntVar(root_three, value=1)
    capacitor_check = IntVar(root_three, value=0)
    inductor_check = IntVar(root_three, value=0)

    # primeros checkboxes
    check_buttons_one = Frame(root_three)
    check_buttons_one.config(bd=10, bg='#000')
    check_buttons_one.pack()

    image_r = Image.open(
        'imagenes/resistance.png')
    image_r = image_r.resize((200, 35), Image.ANTIALIAS)
    my_img_r = ImageTk.PhotoImage(image_r)
    resistor = Checkbutton(check_buttons_one, image=my_img_r, bg='#000', state=DISABLED,
                           cursor='X_cursor', variable=resistor_check, command=resistor_clicked)
    resistor.grid(row=0, column=0)
    image_c = Image.open(
        'imagenes/capacitance.png')
    image_c = image_c.resize((200, 43), Image.ANTIALIAS)
    my_img_c = ImageTk.PhotoImage(image_c)
    capacitor = Checkbutton(check_buttons_one, image=my_img_c, bg='#000',
                            cursor='hand1', variable=capacitor_check, command=capacitor_clicked)
    capacitor.grid(row=0, column=1)
    image_i = Image.open(
        'imagenes/inductance.png')
    image_i = image_i.resize((200, 35), Image.ANTIALIAS)
    my_img_i = ImageTk.PhotoImage(image_i)
    inductor = Checkbutton(check_buttons_one, image=my_img_i, bg='#000',
                           cursor='hand1', variable=inductor_check, command=inductor_clicked)
    inductor.grid(row=0, column=2)

    # segundos checkboxes
    check_buttons_two = Frame(root_three)
    check_buttons_two.config(bd=1, bg='#000')
    check_buttons_two.pack()

    image_s = Image.open(
        'imagenes/series.png')
    image_s = image_s.resize((120, 37), Image.ANTIALIAS)
    my_img_s = ImageTk.PhotoImage(image_s)
    serie = Checkbutton(check_buttons_two, image=my_img_s, bg='#000', cursor='X_cursor',
                        state=DISABLED, variable=serie_check, command=serie_clicked)
    serie.grid(row=0, column=0)
    Label(check_buttons_two, text='         ', bg='#000').grid(row=0, column=1)
    image_p = Image.open(
        'imagenes/parallel.png')
    image_p = image_p.resize((160, 38), Image.ANTIALIAS)
    my_img_p = ImageTk.PhotoImage(image_p)
    paralelo = Checkbutton(check_buttons_two, image=my_img_p, bg='#000',
                           cursor='hand1', variable=parallel_check, command=parallel_clicked)
    paralelo.grid(row=0, column=2)

    label_one = Label(
        root_three, text='Number of elements (1-100)', bg='#000', fg='#fff')
    label_one.place(x=60, y=150)
    number_elements = Entry(root_three)
    number_elements.config(justify=CENTER)
    number_elements.place(x=75, y=173)
    image_in = Image.open(
        'imagenes/insert.png')
    image_in = image_in.resize((65, 20), Image.ANTIALIAS)
    my_img_in = ImageTk.PhotoImage(image_in)
    insertar = Button(root_three, bd=1, image=my_img_in, command=insertar)
    insertar.place(x=102, y=197)

    # muestreo de datos
    data_two = Frame(root_three)
    data_two.place(x=290, y=140)

    Label(data_two, text='Registred values', bg='#000', fg='#fff').grid(
        sticky=W+E, row=0, column=0, columnspan=2)
    scroll = Scrollbar(data_two, orient=VERTICAL)
    lista = Listbox(data_two, yscrollcommand=scroll.set)
    lista.grid(row=1, column=0)
    scroll.config(command=lista.yview)
    scroll.grid(sticky=N+S, row=1, column=1)

    image_delete = Image.open(
        'imagenes/delete.png')
    image_delete = image_delete.resize((90, 20), Image.ANTIALIAS)
    my_img_delete = ImageTk.PhotoImage(image_delete)
    delete_button = Button(root_three, image=my_img_delete, cursor='X_cursor',
                           state=DISABLED, command=lambda: lista.delete(ANCHOR))
    delete_button.place(x=312, y=330)

    # boton calcular
    image_compute = Image.open(
        'imagenes/compute.png')
    image_compute = image_compute.resize((100, 20), Image.ANTIALIAS)
    my_img_compute = ImageTk.PhotoImage(image_compute)
    boton_calcular = Button(root_three, image=my_img_compute,
                            cursor='hand1', command=compute, state=DISABLED)
    boton_calcular.place(x=525, y=220)
    root_three.mainloop()

def divisor_tension():
    messagebox.showinfo('How to use', '1. Insert the amount of resistors\n2. Insert the value of each resistor\n3. Select the resistor\n4. Press the select button\n5. Enter the value of the source')
    root.destroy()
    root_three = Tk()
    root_three.title("Voltage divider")
    root_three.config(padx=5, pady=5, bg='#000')
    root_three.resizable(0, 0)
    ancho_ventana = 300
    alto_ventana = 100
    x_ventana = root_three.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root_three.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root_three.geometry(posicion)


    def ingresar_fuente():
        if source_entry.get == '' or source_entry.get().isdigit() == False or int(source_entry.get()) <= 0:
            messagebox.showerror(
                'Invalid entry', 'Please insert correct values')
            source_entry.delete(0, END)
        else:
            ancho_ventana = 300
            alto_ventana = 350
            x_ventana = root_three.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = root_three.winfo_screenheight() // 2 - alto_ventana // 2
            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
                "+" + str(x_ventana) + "+" + str(y_ventana)
            root_three.geometry(posicion)
            label_one.place(x=60, y=10)
            number_elements.place(x=75, y=33)
            insertar.place(x=102, y=57)
            data_two.place(x=65, y=90)
            select_button.place(x=138, y=280)
            delete_button.place(x=65, y=280)
            source.place_forget()
            source_entry.place_forget()
            source_button.place_forget()

    def insertar():
        try:
            def insertar_valor():
                if valor.get().isdigit() and int(valor.get()) > 0:
                    lista.insert(END, 'element #' +
                                 str(contador.get())+': '+valor.get())
                    valores['text'] = 'Value of element {}: '.format(
                        str(int(int(contador.get())+1)))
                    contador.set(str(int(contador.get()) + 1))
                    delete_button.config(cursor='hand1', state=NORMAL)
                    if contador.get() == str(cantidad+1):
                        select_button.config(cursor='hand1')
                        messagebox.showinfo(
                            'Limit reached', 'You have inserted all the values')
                        boton_ingresar.config(state=DISABLED)
                        valor.config(state=DISABLED)
                        select_button.config(state=NORMAL)
                else:
                    messagebox.showerror(
                        'Invalid entry', 'Please insert correct values')
                    valor.delete(0, END)
            if number_elements.get() == "":
                messagebox.showwarning(
                    'Invalid amount', 'Please put some value')
            elif int(number_elements.get()) < 1 or int(number_elements.get()) > 100:
                messagebox.showerror(
                    'Crossed Limits', 'You cannot exceed the limits')
            else:
                ancho_ventana = 300
                alto_ventana = 420
                x_ventana = root_three.winfo_screenwidth() // 2 - ancho_ventana // 2
                y_ventana = root_three.winfo_screenheight() // 2 - alto_ventana // 2
                posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
                    "+" + str(x_ventana) + "+" + str(y_ventana)
                root_three.geometry(posicion)
                data_two.place(x=65, y=170)
                delete_button.place(x=65, y=360)
                select_button.place(x=138, y=360)
                cantidad = int(number_elements.get())
                number_elements.config(state=DISABLED)
                insertar.config(state=DISABLED)
                valor = Entry(root_three)
                valor.config(justify=CENTER)
                valor.place(x=75, y=112)
                valores = Label(root_three, text='Value of element {}: '.format(
                    contador.get()), bg='#000', fg='#fff')
                valores.place(x=80, y=90)
                image_v = Image.open(
                    'imagenes/insert_value.png')
                image_v = image_v.resize((110, 20), Image.ANTIALIAS)
                my_img_v = ImageTk.PhotoImage(image_v)
                boton_ingresar = Button(
                    root_three, image=my_img_v, bd=1, command=lambda: insertar_valor())
                boton_ingresar.image = my_img_v
                boton_ingresar.place(x=80, y=136)
            number_elements.delete(0, END)
        except ValueError:
            messagebox.showerror('Invalid entry', 'Please insert numbers')
            number_elements.delete(0, END)

    def select():
        datos = [elemento for elemento in lista.get(0, END)]
        datos_two = [int(elemento[elemento.find(':')+2:])
                     for elemento in datos]
        resultado = 0
        for elemento in datos_two:
            resultado += elemento
        seleccionado = lista.get(ANCHOR).split('#')
        seleccionado = seleccionado[1].split(':')
        resistencia = int(seleccionado[0])
        resis_valor = int(seleccionado[1])
        resultado = round((int(source_entry.get())*resis_valor)/resultado, 3)
        messagebox.showinfo('Result', 'The voltage over the the resistor {} is {}v'.format(
            resistencia, resultado))

    contador = StringVar(root_three, value='1')

    label_one = Label(
        root_three, text='Amount of resistors (1-100)', bg='#000', fg='#fff')
    number_elements = Entry(root_three)
    number_elements.config(justify=CENTER)
    image_in = Image.open(
        'imagenes/insert.png')
    image_in = image_in.resize((65, 20), Image.ANTIALIAS)
    my_img_in = ImageTk.PhotoImage(image_in)
    insertar = Button(root_three, bd=1, image=my_img_in, command=insertar)

    # muestreo de datos
    data_two = Frame(root_three)

    Label(data_two, text='Resistance values', bg='#000', fg='#fff').grid(
        sticky=W+E, row=0, column=0, columnspan=2)
    scroll = Scrollbar(data_two, orient=VERTICAL)
    lista = Listbox(data_two, yscrollcommand=scroll.set)
    lista.grid(row=1, column=0)
    scroll.config(command=lista.yview)
    scroll.grid(sticky=N+S, row=1, column=1)

    image_delete = Image.open(
        'imagenes/delete.png')
    image_delete = image_delete.resize((64, 20), Image.ANTIALIAS)
    my_img_delete = ImageTk.PhotoImage(image_delete)
    delete_button = Button(root_three, image=my_img_delete, cursor='X_cursor',
                           state=DISABLED, command=lambda: lista.delete(ANCHOR))

    image_select = Image.open(
        'imagenes/select.png')
    image_select = image_select.resize((64, 20), Image.ANTIALIAS)
    my_img_select = ImageTk.PhotoImage(image_select)
    select_button = Button(root_three, image=my_img_select,
                           cursor='X_cursor', state=DISABLED, command=select)

    source = Label(
        root_three, text='Insert the value of your voltage source', bg='#000', fg='#fff')
    source.place(x=45, y=5)
    source_entry = Entry(root_three)
    source_entry.config(justify=CENTER)
    source_entry.place(x=85, y=26)
    source_button = Button(root_three, image=my_img_in,
                           bd=1, cursor='hand1', command=ingresar_fuente)
    source_button.place(x=113, y=48)

    root_three.mainloop()

if __name__ == "__main__":
    create_main_window()
