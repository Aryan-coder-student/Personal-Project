from tkinter import *
import wikipedia 
from tkinter.filedialog import asksaveasfile
win = Tk()
win.iconbitmap('globe_hMo_icon.ico')
win.title('Wikipedia search')
heading = Label(win , text ="Search for Result in Wikipedia ?", font = (("Consolas bold"),20) , borderwidth = 5 , relief = SUNKEN)
heading.grid( columnspan = 5,padx = 20 , pady = 20)
enter = Entry(win , font = (("Lucida Sans Unicode bold"),12),width = 50, borderwidth = 5)
enter.grid(row = 1 , columnspan = 4,padx = 20 , pady = 20)
str0 = StringVar()
# str2 = StringVar()
# str3 = StringVar()
str1 = StringVar()
# str = StringVar()
str0.set("Summary")
option_choose_1 = Radiobutton(win , text = "Summary",font = (("Consolas bold"),12), variable = str0,value ="su")
option_choose_1.grid(row = 2 , column =0 , padx = 10 , pady = 10)
# option_choose_1.deselect()
option_choose_2 = Radiobutton(win , text = "Whole Page",font = (("Consolas bold"),12) , variable = str0,value ="wp")
option_choose_2.grid(row = 2 , column =1 , padx = 10 , pady = 10)
# option_choose_2.deselect()
option_choose_3 = Radiobutton(win , text = "Short Defination",font = (("Consolas bold"),12) , variable = str0,value ="sd")
option_choose_3.grid(row = 2 , column = 2, padx = 10 , pady = 10)
# option_choose_3.deselect()
# option_choose = Radiobutton(win , text = "Content",font = (("Consolas bold"),12) , variable = str0,value ="sd")
# option_choose.grid(row = 2 , column = 4, padx = 10 , pady = 10)
option_choose_4= Checkbutton(win , text = "Hindi\n( Default is English)",font = (("Consolas bold"),12) , variable = str1, onvalue ="hi", offvalue ="no")
option_choose_4.grid(row = 2 , column =3 , padx = 10 , pady = 10)
option_choose_4.deselect()

def search_wiki():
    # search_button.destroy()



    fr = Frame(win)
    my_scroll = Scrollbar(fr , orient = VERTICAL)
    txt_area = Text(fr , width = 78 , height = 20  , font = (("Century Gothic bold"),) , borderwidth = 5 , yscrollcommand = my_scroll.set)
    if(str0.get()=="su"):
        if(str1.get()=="hi"):
            wikipedia.set_lang("hi")
            sumry = wikipedia.summary(enter.get())
            txt_area.insert(END,sumry)
        elif(str1.get()=="no") : 
            wikipedia.set_lang("en")
            sumry = wikipedia.summary(enter.get())
            txt_area.insert(END,sumry)
    if(str0.get() =="wp"):
        if(str1.get()=="hi"):
            wikipedia.set_lang("hi")
            whole_page = wikipedia.page(enter.get()).content
            txt_area.insert(END,whole_page) 
        elif (str1.get()=="no"):
            wikipedia.set_lang("en")
            whole_page = wikipedia.page(enter.get()).content
            txt_area.insert(END,whole_page)
    if(str0.get() =="sd"):
        if(str1.get()=="hi"):
            wikipedia.set_lang("hi")
            short_def = wikipedia.summary(enter.get() , sentences = 4)
            txt_area.insert(END,short_def)
        elif (str1.get()=="no"):
            wikipedia.set_lang("en")
            short_def = wikipedia.summary(enter.get() , sentences = 4)
            txt_area.insert(END,short_def)
    my_scroll.config(command = txt_area.yview)
    my_scroll.pack(side = RIGHT, fill = Y)
    txt_area.pack()
    fr.grid(row = 6 , columnspan = 4,padx = 5 , pady = 10)
    tags =wikipedia.search(enter.get())
    fr_1 = Frame(win)
    my_scroll_2 = Scrollbar(fr_1 , orient = HORIZONTAL)
    suggested_tags = Label(fr_1 ,text = "Some Suggested tags", font = (("Consolas bold"),))
    txt_suggest = Text(fr_1, font = (("Consolas bold"),) , width = 60 , height = 1 , borderwidth = 5 , xscrollcommand = my_scroll_2.set,wrap='none')
    txt_suggest.insert(END,tags)
    
    my_scroll_2.config(command = txt_suggest.xview)
    my_scroll_2.grid(row = 2 , columnspan = 4 ,  sticky=E+W )
    txt_suggest.grid(row = 1 , columnspan = 4)
    suggested_tags.grid(row = 0 , columnspan = 4)
    fr_1.grid(row = 4 , columnspan = 4,padx = 5 , pady = 1)
    def all_back():
        # suggested_tags.destroy()
        txt_area.destroy()
        back_button.destroy()
        save_button.destroy()
        fr_1.destroy()
        fr.destroy()
        # search_button = Button(win , text = "Enter",font = (("Consolas bold"),20) , borderwidth = 5 , width = 45 , command = lambda : search_wiki())
        # search_button.grid(row =3 , columnspan = 4 , padx = 10 , pady = 10)
    
    def save():
        save_name = asksaveasfile(filetypes = (('Text Document' , '*.txt'), ) , defaultextension =(('Text Document', '*.txt'),))
        txt = open(save_name.name,mode='w')
        text_save= txt_area.get('0.0','end')
        txt.write(f'{text_save}')
        # print(txt_area.get('0.0','end'))
        txt.close()
    
    back_button = Button(win , text = " <-Back",font = (("Consolas bold"),10) , borderwidth = 5, command = all_back)
    back_button.grid(row =5 , column = 2   )

    save_button = Button(win , text = "Save",font = (("Consolas bold"),12) , borderwidth = 5, command =save)
    save_button.grid(row =5 , column = 1  )
    # if (str0 == "su"):

print("नाटकीय")

    
    








search_button = Button(win , text = "Enter",font = (("Consolas bold"),20) , borderwidth = 5 , width = 45 , command = search_wiki)
search_button.grid(row =3 ,columnspan = 4 , padx = 10 , pady = 10)

win.mainloop() 
