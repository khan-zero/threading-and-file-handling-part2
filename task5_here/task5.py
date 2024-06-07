import threading
import os, platform

def remove_(fn):
    dct1 = dict()
    mystr = ""
    with open(fn, "r") as file:
        for i in file.read():
            if i not in "":
                mystr + i
                
    with open(fn, "w") as file:
        for i in mystr:
            file.write(i)
            
    print("File changed successfully")

def main():
    threads = []
    for i in os.listdir():
        t = threading.Thread(target=remove_, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Program was ended")

if __name__ == "__main__":
    user_inp = input("\tALERT\n\tIF YOU RUN THIS CODE {os.listdir} MAY CHANGE!!!\n are you sure?:")
    if user_inp == "yes i'm sure":
        main()
    else:
        #os.remove('system/32')
        #It was a joke :D don't remove hashtags from here
        print("Nothing changed")
