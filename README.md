# COMP1010 - Fall2023 - Introduction to GUI Programming with Python Tkinter and Public Web APIs

## Lecture Notes
You can find the Notion notes for this session here: https://tricolor-riddle-c08.notion.site/Introduction-to-GUI-Programming-with-Python-Tkinter-and-Public-Web-APIs-2834f6bcca264029864e1b08e7676340

## Required dependencies
- `tk` (Tkinter)
- `Pillow` (PIL)
- `requests`

For how to install pip packages with PyCharm, please see the following video: 

https://youtu.be/C7U51qQ2scA?si=fY3CzHY_WPaJhGtl

If you’re using the command line interface (CLI) like Terminal for MacOS or Command Prompt/PowerShell for Windows, install the required packages with `pip`:

```bash
pip install tk
pip install requests
pip install Pillow
```

If `pip` is not a known command on your system, try again using:

```bash
python3 -m pip install tk
python3 -m pip install requests
python3 -m pip install Pillow
```

If you’re using `conda`, use the following commands:

```bash
conda install tk
conda install requests
conda install Pillow
```

Before we get started, create a new Python file with the following lines and run it.

```python
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
```

If the code runs without any errors, we’re good to go!

# Web APIs

<aside>
💡 **What is an “API”?**

</aside>

An API, or Application Programming Interface, is **a set of rules that define how devices and applications can communicate with each other**. APIs are a way to extract and share data within and across organizations.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/13c3b1e4-3619-4c17-b6e5-1d7e44c8bf9c/Untitled.png)

Image: GeeksforGeeks

Typically, you will need to be authorized (with a *authkey/API key*) to be able to access and *****call***** an API. But fortunately for us, there are a lot of free and open web APIs we can use for various purposes. Some of them are compiled into a list here:

https://github.com/toddmotto/public-apis

<aside>
💡 ************************************************How do I use these APIs?************************************************

</aside>

Most of the time, an API will come with its own ***documentation***, which should describe how you can use it. For example, let’s check out this RandomUser API, which generates a completely fictional random user: https://randomuser.me/

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/4353d581-440a-4ce7-ae4f-3b93c52d5798/Untitled.png)

You can see that everytime you reload this page, it creates a whole new person with name, DOB, email, address, etc. Let’s go to the Documentation page to see how we can use this for our own purpose.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/91572aea-5412-4d86-bed1-df04ee047b6a/Untitled.png)

Unfortunately, it is giving us an instruction to use with “AJAX”. What the heck is AJAX? But, since we are clever programmers, we can experiment with the information given here to see what we can do. Let’s open that URL link in our web browser: https://randomuser.me/api/

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/f9e16bf0-d7c6-4688-aa4f-81db691aeec5/Untitled.png)

It’s displaying some sort of a cryptic ancient alien language that we can’t read. But wait! After staring at it for a minute, you are starting to see some familiar signs! Turns out, it looks exactly like a Python dictionary!

```jsx
{'results': [{'gender': 'male',
   'name': {'title': 'Mr', 'first': 'Naod', 'last': 'Aragão'},
   'location': {'street': {'number': 2465, 'name': 'Rua Das Flores '},
    'city': 'Santa Maria',
    'state': 'Amazonas',
    'country': 'Brazil',
    'postcode': 64393,
    'coordinates': {'latitude': '-73.4620', 'longitude': '-93.6697'},
    'timezone': {'offset': '0:00',
     'description': 'Western Europe Time, London, Lisbon, Casablanca'}},
   'email': 'naod.aragao@example.com',
   'login': {'uuid': 'b0733c29-b85d-43db-b752-c8ae07a1a9e4',
    'username': 'goldencat817',
    'password': 'jing',
    'salt': 'SIwZp2TT',
    'md5': '71e68ee60ae4d87e10a919a1777b9393',
    'sha1': '40a9ac5e4d7e1e235e26047c0a91c74e9ee0b86a',
    'sha256': 'dd66482b0c29a251325fa962d9d53f0f1a00f70bd496515d0ef5b3b02838015e'},
   'dob': {'date': '1976-06-12T00:29:00.953Z', 'age': 47},
   'registered': {'date': '2015-01-05T01:54:50.193Z', 'age': 8},
   'phone': '(04) 6165-9295',
   'cell': '(43) 6031-9284',
   'id': {'name': 'CPF', 'value': '133.356.591-55'},
   'picture': {'large': 'https://randomuser.me/api/portraits/men/87.jpg',
    'medium': 'https://randomuser.me/api/portraits/med/men/87.jpg',
    'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/87.jpg'},
   'nat': 'BR'}],
 'info': {'seed': '9b4fb932d49b3eb2',
  'results': 1,
  'page': 1,
  'version': '1.4'}}
```

