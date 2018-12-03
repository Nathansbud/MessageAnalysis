import json
import shutil
import os
import matplotlib.pyplot as plt
import numpy as np
import re

import datetime

colors = [
    "FF0000",
    "FF7F00",
    "FFFF00",
    "00FF00",
    "0000FF",
    "8B00FF",
]

def move_all_facebook_subdirectory_files(path, new_path, file_name, new_name):
    i = 1

    for f in os.listdir(path):
        if f != ".DS_Store":
            for s in os.listdir(path + "/" + f):
                if s == file_name:
                    os.rename(path + "/" + f + "/" + file_name, path + "/" + f + "/" + new_name + "_" + str(i) + ".json")
                    shutil.copy(path + "/" + f + "/" + new_name + "_" + str(i) + ".json", new_path)
                    i+=1
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
       
        words.append(f.replace("\"", "").lower().split())


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



def swear_count(source_file):
    swear_dict = [
        "ass",
        "bitch",
        "crap",
        "cunt",
        "damn",
        "dick",
        "hell",
        "fuck",
        "shit",
    ]
    sc = [0]*swear_dict.__len__()

    read_file = open(source_file, "r+")
    for l in read_file.readlines():
        s = l[l.find(",")+2:].rstrip("\n")

        for i in range(swear_dict.__len__()):
            if swear_dict[i] in s:
                if l[:l.find(",")-1] != "":
                    sc[i] += int(l[:l.find(",")])

    read_file.close()

    for i in range(swear_dict.__len__()):
        print(swear_dict[i] + ": " + str(sc[i]))

    plt.figure()
    plt.title("Swearing on Facebook", y=1.08)
    # plt.plot(sc)

    barlist = plt.bar(swear_dict, sc)

    for i in range(barlist.__len__()):
        barlist[i].set_color("#"+colors[i % colors.__len__()])


    plt.colormaps()
    plt.xticks(rotation=45)


    plt.ylabel("Frequency")
    plt.xlabel("Swears")
    plt.show()
def most_used_words(source_file):
    words = []
    counts = []
    labels = []

    read_file = open(source_file, "r+")
    for r in read_file.readlines():
        words.append(r)

    words.sort(reverse=True, key=returnFirst)
    top_used = words[0:25]
    top_used.reverse()

    for i in range(top_used.__len__()):
        counts.append(top_used[i][:top_used[i].find(",")])

    for l in top_used:
        labels.append(l[l.find(",")+2:])



    plt.figure()

    plt.figure()
    plt.title("Most Used Words", y=1.08)
    # plt.yscale("linear")
    plt.yticks(np.arange(1, 25, 4))


    barlist = plt.bar(labels, counts)


    for i in range(barlist.__len__()):
        barlist[i].set_color("#" + colors[i % colors.__len__()])

    # plt.yticks(np.arange(start=0, stop=30000, step=6000))
    plt.xticks(rotation=90)

    plt.ylabel("Frequency")
    plt.xlabel("Words")


    plt.show()
def fucks_per_time(source_file, word):
    read_file = open(source_file, "r+")
    swear_file = open("/Users/zackamiton/Desktop/Output Files/SWEAR_MESSAGES.txt", "w+")


    for w in read_file.readlines():
        if w.count(word) > 0:
            swear_file.write(w.rstrip("\n").strip("\n") + ", " + str(w.count(word)) + "\n")

    swear_file = open("/Users/zackamiton/Desktop/Output Files/SWEAR_MESSAGES.txt", "r+")

    dates = []
    counts = []

    line = swear_file.readline()
    count = 0





    # for t in read_file.readlines():

    total_count = 0

    for l in swear_file.readlines():
        if line[:7] != l[:7]:
            dates.append(line[:7])

            counts.append(count)
            count = 0
            total_count = 0

        count += int(l[l.rfind(",")+2:])
        total_count += line.split(" ").__len__()
        line = l


    dates.reverse()
    counts.reverse()


    for i in range(dates.__len__()):
        print(dates[i] + ", " + str(counts[i]))

    plt.figure()
    plt.title("Ability to Give a Fuck", y=1.08)

    plt.plot(dates, counts, "#FF0000")

    # plt.pcolor("#FF00FF")

    plt.xticks(rotation=90)

    plt.ylabel("Fucks Given")
    plt.xlabel("Months")

    plt.show()


#Data Handling Order:
# - Move All
# - JSON Parse
# - Cut Space & Sort
# - Make Frequency
#
move_all_facebook_subdirectory_files("/Users/zackamiton/Desktop/messages", "/Users/zackamiton/Desktop/Moved Files", "message.json", "MESSAGE")
json_parse("/Users/zackamiton/Desktop/Moved Files", "/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt", "Zachary Amiton")
cut_spaces_and_sort("/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt")
make_frequency_file("/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt")
make_dated_file("/Users/zackamiton/Desktop/Output Files/DATED_MESSAGES.txt")


fucks_per_time("/Users/zackamiton/Desktop/Output Files/DATED_MESSAGES.txt", "fuck")
swear_count("/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt")
most_used_words("/Users/zackamiton/Desktop/Output Files/PARSED_MESSAGES.txt")




if __name__ == "__parser__":
    pass
