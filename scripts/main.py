import os
import json

path = "/Users/zackamiton/GitHub/MessageAnalysis/data/Safe Files"
directory = os.listdir(path)

read_file = open(path + "/SORTED_MESSAGE_OUTPUT.txt", "r")
write_file = open(path + "/SORTED_MESSAGE_OUTPUT_2.txt")
freq_file = open(path + "/FREQUENCY_MESSAGE_OUTPUT.txt", "r+")

def read_in_and_sort():
    words = []

    for line in read_file.readlines():
        words.append(line.lower())

    words.sort()

    for w in words:
        write_file.write(w)

def create_frequency_from_read_file():
    count = 0
    l = read_file.readline().rstrip("\n")

    for line in read_file.readlines():
        line = line.rstrip("\n")
        if l != line:
            freq_file.write(l + ", " + str(count) + "\n")
            count = 0

        count+=1
        l = line


read_file.close()
freq_file.close()
write_file.close()

if __name__ == '__main__':
    pass
