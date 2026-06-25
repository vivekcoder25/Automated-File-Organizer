import tkinter as tk
from tkinter import filedialog, messagebox
import os

def create_folders():
    folder = filedialog.askdirectory()

    if not folder:
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".doc", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    for category in list(file_types.keys()) + ["Others"]:
        os.makedirs(os.path.join(folder, category), exist_ok=True)

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue

        moved = False

        extension = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():

            if extension in extensions:

                destination = os.path.join(folder, category)

                os.rename(
                    file_path,
                    os.path.join(destination, file)
                )

                moved = True
                break

        if not moved:

            destination = os.path.join(folder, "Others")

            os.rename(
                file_path,
                os.path.join(destination, file)
            )
messagebox.showinfo(
    "Success",
    "Files Organized Successfully!"
)
    

root = tk.Tk()
root.title("Automated File Organizer")
root.geometry("500x300")

title = tk.Label(
    root,
    text="Automated File Organizer",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

button = tk.Button(
    root,
    text="Create Folders",
    command=create_folders
)
button.pack(pady=20)

root.mainloop()