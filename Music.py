from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog
import os 
import pygame
import mysql.connector as msqc
# import numpy as np
pygame.mixer.init()
db = msqc.connect(
    host="localhost",
    username="root",
    password=" ",
    database="music_data",
)
cur = db.cursor(buffered=True)
win = Tk()
win.iconbitmap('music_noM_icon.ico')
win.title('Illuminati Music Player')
# Window For Tumbnail
img = Image.open('musicthumb.png')
img_resize = img.resize((200,200))
img_thum = ImageTk.PhotoImage(img_resize)
img_lbl = Label(win , image = img_thum, relief = SUNKEN , borderwidth = 5 , width = 400)
img_lbl.grid(columnspan = 3 , padx = 10 , pady = 10)
#Music Label
music_label = Label(win , text = 'Music' , relief = SUNKEN , borderwidth = 4 , width = 25 , font = (("Consolas") , 15))
music_label.grid(row = 1 , columnspan = 3 , padx = 10 , pady = 10)
# Music Listbox 
queu_box = Listbox(win , width = 50 , borderwidth = 5)
queu_box.grid(columnspan = 3 , padx = 10 , pady = 10)


#Image for button
frm = Frame(win)
frm.grid(columnspan = 3 , padx = 10 , pady = 10)
img_button_play = Image.open('play.png').resize((65 , 65))
img_button_next = Image.open('right-arrow.png').resize((45 , 45))
img_button_pre = Image.open('back.png').resize((50 , 50))
img_button_pause = Image.open('pause (1).png').resize((50 , 50))
img_button_delete = Image.open('delete.png').resize((50 , 50))
# Frame Image 
img_button_play_thumbnail = ImageTk.PhotoImage(img_button_play)
img_button_next_thumbnail = ImageTk.PhotoImage(img_button_next)
img_button_pre_thumbnail = ImageTk.PhotoImage(img_button_pre)
img_button_pause_thumbnail = ImageTk.PhotoImage(img_button_pause)
img_button_delete_thumbnail = ImageTk.PhotoImage(img_button_delete)
#Button fro controller

         
i = 0;j = 1
# print(no)
# global queu_box_own , queu_box_own_1 , queu_box_own_2 ,  queu_box_own_3
T_NAME ='music_info_queue'
def start(table_name):
    global T_NAME
    T_NAME = table_name
    # Set default values
    play_song = queu_box.get(ACTIVE)
    qry = f'SELECT file_loc FROM {table_name} where first_name LIKE"{play_song}%"'
    cur.execute(qry)
    music = cur.fetchone()[0]
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
pa = 0    
def add_music(t_name = T_NAME):
    # print(t_name)
    file = filedialog.askopenfilenames(initialdir = '/' , title = 'Musics' , filetypes = (('all music', '*.opus *.mp3 *.wav '),))
    for path in file:
        remove_ext = str(os.path.basename(path))
        orginal_name = os.path.splitext(remove_ext)
        path = str(path)
        sql = (orginal_name[0],path)
        query = f'INSERT INTO {t_name} values (%s,%s)'
        cur.execute(query,sql)
        db.commit()
        queu_box.insert(END,"Song Added to"+" "+t_name+" "+ orginal_name[0])
def pause(ev):
    global pa
    if(pa==0):
        pygame.mixer.music.pause()
        pa = 1
    else:
        pygame.mixer.music.unpause()
        pa = 0
# print(ii)
def next():
    number = f"SELECT count(first_name) from {T_NAME}"
    cur.execute(number)
    no = cur.fetchone()[0]
    ii = int(no)
    cur_song = queu_box.curselection()
    cur_song = cur_song[0]+1
    # print(cur_song)
    if (cur_song == ii):
        cur_song = 0
    next_song = queu_box.get(cur_song)
    # print(next_song)
    print(T_NAME)
    qry = f'SELECT file_loc FROM {T_NAME} where first_name LIKE"%{next_song}%"'
    cur.execute(qry)
    # print(cur.fetchone())
    music = cur.fetchone()[0]
    # print(music)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    queu_box.selection_clear(0,END)
    queu_box.activate(cur_song)
    queu_box.selection_set(cur_song , last = None)
    # print(ii)

