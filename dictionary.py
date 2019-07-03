##this is a latest Oxford dictionary made in python by Rounak.

import requests
from bs4 import BeautifulSoup as bs
def search(query):
    query = query.lower()
    url = "https://en.oxforddictionaries.com/definition/" + query.replace(" ", "+")
    try:
        r= requests.get(url, timeout=10)
    except:
        return print("Please check your internet connection.")
    soup = bs(r.text, "lxml")
    try:
        pos = soup.findAll("span", {"class": "pos"})
        print(f"Parts of Speach: {pos[0].text}")
        data = soup.findAll("span", {"class": "ind"})
        ex = soup.findAll("div", {"class": "ex"})
    except:
        return print("Word not found!")  
    print(f"\nDefinition of {query}:\n")
    for (i, results) in enumerate(data):
        print(str(i + 1), ". ",data[i].text)
        if i == 4:
            break
    print(f"\nExamples of {query}:\n")
    for (i, results) in enumerate(ex):
        print(str(i + 1), ". ",ex[i].text)
        if i == 4:
            break
    print("\n" * 2)
if __name__ == "__main__":
    print("Oxford Dictionary Coded in Python by Rounak\n")
    while True:
        quary = input("What You want to search!\n")
        search(quary)