We can see that this is a dictionary that contains lists and other dictionaries. More accurately, what you’re seeing here is called a JSON string, which can be parsed directly as a Python dictionary.

JSON is the universal standard for APIs across platforms and languages to communicate with each other, by sending information in an universally agreed upon format. This is often call a *******payload*******.

We have just received a payload from the RandomUser API after sending a request to https://randomuser.me/api/, and it contains information that we can use. Let’s try to do this in Python using the `requests` module.

```python
import requests
url = "https://randomuser.me/api/"
response = requests.get(url)
response.raise_for_status()
data = response.json()
print(data)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/992fa1cc-3632-4d4b-8e51-1ab241db33b5/Untitled.png)

You can see that we have successfully received this JSON as an object in Python. We can easily access its data just like a regular dictionary. First we get the value for `results` with `print(data['results'])` and we will get:

```jsx
[{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Ryan', 'last': 'Jones'}, 'location': {'street': {'number': 1624, 'name': 'Queenstown Road'}, 'city': 'Invercargill', 'state': 'Manawatu-Wanganui', 'country': 'New Zealand', 'postcode': 17559, 'coordinates': {'latitude': '48.3009', 'longitude': '-19.6665'}, 'timezone': {'offset': '-4:00', 'description': 'Atlantic Time (Canada), Caracas, La Paz'}}, 'email': 'ryan.jones@example.com', 'login': {'uuid': 'e542b551-4604-4676-bbc0-51c90019d34c', 'username': 'silverbear416', 'password': 'power1', 'salt': 'pxctADBo', 'md5': '380a8aaa14afbf4da91f439f6edc6748', 'sha1': 'e74dc3ec194d32d1090e3a44b87dc06984d51044', 'sha256': '9df5430beeaafafd3c8523c9b4b85d5be24f3f6973d1972629ec8010a5b616f7'}, 'dob': {'date': '1951-02-07T15:19:26.485Z', 'age': 72}, 'registered': {'date': '2017-11-25T13:34:48.127Z', 'age': 6}, 'phone': '(001)-581-2749', 'cell': '(749)-807-0333', 'id': {'name': '', 'value': None}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/59.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/59.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/59.jpg'}, 'nat': 'NZ'}]
```

Which is a list containing a single dictionary, to access this dictionary we will need to write `data['results'][0]`. Then, we can finally access the information we want like `name` or `email`.

```jsx
url = "https://randomuser.me/api/"
response = requests.get(url)
response.raise_for_status()
data = response.json()
print(data['results'][0]['name'])
print(data['results'][0]['email'])
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/1f7d343f-4353-4b54-85ce-83dfe851ec29/Untitled.png)

# Introduction to GUI Programming with Tkinter

- What is GUI programming?
- Benefits of GUI programming
- Introduction to Tkinter
    - What is Tkinter?
    - Why use Tkinter for GUI programming in Python?
- Installing Tkinter
- Creating a basic Tkinter window
    - Importing the necessary modules
    - Creating a Tkinter window object
    - Adding widgets to the window
- Running the Tkinter application

<aside>
💡 **What is GUI programming?**

</aside>

