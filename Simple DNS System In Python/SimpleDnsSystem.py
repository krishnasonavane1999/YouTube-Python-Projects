from tkinter import *
from tkinter import messagebox
import socket
import webbrowser

'''
Let me know in the comments of this YouTube Video if you face any challenge - https://www.youtube.com/results?search_query=Krishna+Sonavane

There is lot you can improve in this project - Below are some points for you
1. Jab input me ham kuch bhee nahi denge aur Get IP click karenge to kya dikhta hai? Usko haise handle kar sakte hai?
2. Kya hota hai jab ham IP address hee as a input denge?
3. Ek aur scenario ke baare me socho jaha ye fail ho sakta hai.

'''

def main(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        message = f"IP addreess of {domain_name} is {ip_address}"
        messagebox.showinfo(title="DNS System", message=message)
        show_ip.config(text=ip_address)
        visit_ip.grid(row=4, column=0)
    except:
        messagebox.showerror(title="DNS System", message="Hmm.. Looks like you have entered invalid Domain name")


def get_ip_address():
    domain_name = domain_name_field.get()
    main(domain_name)


# User interface
window = Tk()
window.title("DNS System")
window.geometry("275x300")  # WXH

message = Label(window, text="Enter Domain Name",
                font=("Calibri", 15, "bold"))

domain_name_field = Entry(width=25, font=("Calibri", 15, "bold"))

get_ip_button = Button(text="Get IP",
                       font=("Calibri", 12, "bold"),
                       foreground="green",
                       command=get_ip_address)

show_ip = Label(text="", font=("Calibri", 15, "bold"))
message.grid(row=0, column=0, padx=10, pady=10)
domain_name_field.grid(row=1, column=0, padx=10, pady=10)
get_ip_button.grid(row=2, column=0, padx=10, pady=10)
show_ip.grid(row=3, column=0, padx=10, pady=10)


def goto_ip_address():
    ip_address = show_ip["text"]
    webbrowser.open_new_tab(f"http://{ip_address}")


visit_ip = Button(text="Visit IP",
                  font=("Calibri", 12, "bold"),
                  foreground="green",
                  command=goto_ip_address)


# Bonus - Your Branding on Your Product ✔
branding_message = "Designed by Krisha Sonavane" #
branding = Label(text=branding_message, font=("Helvetica", 10, "normal"))
branding.grid(row=7, column=0, padx=10, pady=40)

window.mainloop()
