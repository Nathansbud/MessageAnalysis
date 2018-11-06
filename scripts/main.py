import os

directory = os.listdir("/Users/zackamiton/Desktop/Messages 2")
os.chdir("/Users/zackamiton/Desktop/Messages 2")
i = 1
write_file = open("MESSAGE_OUTPUT.txt", 'w')

for f in write_file.readlines():
    print(f)

write_file.close();


if __name__ == '__main__':
    pass
