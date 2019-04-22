import json
import shutil
import os
import re

import datetime

def move_all_facebook_subdirectory_files(path, new_path, file_name, new_name):
    i = 0

    for f in os.listdir(path):
        if f != ".DS_Store":
            for s in os.listdir(path + "/" + f):
                if s.endswith(".json"):
                    i+=1
                    shutil.copy(path + "/" + f + "/" + s, new_path + "/" + "MESSAGE_" + str(i) + ".json")
                if s.endswith("photos"):
                    shutil.rmtree(path + "/" + f + "/photos")
                if s.endswith("audio"):
                    shutil.rmtree(path + "/" + f + "/audio")
                if s.endswith("videos"):
                    shutil.rmtree(path + "/" + f + "/videos")
                if s.endswith("files"):
                    shutil.rmtree(path + "/" + f + "/files")
                if s.endswith("gifs"):
                    shutil.rmtree(path + "/" + f + "/gifs")

def json_parse(path, source_file, sender):
    write_file = open(source_file, "w+")
    dated_file = open("/Users/zackamiton/Desktop/Output Files/DATED_MESSAGES.txt", "w+")

    for files in os.listdir(path):
        if files != ".DS_Store":
            with open(path + "/" + files) as f:
                data = json.load(f)

                for m in data["messages"]:
                    if "sender_name" in m and "content" in m:
                        if m["sender_name"] == sender:
                            c = m["content"].encode('latin1').decode('utf-8')
                            write_file.write(c + "\n")
                            dated_file.write(datetime.datetime.utcfromtimestamp((m["timestamp_ms"] + 19800000)/1000).strftime("%Y-%m-%d %H:%M:%S") + ", " + c.lower().replace("\n", " ") + "\n")
    write_file.close()
    dated_file.close()



def cut_spaces_and_sort(source_file):
    words = []
    wordier = []
    write_file = open(source_file, "r+")

    for f in write_file.readlines():
        f = re.sub("(P?http.+?($|\s))|[^a-zA-Z0-9'\-]", " ", f) #not even sure if this is working but pattern match for http and every character (.) up to end of the "word" (space match) or string, ($ | \s) is the pattern that does both (match a or b), and replace with space.
        words.append(f.lower().split())


    for w in words:
        for a in w:
            wordier.append(a)

    wordier.sort()

    write_file = open(source_file, "w+")

    for w in wordier:
        write_file.write(w + "\n")

def returnFirst(elem):
    return int(elem[:elem.find(",")])
def sortDate(elem):
    return elem[:elem.find(",")]


def make_frequency_file(source_file):
    count = 0
    words = []
    write_file = open(source_file, "r+")

    l = write_file.readline().rstrip("\n")

    for line in write_file.readlines():
        line = line.rstrip("\n")
        if l != line:
            words.append(str(count) + ", " + l)
            count = 0

        count += 1
        l = line

    words.sort(reverse=True, key=returnFirst)
    write_file = open(source_file, "w+")

    for w in words:
        write_file.write(w + "\n")

    write_file.close()

def make_dated_file(source_file):
    words = []
    write_file = open(source_file, "r+", encoding="utf-8")

    for line in write_file.readlines():
        words.append(line.rstrip("\n").replace("\n", " "))

    words.sort(reverse=True, key=sortDate)

    write_file = open(source_file, "w+", encoding="utf-8")

    for w in words:
        write_file.write(w + "\n")

    write_file.close()


#Data Handling Order:
# - Move All
# - JSON Parse
# - Cut Space & Sort
# - Make Frequency
#




if __name__ == "__main__":
    move_all_facebook_subdirectory_files("/Users/zackamiton/Desktop/messages/Inbox", "/Users/zackamiton/Desktop/Moved Files", "message_1.json", "MESSAGE")
    json_parse("/Users/zackamiton/Desktop/Moved Files", "/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt", "Zachary Amiton")
    cut_spaces_and_sort("/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt")
    make_frequency_file("/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt")
    make_dated_file("/Users/zackamiton/Desktop/Output Files/DATED_MESSAGES.txt")
    pass
