""" https://anapioficeandfire.com/"""

# import tkinter as tk
# import requests

# window = tk()
# window.geometry("500x500")
# window.title("test")

# enteruser = Entry(window, font="Arial, 12")
# submit_button = Button(window, text="Submit Data", font="Arial, 12", bg="yellow")
# testlabel = Label(window, font="Arial, 12")


import requests

def test(temptest):
    url = f"https://anapioficeandfire.com/api/books/{temptest}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data!", response.status_code)
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "isbn": data["isbn"],
        "authors": data["authors"],
        "number_of_pages": data["numberOfPages"],
        "publisher": data["publisher"],
        "released": data["released"],
        "characters": data["characters"],
        "pov_characters": data["povCharacters"]
    }

testv1 = test(1)
print(testv1)

