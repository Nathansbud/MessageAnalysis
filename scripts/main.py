import os
import json

path = "/Users/zackamiton/Desktop"
directory = os.listdir(path)




read_file = open("/Users/zackamiton/Desktop/PRITHVI_MESSAGE_OUTPUT.txt", "r")
write_file = open("/Users/zackamiton/Desktop/SORTED_MESSAGES.txt", "r+")
freq_file = open("/Users/zackamiton/Desktop/FREQUENCY_MESSAGES.txt", "r+")
freq_sorted_file = open("/Users/zackamiton/Desktop/MESSAGES_SORTED_BY_FREQUENCY.txt", "r+")
final_freq_sorted_file = open("/Users/zackamiton/Desktop/MESSAGES_SORTED_FOR_REAL.txt", "r+")


# def move_all_subdirectory_files(file_name, new_name, file_extension):
#     i = 1
#
#     for f in directory:
#         if f != ".DS_Store":
#             new_path = os.listdir(path + "/" + f)
#
#             for s in new_path:
#                 if s == file_name:
#                     os.rename(path + "/" + f + "/" + file_name, move_path + "/" + new_name + "_" + str(i) + file_extension)
#                     i += 1

def json_parse():
    for files in directory:
        print(files)
        if files != ".DS_Store":
            with open(path + "/" + files) as f:
                data = json.load(f)

            for m in data["messages"]:
                if "sender_name" in m and "content" in m:
                    if m["sender_name"] == "Prithvi Rajaram Subrahmanyam":
                        line = m["content"].encode('utf-8')
                        write_file.write(line + "\n")


def cut_spaces():
    words = []

    for f in read_file.readlines():
        f = f.replace(" ", "\n")
        words.append(f.lower())

    words.sort()

    for w in words:
        write_file.write(w)



def read_in_and_sort():
    words = []

    for line in freq_sorted_file.readlines():
        words.append(line.lower().replace(" ", ""))

    words.sort()

    for w in words:
        final_freq_sorted_file.write(w)

#
def create_frequency_from_read_file():
    count = 0
    l = write_file.readline().rstrip("\n")

    for line in write_file.readlines():
        line = line.rstrip("\n")
        if l != line:
            freq_file.write(l + ", " + str(count) + "\n")
            count = 0

        count+=1
        l = line

def sort_by_frequency():
    for line in freq_file.readlines():
        index = line.rfind(" ")
        freq_line = line[index+1:].rstrip("\n") + ", " + line[:index - 1]
        freq_sorted_file.write(freq_line + "\n")










# cut_spaces()

read_in_and_sort()
# sort_by_frequency()

read_file.close()
write_file.close()
freq_file.close()
freq_sorted_file.close()
final_freq_sorted_file.close()

# json_parse()

if __name__ == '__main__':
    pass
