import matplotlib.pyplot as plt

colors = [
    "FF0000",
    "FF7F00",
    "FFFF00",
    "00FF00",
    "0000FF",
    "8B00FF",
]


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
    sc = [0] * swear_dict.__len__()

    read_file = open(source_file, "r+")
    for l in read_file.readlines():
        s = l[l.find(",") + 2:].rstrip("\n")

        for i in range(swear_dict.__len__()):
            if swear_dict[i] in s:
                if l[:l.find(",") - 1] != "":
                    sc[i] += int(l[:l.find(",")])

    read_file.close()

    for i in range(swear_dict.__len__()):
        print(swear_dict[i] + ": " + str(sc[i]))

    plt.figure()
    plt.title("Swearing on Facebook", y=1.08)
    # plt.plot(sc)

    barlist = plt.bar(swear_dict, sc)

    for i in range(barlist.__len__()):
        barlist[i].set_color("#" + colors[i % colors.__len__()])

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
        labels.append(l[l.find(",") + 2:])

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