'''
Names: Pablo Duenas & Olive Riggs
Class: CS 2520
Project: Horoscope Generator

Hello there! In order to run this program you must:
(1) Have the pygame module dowloaded via terminal
(2) Contain all necessary files in one folder such as:
    (a) all .jpg files for each of the 12 zodiac signs
    (b) background_horoscope.gif
    (c) Now-We-Ride.mp3
    (d) Horoscope.main.py
    (e) zodiac.py
(3) press the run button on Pycharm or any other equivalent IDE
'''
import tkinter as tk    #GUI module
from PIL import ImageTk #Display photos
import zodiac as z  #OOP class with two fucntions
import pygame       #used for music

def main():
    #function displays horoscope page of information
    def display_zodiac(sign, image):
        # using tkinter's Toplevel() will create a seprate window for horoscope
        sign_generated = tk.Toplevel()
        # title of window is set as sign String: ex. SCORPIO
        sign_generated.title(sign.upper())
        # dimentions of window
        sign_generated.geometry('750x950')
        # Window is set at dimension and cannot be resized
        sign_generated.resizable(width=False, height=False)

        # define background canvas for the window by using tkinter's Canvas class
        horoscopeCanvas = tk.Canvas(sign_generated, width=750, height=950, bd=0, highlightthickness=0)
        horoscopeCanvas.pack(fill="both", expand=True)

        #background photo is set to the value of dictionary that corresponds to zodiac sign
        bg = ImageTk.PhotoImage(file=image)
        horoscopeCanvas.create_image(0, 0, image=bg, anchor="nw")

        # Adding exit button, the sign display info will disappear after clicking this button
        exit_button = tk.Button(sign_generated, text="EXIT ➯",fg = 'red', activeforeground='black', font=("Helvetica", 16), \
                                width=15, borderwidth=20, command=lambda: sign_generated.destroy())
        exit_button_window = horoscopeCanvas.create_window(450, 10, height=25, anchor="nw", window=exit_button)

        #GUI mainloop allows for window to stay open
        sign_generated.mainloop()

    # funtion will return image file as String
    def getImage(sign):
        # utilizing dictionary in order to obtain image file that corresponds to each zodiac sign
        zodiacImages = {'Aries':'aries.jpg', 'Taurus':'taurus.jpg', 'Gemini':'gemini.jpg',\
                        'Cancer':'cancer.jpg', 'Leo':'leo.jpg', 'Virgo':'virgo.jpg', \
                        'Libra':'libra.jpg', 'Scorpio':'scorpio.jpg', 'Sagittarius':'sagittarius.jpg',\
                        'Capricorn':'capricorn.jpg', 'Aquarius':'aquarius.jpg', 'Pisces':'pisces.jpg'}
        #image variable saved the value from using the key as index
        image = zodiacImages[sign]
        return image

    # getBirthday function will call get user's input, creates a new object, checks valid birthday
    # if bday is valid then sign is assigned and horoscope will display
    def getBirthday(month, date):
        #user input  is saved into variables
        month = month_entry.get()
        date = date_entry.get()
        #oject is created and month and date is passed into class
        zodiac = z.Zodiac(month, date)
        # testBday will save True/False
        testBday = zodiac.checkBirthday()
        # if/else statment: True will display horoscope info, False will show
        if testBday == True:
            # acquire the sign by using zodiacSign() method from Zodiac class
            sign = zodiac.zodiacSign()
            # acquire the image file that corresponds
            image = getImage(sign)
            # call the display_zodiac function to display the new window of zodiac information
            display_zodiac(sign, image)
        else:
            # These two lines will print and error message saying the user input is incorrect
            error = tk.Canvas()
            my_canvas.create_text(425, 300, text="You Entered an invalid Birthday! Try again!", font=("Helvetica", 18), fill="white")

    # entry_clear(e) function is used to clear the pre-input text inside the widgets once user clicks on them
    def entry_clear(e):
        if month_entry.get() == 'ex: 1-12' or date_entry.get() == 'ex: 1 - 31':
            month_entry.delete(0, 'end')
            date_entry.delete(0, 'end')

    # This function recieves the music file name in the parameter and plays music while program is running
    def play_music_bg(music):
        pygame.mixer.init()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(loops=0)

    # -----following code pertains to main user input window-----
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("🪐🌀HOROSCOPE GENERATOR🌀🪐")
    # sets the dimensions of the window to measurement
    root.geometry('625x350')
    #prevents user to resize the window
    root.resizable(width=False, height=False)

    #canvas function will create a background for the GUI
    my_canvas = tk.Canvas(root, width=625, height=350, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    #using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="background_horoscope.gif")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # Background music function has music file in parameter
    play_music_bg("Now-We-Ride.mp3")

    # create_text funtion from tkinter will display text onto GUI
    my_canvas.create_text(425, 50, text="✨HOROSCOPE GENERATOR✨\n  ♈️♉️♊️♋️♌️♍️♎️♏️♐️♑️♒️♓️",\
                          font=("Helvetica", 18), fill="white")
    my_canvas.create_text(380, 140, text="Month", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(380, 190, text="Date", font=("Helvetica", 16), fill="white")

    # next four lines will create Entry text boxes: month and date
    month_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=10, bg="white", borderwidth=5)
    date_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=10, bg="white", borderwidth=5)
    month_window = my_canvas.create_window(425, 125, anchor="nw", window=month_entry)
    date_window = my_canvas.create_window(425, 175, anchor="nw", window=date_entry)

    # pre set text will appear at the start of the code to give user formatting instructions of their month and date
    month_entry.insert(0, "ex: 1 for Jan")
    date_entry.insert(0, "ex: 1 - 31")
    month_entry.bind("<Button-1>", entry_clear)
    date_entry.bind("<Button-2>", entry_clear)

    # We used the Button function in Tkinter which will call the getBirthday function once clicked
    continue_button = tk.Button(root, text="DONE ➯", activeforeground='white', font=("Helvetica", 14), \
                                width=12, borderwidth=10, relief="sunken", command=lambda :\
                                getBirthday(month_entry, date_entry))

    continue_button_window = my_canvas.create_window(420, 250, height= 20, anchor="nw", window=continue_button)
    root.mainloop()

if __name__ == '__main__':
    main()
