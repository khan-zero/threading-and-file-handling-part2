import requests, threading
import os

def download_image(url, fn):
    dct1 = dict()
    res = requests.get(url)
    if res.status_code == 200:
        with open(fn, "wb") as file:
            file.write(res.content)
        print(f"Image downloaded to {fn} succesfully")
    else:
        print("Failed to download")
        
def main(url, path):

    t = threading.Thread(target=download_image, args=(url, path))
    t.start()
    t.join()

    print("Program was ended")

if __name__ == "__main__":
    main(input("Please enter the url: "), input("and save path: "))