def previous():
    cur_song = queu_box.curselection()
    cur_song = cur_song[0]-1
    if (cur_song == -1):
        cur_song = ii-1
    next_song = queu_box.get(cur_song)
    # print(T_NAME)
    qry = f'SELECT file_loc FROM {T_NAME} where first_name LIKE"{next_song}%"'
    cur.execute(qry)
    music = cur.fetchone()[2]
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    queu_box.selection_clear(0,END)
    queu_box.activate(cur_song)
    queu_box.selection_set(cur_song)

def delete():
    cur_song = queu_box.curselection()
    pygame.mixer.music.pause()
    # cur_song = cur_song[0] 
    queu_box.delete(cur_song[0])
    queu_box.selection_set(0)
# create a new playlist



button_play = Button(frm,image =img_button_play_thumbnail  , borderwidth = 0, command =  lambda :start('music_info_queue'))
button_pause = Button(frm,image =img_button_pause_thumbnail  , borderwidth = 0 , command = lambda : pause(0))
button_next = Button(frm,image = img_button_next_thumbnail , borderwidth = 0 ,command =  next)
button_pre = Button(frm,image = img_button_pre_thumbnail , borderwidth = 0 ,command =  previous)
button_delete = Button(frm,image = img_button_delete_thumbnail , borderwidth = 0 , command = delete)

