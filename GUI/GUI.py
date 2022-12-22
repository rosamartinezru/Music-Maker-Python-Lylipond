import tkinter as tk
from PIL import ImageTk, Image



def start_GUI():
    window = tk.Tk()
    window.geometry("900x900")
    bg = '#353445'
    text = '#00b76c'
    bg_box = '#282733'
    box_text = '#dcdee2'

    window.configure(background= bg)
    
    Xbox = 230      # Elements positioning
    Xlab = 70       # Elements positioning

    ticket_0 = tk.Label(window, text= "Mus(E)ify", bg= bg, fg= text, font= "Verdana 20 bold", justify= tk.LEFT)
    ticket_0.place(x = 450 - 100, y = 10,width= 200, height= 30)

    ''' IMAGES '''
    img_1 = Image.open("Nota_musical.png")
    image_resize = img_1.resize((50, 50))
    img1 = ImageTk.PhotoImage(image_resize)
    label_1 = tk.Label(image= img1, borderwidth= 0)
    label_1.place(x = 525, y = 5)

    img_2 = Image.open("Nota_musical.png")
    image_resize = img_2.resize((50, 50))
    img2 = ImageTk.PhotoImage(image_resize)
    label_2 = tk.Label(image= img2, borderwidth= 0)
    label_2.place(x = 320, y = 5)

    img_3 = Image.open("Corazon.png")
    image_resize = img_3.resize((50, 50))
    img3 = ImageTk.PhotoImage(image_resize)
    label_3 = tk.Label(image= img3, borderwidth= 0)
    label_3.place(x = 620, y = 225)

    img_4 = Image.open("Nota_musical_2.png")
    image_resize = img_4.resize((50, 50))
    img4 = ImageTk.PhotoImage(image_resize)
    label_4 = tk.Label(image= img4, borderwidth= 0)
    label_4.place(x = 720, y = 425)

    ''' GIFS '''

    # def play_gif():
    #     global img
    #     img = Image.open("gato_piano.gif")

    #     lbl = tk.Label(window)
    #     lbl.place(x= 600, y= 200, width= 300, height= 300)

    #     for img in ImageSequence.Iterator(img):
    #         img = ImageTk.PhotoImage(img)
    #         lbl.config(image= img)
    #         window.update()
    #         time.sleep(0.05)
    #         window.after(0, play_gif)
    


    ''' TITLE '''
    ticket_1 = tk.Label(window, text= "Title", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_1.place(x = Xlab, y = 100)

    textbox_1 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_1.place(x = Xbox, y = 100,width= 220, height= 20)

    ''' COMPOSER '''
    ticket_2 = tk.Label(window, text= "Composer", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_2.place(x = Xlab, y = 150)

    textbox_2 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_2.place(x = Xbox, y = 150,width= 220, height= 20)

    ''' INSTRUMENT '''
    ticket_3 = tk.Label(window, text= "Instrument", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_3.place(x = Xlab, y = 200)

    Instrument = ""
    def instrument(Button):
        global Instrument
        Button.config(state= "disabled")
        if Button == button_3:
            Instrument= "Piano" 
    button_3 = tk.Button(window, text= "Piano", font = "Verdana 12 bold", bg= box_text)
    button_3.place(x = Xbox, y = 200)
    button_3.config(command= lambda: instrument(button_3))

    ''' REFERENCE '''
    ticket_4 = tk.Label(window, text= "Reference", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_4.place(x = Xlab, y = 250)

    textbox_4 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_4.place(x = Xbox, y = 250,width= 220, height= 20)

    ''' KEY SIGNATURE '''
    ticket_5 = tk.Label(window, text= "Key Signature", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_5.place(x = Xlab, y = 300)

    textbox_5 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_5.place(x = Xbox, y = 300,width= 220, height= 20)

    ''' TIME '''
    ticket_11 = tk.Label(window, text= "Time", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_11.place(x = Xlab, y = 350)

    textbox_11 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_11.place(x = Xbox, y = 350,width= 220, height= 20)

    ''' TEMPO '''
    ticket_6 = tk.Label(window, text= "Tempo", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_6.place(x = Xlab, y = 400)

    textbox_6_1 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_6_1.place(x = Xbox, y = 400,width= 30, height= 20)
    textbox_6_2 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_6_2.place(x = Xbox + 30 + 20, y = 400,width= 220 - (30 + 20), height= 20)

    ''' CLEF '''
    ticket_7 = tk.Label(window, text= "Clef", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_7.place(x = Xlab, y = 450)

    Clef = ""
    def clef(Button):
        global Clef
        button_7_1.config(state= "active")
        button_7_2.config(state= "active")
        button_7_3.config(state= "active")
        button_7_4.config(state= "active")
        Button.config(state= "disabled")
        if Button == button_7_1:
            Clef = "Treble"
        elif Button == button_7_2:
            Clef = "Alto"
        elif Button == button_7_3:
            Clef = "Tenor"
        elif Button == button_7_4:
            Clef = "Bass"

    button_7_1 = tk.Button(window, text= "Treble", font = "Verdana 12 bold", bg= box_text)
    button_7_1.place(x = Xbox, y = 450, width= 70)
    button_7_1.config(command= lambda: clef(button_7_1))
    button_7_2 = tk.Button(window, text= "Alto", font = "Verdana 12 bold", bg= box_text)
    button_7_2.place(x = Xbox + 70 + 5, y = 450, width= 70)
    button_7_2.config(command= lambda: clef(button_7_2))
    button_7_3 = tk.Button(window, text= "Tenor", font = "Verdana 12 bold", bg= box_text)
    button_7_3.place(x = Xbox + 140 +10, y = 450, width= 70)
    button_7_3.config(command= lambda: clef(button_7_3))
    button_7_4 = tk.Button(window, text= "Bass", font = "Verdana 12 bold", bg= box_text)
    button_7_4.place(x = Xbox + 210 + 15, y = 450, width= 70)
    button_7_4.config(command= lambda: clef(button_7_4))

    ''' ANACRUSE '''
    ticket_8 = tk.Label(window, text= "Anacruse", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_8.place(x = Xlab, y = 500)

    Anacruse = ""
    def anacruse(Button, ticket_9, textbox_9):
        global Anacruse
        button_8_1.config(state= "active")
        button_8_2.config(state= "active")
        ticket_9.config(bg= bg, fg= text)
        textbox_9.place(x = Xbox, y = 550, width= 220, height= 20)
        Button.config(state= "disabled")
        if Button == button_8_1:
            Anacruse = "Yes"
        elif Button == button_8_2:
            Anacruse = "No"
            ticket_9.config(fg= bg)
            textbox_9.place(x = -Xbox, y = -550, width= 0, height= 0)

    button_8_1 = tk.Button(window, text= "Yes", font = "Verdana 12 bold", bg= box_text)
    button_8_1.place(x = Xbox, y = 500, width= 60)
    button_8_1.config(command= lambda: anacruse(button_8_1, ticket_9, textbox_9))
    button_8_2 = tk.Button(window, text= "No", font = "Verdana 12 bold", bg= box_text)
    button_8_2.place(x = Xbox + 60 + 5, y = 500, width= 60)
    button_8_2.config(command= lambda: anacruse(button_8_2, ticket_9, textbox_9))

    ''' ANACRUSE RYTHM '''
    ticket_9 = tk.Label(window, text= "Rythm anacruse", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_9.place(x = Xlab, y = 550)

    textbox_9 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_9.place(x = Xbox, y = 550, width= 220, height= 20) 

    ''' SONG '''
    ticket_10 = tk.Label(window, text= "Song", bg= bg, fg= text, font= "Verdana 12 bold", justify= tk.LEFT)
    ticket_10.place(x = Xlab, y = 600)

    textbox_10 = tk.Entry(window, font = "Verdana 12", fg= box_text, bg= bg_box)
    textbox_10.place(x = Xbox, y = 600, width= 600, height= 50)

    ''' RUN '''
    #play_gif()


    def run_button():
        global Instrument, Anacruse, Clef
        Title = textbox_1.get()
        Composer = textbox_2.get()
        # Instrument
        Reference = "" + textbox_4.get() + ""
        key_signature = "" + textbox_5.get() + ""
        figure = textbox_6_1.get()
        Time = textbox_11.get()
        metronome = textbox_6_2.get()
        # Clef
        # Anacruse
        time_anacruse = textbox_9.get()
        song = "" + textbox_10.get() + ""

        V = [Title, Composer, Instrument, Reference, key_signature, figure, Time, metronome, Clef, Anacruse, time_anacruse, song]
        file = open("music_data.txt", "w")
        # file.write(str(Title))
        file.write('\n'.join(V))
        # file.write('\n'.join(str(Instrument)))
        # file.write('\n'.join(str(Reference)))
        # file.write('\n'.join(str(key_signature)))
        # file.write('\n'.join(str(figure)))
        # file.write('\n'.join(str(Time)))
        # file.write('\n'.join(str(metronome)))
        # file.write('\n'.join(str(Clef)))
        # file.write('\n'.join(str(Anacruse)))
        # file.write('\n'.join(str(time_anacruse)))
        # file.write('\n'.join(str(song)))
        file.close()


    button_11 = tk.Button(window, text= "Run", font = "none 12", command= lambda: run_button())
    button_11.place(x = Xbox + 600 - 60, y = 675, width= 60)


        

    ''' MAINLOOPS '''
    window.mainloop()