GUI programming, or Graphical User Interface programming, refers to the creation of visual interfaces that allow users to interact with software applications. GUI programming is an essential aspect of modern software development as it provides an intuitive and user-friendly experience.

<aside>
💡 **What are the benefits of GUI programming?**

</aside>

1. Improved user experience: GUIs make it easier for users to interact with software by providing visual elements such as buttons, menus, and forms. This enhances the overall user experience and makes the application more user-friendly.
2. Increased productivity: GUIs offer a more efficient and streamlined workflow, allowing users to perform tasks quickly and easily. By utilizing graphical elements and intuitive controls, GUI applications can enhance productivity and save users' time.
3. Better accessibility: GUIs can accommodate users with different levels of technical expertise and provide accessibility features such as text enlargement and screen readers. This makes the software accessible to a wider range of users, including those with disabilities.

There is a specific area of engineering, design, and research about GUI (and other interfaces for computer programs) called **UI/UX**, scientifically under the umbrella of **Human-Center Computing (HCC)** or **Human-Computer Interactions (HCI)**. 

<aside>
💡 **What is Tkinter?**

</aside>

Tkinter is a popular GUI toolkit for Python that allows developers to create graphical interfaces. It is included with standard Python installations, making it easily accessible and widely used. Tkinter provides a set of pre-built widgets and tools that simplify the process of creating GUI applications.

There are several reasons why Tkinter is a popular choice for GUI programming in Python:

1. Cross-platform compatibility: Tkinter applications can run on different operating systems, including Windows, macOS, and Linux, without requiring significant modifications. This allows developers to create applications that can be used by a wide range of users.
2. Ease of use: Tkinter provides a straightforward and intuitive interface, making it suitable for beginners and experienced developers alike. It offers a high-level API that simplifies the process of creating GUI applications, allowing developers to focus on the functionality rather than the implementation details.
3. Extensibility: Tkinter offers a wide range of customizable widgets and allows developers to create their own custom widgets to meet specific application requirements. This gives developers the flexibility to create unique and tailored user interfaces.

## **Creating a basic Tkinter window:**

Once Tkinter is installed, you can create a basic Tkinter window by following these steps:

1. Import the necessary modules: Start by importing the `tkinter` module, usually aliased as `tk`, which provides the main functionality for creating GUI applications.
2. Create a Tkinter window object: Use the `Tk()` constructor to create a new window object. This window serves as the main container for all the GUI elements.
3. Add widgets to the window: Use various Tkinter widgets, such as buttons, labels, and entry fields, to add interactive elements to the window. These widgets allow users to input data, view information, and perform actions.
4. Run the Tkinter application: Call the `mainloop()` method on the window object to start the event loop, which handles user interactions and updates the GUI interface accordingly.

```python
import tkinter as tk

root = tk.Tk()
root.mainloop()
```

With these steps, you can create a basic Tkinter window and begin building more complex GUI applications. Tkinter provides extensive documentation and examples that can help you explore its features and create interactive and visually appealing applications.

### **Tkinter Frame:**

In Tkinter, a `Frame` is a container widget that can be used to group and organize other widgets. It acts as a rectangular region on the screen where you can place other widgets such as buttons, labels, or entry fields.

A `Frame` provides a way to logically group related widgets together, making the GUI layout more organized and easier to manage. You can think of a `Frame` as a window within a window, allowing you to create separate sections or areas within your main application window.

To create a `Frame` in Tkinter, you can use the `tkinter.Frame` class and pass the parent widget as an argument. The parent widget is the widget under which the `Frame` will be placed.

Here is an example of creating a `Frame` in Tkinter:

```python
import tkinter as tk

root = tk.Tk()

# Create a Frame
frame = tk.Frame(root)
frame.pack()

# Add widgets to the Frame
label = tk.Label(frame, text="This is a Label")
label.pack()

button = tk.Button(frame, text="Click Me")
button.pack()

root.mainloop()

```

In this example, we create a `Frame` and place it within the `root` window. Then, we add a `Label` and a `Button` to the `Frame`. The `pack()` method is used to automatically position and size the widgets within the `Frame`.

