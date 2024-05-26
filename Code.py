import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root=tk.Tk()
root.geometry('+%d+%d'%(450,150))
root.title("Human Face Counting")

canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3)

logo=Image.open("logo.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

instructions=tk.Label(root,text="Count Number of Faces")
instructions.grid(column=1,row=1)

def open_file():
 
 camera = cv2.VideoCapture(0)
# Take a photo
 ret, photo = camera.read()

# Release the camera
 camera.release()

# Load the Haar cascade for face detection
 face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Convert the photo to grayscale
 gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

# Detect faces in the photo
 faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

# Count the number of faces
 face_count = len(faces)

# Print the number of faces
 print("Number of faces:", face_count)

# Draw a rectangle around each face
 for (x, y, w, h) in faces:
     cv2.rectangle(photo, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show the photo with rectangles around the faces
 cv2.imshow("Faces", photo)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

 #textbox
 text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
 text_box.insert(1.0,"Total Number of Faces counted:",1.0,face_count)
 text_box.tag_configure("center",justify="center")
 text_box.tag_add("center",1.0,"end")
 text_box.grid(column=1,row=4)

def upload():
    browse_text.set("Loading...") 
    file_path = filedialog.askopenfilename()

    browse_text.set("Upload Picture")  

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    img = cv2.imread(file_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    face_count = len(faces)


    print("Number of faces:", face_count)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
 #textbox
    text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
    text_box.insert(1.0,"Total Number of Faces counted:",1.0,face_count)
    text_box.tag_configure("center",justify="center")
    text_box.tag_add("center",1.0,"end")
    text_box.grid(column=1,row=4)  

browse_text=tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text,command=lambda:open_file(),bg="#20bebe",height=2,width=19)
browse_text.set("Capture")
browse_btn.grid(column=1,row=2)

browse_text=tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text,command=lambda:upload(),bg="#20bebe",height=2,width=19)
browse_text.set("Upload Picture")
browse_btn.grid(column=1,row=3)

canvas=tk.Canvas(root,width=600,height=100)
canvas.grid(columnspan=3)

root.mainloop()
