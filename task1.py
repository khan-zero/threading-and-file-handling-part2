import threading
import os

def ct_letters(fn):
    with open(fn, "r") as file:
        count = len(file.read())
        #print(file.read())
        #print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    print(f"count of letters in {fn}: {count}")

def main():
    threads = []
    for i in os.listdir():
        t = threading.Thread(target=ct_letters, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Program was ended")

if __name__ == "__main__":
    main()

