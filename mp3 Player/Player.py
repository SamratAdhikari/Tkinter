from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog as fd
import pygame
import time
from mutagen.mp3 import MP3

# Functions


def add_song():
    song = fd.askopenfilename(initialdir="C:\\Users\\KillerBee\\Downloads\\Music\\", title="Choose a Song",
                              filetypes=(("mp3 Files", "*.mp3"), ("All Files", "*.*")))
    # Add songhttps://youtu.be/3rL15j0WvlA?t=4 to the screen
    song_box.insert(END, song)


def add_many_songs():
    songs = fd.askopenfilenames(initialdir="C:\\Users\\KillerBee\\Downloads\\Music\\", title="Choose a Song",
                                filetypes=(("mp3 Files", "*.mp3"), ("All Files", "*.*")))
    for song in songs:
        song_box.insert(END, song)


def remove_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def remove_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()
    msg.showinfo("Done", "All songs removed from the Playlist")


# Grab Song Length info
def play_time():
    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000
    # throw up temporary label to get data
    # slider_label.config(text=f"{int(slider.get())} and {int(current_time)}")
    converted_current = time.strftime("%H:%M:%S", time.gmtime(current_time))

    # Get currently playing song
    song = song_box.get(ACTIVE)
    song_mut = MP3(song)

    global song_len
    song_len = song_mut.info.length
    total_time = time.strftime("%H:%M:%S", time.gmtime(song_len))

    current_time += 1  # just to label the timestamps

    if int(slider.get()) == int(song_len):
        sts.config(text=f"{total_time}  ||  {total_time}  ")

    elif paused:
        pass

    elif int(slider.get()) == int(current_time):
        #     slider hasnt been moved
        # Update slider position
        slider_pos = int(song_len)
        slider.config(to=slider_pos, value=current_time)
    else:
        #     silder has moved
        # Update slider position
        slider_pos = int(song_len)
        converted_current = time.strftime(
            "%H:%M:%S", time.gmtime(int(slider.get())))
        slider.config(to=slider_pos, value=slider.get())
        sts.config(text=f"{converted_current}  |  {total_time}  ")

    #     Move this thing along by one second
        next_time = int(slider.get()) + 1
        slider.config(value=next_time)

    # Update slider postion value to song time passed
    # slider.config(value=int(current_time))

    # Update slider position
    # slider_pos = int(song_len)

    # Update Time
    sts.after(1000, play_time)  # 1000 milisecond = 1 second


# Play the Selected Song
def play():
    global stopped
    stopped = False
    slider.config(value=0)
    song = song_box.get(ANCHOR)
    try:
        if song != '':
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            play_time()

            # Update slider position
            # slider_pos = int(song_len)
            # slider.config(to=slider_pos, value=0)

            current_volume = pygame.mixer.music.get_volume()

        elif song == '':
            msg.showinfo(
                "Select a song", "Please Select a Song before pressing the Play Button")
    except Exception as e:
        msg.showerror("Error", e)


global stopped
stopped = False


def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    slider.config(value=0)
    sts.config(text="")

    global stopped
    stopped = True


def forward():
    try:
        slider.config(value=0)
        next_song = song_box.curselection()
        next_song = next_song[0]+1
        song = song_box.get(next_song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Move active forward
        song_box.selection_clear(0, END)
        song_box.activate(next_song)
        song_box.selection_set(next_song, last=None)

    except Exception as e:
        stop()
        msg.showinfo("Error", "No more song in the list to play forward")


def backward():
    try:
        slider.config(value=0)
        back_song = song_box.curselection()
        back_song = back_song[0] - 1
        song = song_box.get(back_song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Move active forward
        song_box.selection_clear(0, END)
        song_box.activate(back_song)
        song_box.selection_set(back_song, last=None)

    except Exception as e:
        stop()
        msg.showinfo("Error", "No more song in the list to play backward")


# Create global pause variable
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    elif not paused:
        pygame.mixer.music.pause()
        paused = True


# Slider
def slide(x):
    # slider_label.config(text=f"{int(slider.get())}")
    song = song_box.get(ANCHOR)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


def volume(x):
    pygame.mixer.music.set_volume(vol_slider.get())

    # Change Volume images
    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume*100
    vol = int(current_volume)
    if vol < 1:
        volume_meter.config(image=vol0)
    elif vol >= 1 and vol <= 25:
        volume_meter.config(image=vol1)
    elif vol > 25 and vol <= 50:
        volume_meter.config(image=vol2)
    elif vol > 50 and vol <= 75:
        volume_meter.config(image=vol3)
    elif vol > 75 and vol <= 100:
        volume_meter.config(image=vol4)


root = Tk()

# Initialize Pygame Mixer
pygame.mixer.init()

# Create a Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="white", width=60,
                   selectbackground="steelblue3", selectforeground="black")
song_box.grid(row=0, column=0)

# Define Player Control Buttons Images
back_img = PhotoImage(file="images/backward.png")
for_img = PhotoImage(file="images/forward.png")
play_img = PhotoImage(file="images/play.png")
pause_img = PhotoImage(file="images/pause.png")
stop_img = PhotoImage(file="images/stop.png")

# Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file="images/volume0.png")
vol1 = PhotoImage(file="images/volume1.png")
vol2 = PhotoImage(file="images/volume2.png")
vol3 = PhotoImage(file="images/volume3.png")
vol4 = PhotoImage(file="images/volume4.png")

# Create Player Control Frames
controls_frame = ttk.Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create volume control frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=(10, 0))

# Create Volume Meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

# Create Player Control Buttons
back_btn = Button(controls_frame, image=back_img,
                  borderwidth=0, command=backward)
for_btn = Button(controls_frame, image=for_img, borderwidth=0, command=forward)
play_btn = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_img,
                   borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

# Grid the Buttons
pause_btn.grid(row=0, column=0, padx=10)
back_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
for_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# File Menu
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=add_song_menu)
# Add a Song
add_song_menu.add_command(label="Add a song", command=add_song)
# Add many Songs
add_song_menu.add_command(label="Add many songs", command=add_many_songs)

# Remove Songs
remove_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove", menu=remove_menu)
remove_menu.add_command(label="Remove selected song", command=remove_song)
remove_menu.add_command(label="Remove all songs", command=remove_songs)

# Create Status Bar
sts = ttk.Label(root, text="Play a Song  ",
                borderwidth=2, relief=SUNKEN, anchor=E)
sts.pack(fill=X, side=BOTTOM, ipady=2)

# Create Slider
slider = ttk.Scale(master_frame, from_=0, to=100,
                   orient=HORIZONTAL, value=0, command=slide, length=350)
slider.grid(row=2, column=0)

# Create Volume Slider
vol_slider = ttk.Scale(volume_frame, from_=1, to=0,
                       orient=VERTICAL, value=1, command=volume, length=130)
vol_slider.pack(pady=10)
vol_slider.set(0.5)


root.wm_iconbitmap("images/icon.ico")
root.title("mp3 Player")
root.geometry("520x350")
root.config(bg="grey")
root.resizable(False, False)
root.mainloop()
