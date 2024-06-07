import threading
import os

def longest(fn):
    dct1 = dict()
    lst_w,lst_c = [],[]
    with open(fn, "r") as file:
        for i in file.read().split():
            lst_w.append(i)
            lst_c.append(len(i))
    print(f"Most longest word in {fn}: {lst_w[lst_c.index(max(lst_c))]}")

def main():
    threads = []
    for i in os.listdir():
        t = threading.Thread(target=longest, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Program was ended")

if __name__ == "__main__":
    main()

