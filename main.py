from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Image Encryption")
window.geometry("500x200")

label = Label(window, text='Welcome to the Image Encryption')
label.pack()
label1 = Label(window, text='Enter the Encryption Key and Press the button:')
label1.pack(pady=3)
def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetype=[('image file', '*.jpg;*png')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)
        print(file_name, key)

        fi = open(file_name, 'rb')  # Read the data in byte format
        image = fi.read()
        fi.close()

        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ int(key)  # Interchanging the values

        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()


b1 = Button(window, text="Encrypt/Decrypt", command=encrypt_image)
b1.place(x=200, y=100)

entry1 = Text(window, height=1, width=20)
entry1.place(x=180, y=70)

window.mainloop()
