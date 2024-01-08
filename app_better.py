import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from API import fetch_person_data, fetch_business_proposal, fetch_advice

class ImageLoader:
    @staticmethod
    def load_image(image_url):
        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

class DataFetcher:
    @staticmethod
    def fetch_person_info():
        try:
            return fetch_person_data(), fetch_business_proposal(), fetch_advice()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None, None, None

class UserInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Get User Info")
        self.setup_ui()

    def setup_ui(self):
        self.person_frame = ttk.Frame(self.root, padding="10")
        self.person_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.image_label = ttk.Label(self.person_frame)
        self.image_label.grid(row=0, column=0, rowspan=7)

        self.name_label = self.create_label("Full Name:", 0, 1)
        self.dob_label = self.create_label("Date of Birth:", 1, 1)
        self.username_label = self.create_label("User Name:", 2, 1)
        self.password_label = self.create_label("Password:", 3, 1)
        self.business_label = self.create_label("Business Proposal:", 4, 1, wraplength=300)
        self.advice_label = self.create_label("", 5, 1, wraplength=300, columnspan=2, justify=tk.CENTER)

        fetch_button = ttk.Button(self.root, text="Leak A User", command=self.update_data)
        fetch_button.grid(row=1, column=0, columnspan=3, pady=10)

    def create_label(self, text, row, column, wraplength=None, columnspan=1, justify=tk.LEFT):
        ttk.Label(self.person_frame, text=text).grid(row=row, column=column, sticky=tk.W)
        label = ttk.Label(self.person_frame, text="", wraplength=wraplength if wraplength else 0, justify=justify)
        label.grid(row=row, column=column + 1, columnspan=columnspan, sticky=tk.W)
        return label

    def update_data(self):
        person_data, business_proposal, advice = DataFetcher.fetch_person_info()
        if person_data:
            self.name_label.config(text=f"{person_data['name']['title']} {person_data['name']['first']} {person_data['name']['last']}")
            self.dob_label.config(text=person_data['dob']['date'][:10])
            self.username_label.config(text=person_data['login']['username'])
            self.password_label.config(text=person_data['login']['password'])
            self.business_label.config(text=business_proposal)
            self.advice_label.config(text=advice)

            img_tk = ImageLoader.load_image(person_data['picture']['large'])
            if img_tk:
                self.image_label.config(image=img_tk)
                self.image_label.image = img_tk  # Keep a reference!

def main():
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