button_delete.grid(row = 2, column = 1 ,  pady = 10 )
button_play.grid(row = 3, column = 1 ,  pady = 10 , padx = 10 )
button_pause.grid(row = 4,  pady = 10 , padx = 6, columnspan=3 )
button_next.grid(row = 3, column = 2 ,  pady = 10 , padx = 5)
button_pre.grid(row = 3, column = 0 ,  pady = 10 , padx = 5)

    
#Backend functions
def play_list():
    global win_new_3
    win_new_3 = Toplevel()
    win_new_3.iconbitmap('music_noM_icon.ico')
    win_new_3.title('Add Songs')
    play_label = Label(win_new_3 , text ="music_info_queue", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label.grid(row = 0 , column = 0,  pady = 10 , padx = 5)
    queu_box_own = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own.grid(row = 1 , column = 0 , padx = 10 , pady = 10)
    button_song_add_0   = Button(win_new_3 , text = "Add Song " , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command =  lambda:add_music('music_info_queue'))
    button_song_add_0.grid(row = 2 , column =0,  pady = 10 , padx = 5 )
    
    qry_queue = f'SELECT first_name FROM music_info_queue'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own.insert(END,naam[0])

    play_label_1 = Label(win_new_3 , text ="my_music", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label_1.grid(row = 0 , column = 1,  pady = 10 , padx = 5)
    queu_box_own_1 = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own_1.grid(row = 1 , column = 1 , padx = 10 , pady = 10)
    button_song_add_1   = Button(win_new_3 , text = "Add Song" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command =  lambda:add_music(t_name='my_music'))
    button_song_add_1.grid(row = 2 , column =1,  pady = 10 , padx = 5 )

    qry_queue = f'SELECT first_name FROM my_music'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own_1.insert(END,naam[0])


    play_label_2 = Label(win_new_3 , text ="playlist_3", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label_2.grid(row = 0 , column = 2,  pady = 10 , padx = 5)
    queu_box_own_2 = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own_2.grid(row = 1 , column = 2 , padx = 10 , pady = 10)
    button_song_add_2   = Button(win_new_3 , text = "Add Song" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command =lambda:add_music(t_name='playlist_3'))
    button_song_add_2.grid(row = 2 , column =2,  pady = 10 , padx = 5 )

    qry_queue = f'SELECT first_name FROM playlist_3'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own_2.insert(END,naam[0])

    play_label_3 = Label(win_new_3 , text ="playlist_4", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label_3.grid(row = 0 , column = 4,  pady = 10 , padx = 5)
    queu_box_own_3 = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own_3.grid(row = 1 , column = 4 , padx = 10 , pady = 10)
    button_song_add_3   = Button(win_new_3 , text = "Add Song" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command = lambda:add_music(t_name='playlist_4'))
    button_song_add_3.grid(row = 2 , column =4,  pady = 10 , padx = 5 )
       
    qry_queue = f'SELECT first_name FROM playlist_4'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
        queu_box_own_3.insert(END,naam[0])

def play_button(table_name):
    pygame.mixer.music.stop()
    queu_box.delete('0','end')
    qry_queue = f'SELECT first_name FROM {table_name}'
    cur.execute(qry_queue)
    name = cur.fetchall()
    
    for naam in name:
        queu_box.insert(END,naam[0])
    queu_box.select_set(0)
    button_play['command'] = lambda : start(table_name)
    global T_NAME
    T_NAME = table_name
    start(table_name)
def play_own():
    win_new_3 = Toplevel()
    win_new_3.title('Your Songs')
    win_new_3.iconbitmap('music_noM_icon.ico')
    global play_button,play_label
    play_label = Label(win_new_3 , text ="music_info_queue", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label.grid(row = 0 , column = 0,  pady = 10 , padx = 5)
    queu_box_own = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own.grid(row = 1 , column = 0 , padx = 10 , pady = 10)
    qry_queue = f'SELECT first_name FROM music_info_queue'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own.insert(END,naam[0])
    play_button_playlist = Button(win_new_3 , text = "Play now" , width = 16 , borderwidth = 5 , font = (("Consolas bold") , 10) , command = lambda : play_button("music_info_queue"))
    play_button_playlist.grid(row = 2 , column = 0 , padx = 10 , pady = 10)


    play_label_1 = Label(win_new_3 , text ="my_music", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label_1.grid(row = 0 , column = 1,  pady = 10 , padx = 5)
    queu_box_own_1 = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own_1.grid(row = 1 , column = 1 , padx = 10 , pady = 10)
    qry_queue = f'SELECT first_name FROM my_music'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own_1.insert(END,naam[0])
    button_song_add_1_playlist= Button(win_new_3 , text = "Play now" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command = lambda:play_button("my_music"))
    button_song_add_1_playlist.grid(row = 2 , column =1,  pady = 10 , padx = 5 )

    play_label_2 = Label(win_new_3 , text ="playlist 3", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label_2.grid(row = 0 , column = 2,  pady = 10 , padx = 5)
    queu_box_own_2 = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own_2.grid(row = 1 , column = 2 , padx = 10 , pady = 10)

    qry_queue = f'SELECT first_name FROM playlist_3'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own_2.insert(END,naam[0])

    button_song_add_2_playlist   = Button(win_new_3 , text = "Play now" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command = lambda:play_button("playlist_3"))
    button_song_add_2_playlist.grid(row = 2 , column =2,  pady = 10 , padx = 5 )

    play_label_3 = Label(win_new_3 , text ="playlist 4 ", font = (("Consolas bold"),10) , borderwidth = 5 , relief = SUNKEN)
    play_label_3.grid(row = 0 , column = 4,  pady = 10 , padx = 5)
    queu_box_own_3 = Listbox(win_new_3 , width = 50 , borderwidth = 5)
    queu_box_own_3.grid(row = 1 , column = 4 , padx = 10 , pady = 10)

    qry_queue = f'SELECT first_name FROM playlist_4'
    cur.execute(qry_queue)
    name = cur.fetchall()
    for naam in name:
         queu_box_own_3.insert(END,naam[0])

    button_song_add_3_playlist   = Button(win_new_3 , text = "Play now" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command = lambda:play_button("playlist_4"))
    button_song_add_3_playlist.grid(row = 2 , column =4,  pady = 10 , padx = 5 )

    

#Add song , create playlist , Play your own created playlist
button_song_add   = Button(win , text = "Add Song to\n queue" , width = 14 , borderwidth = 5 , font = (("Consolas bold") , 10),command = lambda : add_music("music_info_queue"))
button_song_create = Button(win , text = "Create your own\n playlist" , width = 15 , borderwidth = 5 , font = (("Consolas bold") , 10),command = play_list)
button_song_play_own =Button(win , text = "Play song from \ncreated playlist" , width = 16 , borderwidth = 5 , font = (("Consolas bold") , 10) , command = play_own)
button_song_add.grid(row = 4 , column =0,  pady = 10 , padx = 5 )
button_song_create.grid(row = 4 , column = 1,  pady = 10 , padx = 5)
button_song_play_own.grid(row = 4 , column = 2,  pady = 10 , padx = 5)


win.mainloop()