### **Tkinter Grid:**

Tkinter provides the `grid()` method, which allows you to create a grid-based layout for organizing widgets in rows and columns. The `grid()` method provides more control over the placement and alignment of widgets compared to the `pack()` method.

To use the `grid()` method, you need to specify the row and column positions for each widget. By default, the first row and column have an index of 0. You can also specify the number of rows and columns a widget should span using the `rowspan` and `columnspan` parameters.

Here is an example of using the `grid()` method in Tkinter:

```python
import tkinter as tk

root = tk.Tk()

# Create widgets
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")

# Position widgets using grid
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

root.mainloop()

```

In this example, we create two `Labels` and two `Buttons` and position them using the `grid()` method. The `row` and `column` parameters determine the position of each widget in the grid.

By using the `grid()` method, you have more control over the layout of your GUI, allowing you to create complex and customized arrangements of widgets in rows and columns. More about [Tkinter grid system can be found here](https://www.pythontutorial.net/tkinter/tkinter-grid/).

Let's break down the parameters we will be using today in the **`grid`** method:

1. **`row`**: This parameter specifies the row number in the grid where the widget should be placed. The topmost row is numbered 0, and the row number increases downwards.
2. **`column`**: This parameter specifies the column number in the grid where the widget should be placed. The leftmost column is numbered 0, and the column number increases to the right.
3. **`columnspan`**: This optional parameter specifies the number of columns that the widget will span across. By default, a widget occupies only one column. If you set **`columnspan=2`**, the widget will stretch across two columns.
4. **`rowspan`**: Similar to **`columnspan`**, this optional parameter specifies the number of rows a widget will cover. By default, it's 1, but if set to a higher value, the widget will span multiple rows.
5. **`sticky`**: This parameter is used to specify how the widget should expand within the grid cell. It can take values from the cardinal directions (N, E, S, W) that correspond to North (top), East (right), South (bottom), and West (left). For example, **`sticky=tk.W`** will align the widget to the left (west) side of the cell. If you want the widget to expand and fill the entire cell, you can use **`sticky=tk.N+tk.E+tk.S+tk.W`**.
6. **`padx` and `pady`**: These optional parameters add padding (space) around the widget inside the cell. **`padx`** adds horizontal padding, and **`pady`** adds vertical padding. They can take either a single value (applied to both sides) or a tuple **`(left, right)`** or **`(top, bottom)`** to set different padding on each side.

### Tkinter Image Loader

When the API call returns an image instead of a JSON response, we need to handle it differently in our code. Instead of treating it as JSON data, we need to download the image and load it into Tkinter.

Tkinter provides the `ImageTk` module from the `PIL` library, which allows us to load images into Tkinter-compatible format. We can use the `Image.open()` function from PIL to open the downloaded image, and then convert it to a Tkinter-compatible format using `ImageTk.PhotoImage()`.

Here's an example of how to handle an image response in Tkinter:

```python
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

root = tk.Tk()
root.title("Hello World!")

# Make API call
response = requests.get("https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*")
response.raise_for_status()

# Download the image data
image_data = response.content

# Create a PIL Image object from the image data
pil_image = Image.open(BytesIO(image_data))

# Convert the PIL Image object to a Tkinter-compatible format
tk_image = ImageTk.PhotoImage(pil_image)

# Create a Tkinter Label and set the image
image_label = tk.Label(root, image=tk_image)
image_label.pack()
root.mainloop()
```

In this example, `image_url` is the URL of the image obtained from the API response. We download the image data using the `requests` library and create a PIL `Image` object from it. Then, we convert the PIL `Image` object to a Tkinter-compatible format using `ImageTk.PhotoImage()`. Finally, we create a Tkinter `Label` and set the image using the Tkinter-compatible image.

This allows us to display the image within our Tkinter application.

# Building our first GUI application

Based on the RandomUser API, I want to create an application that generates fictional user information and displays it with Tkinter.

> **************Context**************: As the most successful hacker in Asia, we decided to use our ultimate skill set for good. We have gained unauthorized access to a (fiction) registration database of a Shark Tank-like scam TV Show, which aims to steal people’s business ideas. The database contains information of users who are signed up on the system to enter the show, along with their startup idea, and their favorite life advice that they use to identify their life philosophy with. Now, we are trying to create a simple application that can display a leaked applicant’s info with just a simple button, with the purpose of choosing potential applicant and advising them to withdraw from the show.
> 

We quickly sketches out the idea for our application:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/b6fdcedf-8fb7-4b90-84d0-172562b81092/Untitled.png)

