from tkinter import *
from gtts import gTTS
import os
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

file_text_data = ""

def handle_file():
    file_path = askopenfilename()
    file = open(file_path, 'r')
    global file_text_data
    file_text_data = file.read()

def process_data():
    global file_text_data

    text_language = language.get()

    if text_language == "Choose Language":
        messagebox.showwarning(title="Error Occured", message="Please select the language")
        return
    elif text_language == "Marathi":
        text_language = 'mr' #code for marathi
    elif text_language == "English":
        text_language = 'en' #code for english
    else:
        text_language = 'hi' #code for hindi

    try:
        obj = gTTS(text=file_text_data, lang=text_language, slow=False)
        obj.save("convertedData.mp3")
    except Exception as ex:
        messagebox.showwarning(ex)


def listen():
    try:
        os.system("convertedData.mp3")
    except Exception as ex:
        messagebox.showwarning(ex)

window = Tk()

window.title("Text to Speech Converter")
window.geometry("350x430") #WidthXHeight of UI window(in quotes)

#custom font for labels and buttons
custom_label_font = ("Calibri", 15, "bold") #font family(name), size of text, font style(bold, italic, etc)
custom_button_font = ("Arial", 12, "bold") #font family(name), size of text, font style(bold, italic, etc)

#first label frame
first_label_frame = LabelFrame(window, text="Data")
first_label_frame.grid(row=0, column=0, padx=20, pady=5)

#second label frame
second_label_frame = LabelFrame(window, text="Process")
second_label_frame.grid(row=1, column=0) # one below another


# first frame elements
upload_file_label = Label(first_label_frame,
                          text="Upload file Below",
                          justify="center",
                          font=custom_label_font)

upload_file_button = Button(first_label_frame,
                            text="Choose File",
                            font=custom_button_font,
                            foreground="blue",
                            justify="center",
                            command=handle_file
                            )

choose_language_label = Label(first_label_frame,
                              text="Choose File Language",
                              justify="center",
                              font=custom_label_font)

language = StringVar()
language.set("Choose Language")

choose_language_dropdown = OptionMenu(first_label_frame, language, "English", "Hindi", "Marathi")
choose_language_dropdown.config(font=custom_button_font, foreground="blue", justify="center")

# second frame elements
convert_label = Label(second_label_frame,
                      text="Convert Text to Speech",
                      justify="center",
                      font=custom_label_font)

covert_button = Button(second_label_frame,
                       text="Convert",
                       foreground="blue",
                       justify="center",
                       font=custom_button_font,
                       command=process_data)

listen_label = Label(second_label_frame,
                      text="Listen Now",
                      justify="center",
                      font=custom_label_font)

listen_button = Button(second_label_frame,
                       text="Listen",
                       foreground="blue",
                       justify="center",
                       font=custom_button_font,
                       command=listen)


# screen pe abhee saare elements ko pack karo(matrix ke jaise samjho iss puri main window and labelframe ko)
#second frame
upload_file_label.grid(row=0, column=0, padx=60, pady=5) # row and column
upload_file_button.grid(row=1, column=0, padx=60, pady=5)
choose_language_label.grid(row=2, column=0, padx=60, pady=5)
choose_language_dropdown.grid(row=3, column=0, padx=60, pady=5)

#second frame
convert_label.grid(row=0, column=0, padx=50, pady=5)
covert_button.grid(row=1, column=0, padx=50, pady=5)
listen_label.grid(row=2, column=0, padx=60, pady=5)
listen_button.grid(row=3, column=0, padx=60, pady=5)


custom_branding_font = ("Helvetica", 10, "normal")

#product branding
branding_text =" Designed By Krishna Sonavane"
branding_label = Label(text=branding_text, font=custom_branding_font, justify="center")
branding_label.grid(row=3, column=0, padx=50, pady=15)
window.mainloop()