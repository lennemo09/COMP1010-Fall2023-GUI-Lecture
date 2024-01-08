import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from API import fetch_person_data, fetch_business_proposal, fetch_advice

root = tk.Tk()
root.title("Get User Info")

# Frame for person data
person_frame = ttk.Frame(root, padding="10")
person_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Image label (place it on the left side now)
image_label = ttk.Label(person_frame)
image_label.grid(row=0, column=0, rowspan=7)

# Labels for person data
ttk.Label(person_frame, text="Full Name:").grid(row=0, column=1, sticky=tk.W)
name_label = ttk.Label(person_frame, text="")
name_label.grid(row=0, column=2, sticky=tk.W)

ttk.Label(person_frame, text="Date of Birth:").grid(row=1, column=1, sticky=tk.W)
dob_label = ttk.Label(person_frame, text="")
dob_label.grid(row=1, column=2, sticky=tk.W)

ttk.Label(person_frame, text="User Name:").grid(row=2, column=1, sticky=tk.W)
username_label = ttk.Label(person_frame, text="")
username_label.grid(row=2, column=2, sticky=tk.W)

ttk.Label(person_frame, text="Password:").grid(row=3, column=1, sticky=tk.W)
password_label = ttk.Label(person_frame, text="")
password_label.grid(row=3, column=2, sticky=tk.W)

# Business proposal (update the column index to shift right)
ttk.Label(person_frame, text="Business Proposal:").grid(row=4, column=1, sticky=tk.W)
business_label = ttk.Label(person_frame, text="", wraplength=300)  # wraplength in pixels
business_label.grid(row=4, column=2, sticky=tk.W)

# Advice label (centered and spanning two columns)
advice_label = ttk.Label(person_frame, text="", wraplength=300, justify=tk.CENTER)
advice_label.grid(row=5, column=1, columnspan=2, padx=10, sticky=(tk.E, tk.W))

def update_data():
    person_data = fetch_person_data()
    business_proposal = fetch_business_proposal()
    advice = fetch_advice()

    # Extracting data from the response
    full_name = f"{person_data['name']['title']} {person_data['name']['first']} {person_data['name']['last']}"
    dob = person_data['dob']['date'][:10]  # Format to 'YYYY-MM-DD'
    user_name = person_data['login']['username']
    password = person_data['login']['password']

    # Updating the labels
    name_label.config(text=full_name)
    dob_label.config(text=dob)
    username_label.config(text=user_name)
    password_label.config(text=password)

    # Fetch and update the image
    image_url = person_data['picture']['large']
    image_response = requests.get(image_url)
    img = Image.open(BytesIO(image_response.content))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # keep a reference!

    business_label.config(text=business_proposal)
    advice_label.config(text=advice)

# Button to fetch and update data
fetch_button = ttk.Button(root, text="Leak A User", command=update_data)
fetch_button.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()