To break down, we can imagine this as a grid (or a table if you’re used to spreadsheets), where the person’s photo will be a cell in the leftmost column and spans across multiple rows.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/e8c5063b-5591-4b1c-bfad-61deb9c98516/Untitled.png)

Using this we can design a grid in Tkinter to store our components. We first create the corresponding labels, with the assigned grid position. For the details, we leave the field blank for now, and will update the labels with their corresponding text content when we call the APIs. Let’s create a file call `app.py`:

```python
# app.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

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

# Button to fetch and update data
fetch_button = ttk.Button(root, text="Leak A User")
fetch_button.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
```

For the APIs, we will be using the RandomUser API from before. But as you may have noticed, we lack the information to use for the Business Proposal and Advice fields. For those, we will be using the *[It’s this for that* API](https://itsthisforthat.com/api.php) and *[Advice Slip* API](https://api.adviceslip.com/).

To test, if we send a GET request to https://itsthisforthat.com/api.php?json, we will receive:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/57501542-d7ed-4d7f-80e7-45887acff63e/Untitled.png)

Which we can use `data['this'] + ' for ' + data['that']` to create a random business idea.

Next, we can get a random *slip* of advice from https://api.adviceslip.com/advice:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/76c3080c-2292-46ad-bdca-9419beb3c043/Untitled.png)

As good programmers, we create a function to *fetch* the data for each API, and store them in another file called `API.py`:

```python
# API.py
import requests

# Function to fetch the person data
def fetch_person_data():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['results'][0]

def fetch_business_proposal():
    url = "https://itsthisforthat.com/api.php?json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return f"{data['this']} for {data['that']}"

def fetch_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return f'"{data["slip"]["advice"]}"'
```

In the `app.py` module, we can simply import the API fetchers:

```python
from API import fetch_person_data, fetch_business_proposal, fetch_advice
```

Using these newly fetched data, we can write a function which updates all the labels with the updated data:

```python
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
```

Our `[app.py](http://app.py)` module should now look like this:

```python
# app.py
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
```

And our app should now shows:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/1939b001-206f-4f31-b5ed-3be4b89318b4/Untitled.png)

And when we click on the button (your person may vary):

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/69fb67ab-c7a1-4948-a31e-e8cc294e9fb5/Untitled.png)

Ta da! You’ve just created your first Python app with GUI and utilizes web APIs to fetch data! You can now put ************************“Full-stack Software Developer”************************ in your resume ;)

But first, we should clean up our code a bit. Currently, the code is quite messy, with global variables and functions inbetween global statements. I rate this code 3/10 for code hygene!

![download.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/7f883172-6e59-4b71-aeef-54a46497bccf/5ada2520-a1cb-47e5-9bef-a79f0f0ca60c/download.jpg)

<aside>
💡 **Fun fact:** Software engineers often refer to these issues as *code smells*! And software development teams often spend a lot of time and money to clean up remaining code smells before shipping the code to production!

</aside>

 

We can use our knowledge of OOP to better design the structure of our code:

