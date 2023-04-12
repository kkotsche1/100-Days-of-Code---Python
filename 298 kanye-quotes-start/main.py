from tkinter import *
import requests

def get_quote():
    quote_api_data = requests.get(url="https://api.kanye.rest")
    kanye_quote = quote_api_data.json()["quote"]
    #try:
    canvas.itemconfig(quote_text, text=kanye_quote)
    #except:

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(row=0, column=0)
quote_text = canvas.create_text(150, 207, text=f"_", width=250, font=("Arial", 30, "bold"), fill="white")

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()