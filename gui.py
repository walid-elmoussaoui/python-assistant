from tkinter import *
# Pillow modules for image handling
from PIL import Image, ImageTk

import action 
import speeker
import os
import sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None: 
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()  
def voic ():
    ask_val = speeker.main()
    if not ask_val:
        # either pyaudio missing or recognition failed
        text.insert(END, "Me --> [voice input unavailable]\n")
        return

    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
        text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False,False)
root.config(bg="#6F8FAF")

# Replace your image loading code with this:
try:
    # note: filename was corrected to assistant.png
    image_path = resource_path("image/assistant.png")
    img = Image.open(image_path)
    Display_Image = ImageTk.PhotoImage(img)
except Exception as e:
    print(f"Error loading image: {e}")
    # Create a blank image as fallback
    Display_Image = PhotoImage(width=1, height=1)

# Main Frame
Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

# Text Lable 
Text_lable = Label(Main_frame, text = "AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)


# Image (already attempted to load above using resource_path)
# The try/except block earlier sets Display_Image. Here we simply create the
# label using whatever image was loaded.
Image_Lable = Label(Main_frame, image=Display_Image)
Image_Lable.grid(row=1, column=0, pady=20)



# Add a text widget

text=Text(root , font= ('Courier 10 bold') , bg = "#356696",)
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 




# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=120 , y = 500 , width= 352, height= 30)



button2 =  Button(root,  text="speeker" , bg="#356696" , pady=16 ,  padx=20,  borderwidth=3 , relief=SOLID ,  command= voic)
button2.place(x= 10, y= 484)


# Add a text button2
button2 =  Button(root,  text="Send" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 300, y= 575)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 125, y= 575)
root.mainloop()