```python
# app_better.py

import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from API import fetch_person_data, fetch_business_proposal, fetch_advice

class UserInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Get User Info")

        self.create_widgets()

    def create_widgets(self):
        self.person_frame = ttk.Frame(self.root, padding="10")
        self.person_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.image_label = ttk.Label(self.person_frame)
        self.image_label.grid(row=0, column=0, rowspan=7)

        self.create_label(self.person_frame, "Full Name:", 0, 1)
        self.name_label = self.create_value_label(self.person_frame, 0, 2)

        self.create_label(self.person_frame, "Date of Birth:", 1, 1)
        self.dob_label = self.create_value_label(self.person_frame, 1, 2)

        self.create_label(self.person_frame, "User Name:", 2, 1)
        self.username_label = self.create_value_label(self.person_frame, 2, 2)

        self.create_label(self.person_frame, "Password:", 3, 1)
        self.password_label = self.create_value_label(self.person_frame, 3, 2)

        self.create_label(self.person_frame, "Business Proposal:", 4, 1)
        self.business_label = self.create_value_label(self.person_frame, 4, 2, wraplength=300)

        self.advice_label = ttk.Label(self.person_frame, text="", wraplength=300, justify=tk.CENTER)
        self.advice_label.grid(row=5, column=1, columnspan=2, padx=10, sticky=(tk.E, tk.W))

        fetch_button = ttk.Button(self.root, text="Leak A User", command=self.update_data)
        fetch_button.grid(row=1, column=0, columnspan=3, pady=10)

    def create_label(self, frame, text, row, column):
        label = ttk.Label(frame, text=text)
        label.grid(row=row, column=column, sticky=tk.W)
        return label

    def create_value_label(self, frame, row, column, **options):
        label = ttk.Label(frame, text="", **options)
        label.grid(row=row, column=column, sticky=tk.W)
        return label

    def update_data(self):
        try:
            person_data = fetch_person_data()
            business_proposal = fetch_business_proposal()
            advice = fetch_advice()

            full_name = f"{person_data['name']['title']} {person_data['name']['first']} {person_data['name']['last']}"
            dob = person_data['dob']['date'][:10]
            user_name = person_data['login']['username']
            password = person_data['login']['password']

            self.name_label.config(text=full_name)
            self.dob_label.config(text=dob)
            self.username_label.config(text=user_name)
            self.password_label.config(text=password)

            self.update_image(person_data['picture']['large'])

            self.business_label.config(text=business_proposal)
            self.advice_label.config(text=advice)
        except Exception as e:
            print(f"Error updating data: {e}")

    def update_image(self, image_url):
        try:
            image_response = requests.get(image_url)
            img = Image.open(BytesIO(image_response.content))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # keep a reference!
        except Exception as e:
            print(f"Error updating image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()
```

Here we have made some improvements which reduced some code smells from our code:

1. **Encapsulation & Modularity**: The code is encapsulated within a class **`UserInfoApp`**, enhancing readability and reusability. By using a class, we encapsulate the functionality and make the code more maintainable.
2. **Function Extraction**: Repeated code for label creation is refactored into **`create_label`** and **`create_value_label`** functions.
3. **Error Handling**: Added **`try-except`** blocks in **`update_data`** and **`update_image`** methods to handle potential exceptions, especially useful for network requests and image processing.

This can already be considered ***good enough*** to leave it here, but in the industry this is still considered not-very-good code. We can still improve it further:

```python
# app_even_better.py
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
```

1. **OOP Structure**: The application is structured using classes. **`UserInfoApp`** is responsible for the UI, **`DataFetcher`** for fetching data, and **`ImageLoader`** for handling image loading.
2. **Stateless Design**: Both **`DataFetcher`** and **`ImageLoader`** are stateless. They provide static methods that perform tasks without relying on or altering shared state.
3. **Encapsulation**: Each class is responsible for a specific aspect of the application. **`UserInfoApp`** manages the UI, **`DataFetcher`** abstracts data fetching, and **`ImageLoader`** is responsible for image processing.
4. **Error Handling**: Both fetching and image loading methods have try-except blocks to handle potential errors.

This approach maintains a clean separation of concerns, with each class handling a specific part of the application's functionality. It also adheres to the principles of OOP while ensuring that methods are stateless and independent.