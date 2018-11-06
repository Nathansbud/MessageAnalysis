import os
import json

path = "/Users/zackamiton/GitHub/MessageAnalysis/data/Sanitized Files"
directory = os.listdir(path)

read_file = open(path + "/COMBINED_MESSAGE_OUTPUT.txt", "r")
write_file = open(path + "/SORTED_MESSAGE_OUTPUT.txt", "w")

i = 0
words = []

for line in read_file.readlines():
    words.append(line)
    i+=1

words.sort()

for s in words:
    write_file.write(s)

read_file.close()
write_file.close()



#
# for f in directory:
#     os.rename(os.path.join(path, f), os.path.join(path, "MESSAGE_" + str(i)+'.json'))
#     i = i+1
#
# for files in directory:
#     with open(files) as f:
#         data = json.load(f)
#
#     for m in data["messages"]:
#         if "sender_name" in m and "content" in m:
#             if m["sender_name"] == "Zachary Amiton":
#                 line = m["content"].encode('utf-8')
#                 write_file.write(line + "\n")






if __name__ == '__main__':
    pass
