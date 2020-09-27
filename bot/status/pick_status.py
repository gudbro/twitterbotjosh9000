from random import choice, shuffle


# ---------------------------------------------------------------------------- #
def pick_status():
    status_options = [
        "Ping! Mutualan RT aja",
        "Ping! mutualan yuk, rt aja. jfb y!!",
        "Ping! Mutualan kuy rt aja yah",
        "Ping! yug mutualan rt aja yap",
        "Ping! Yg suka jbjb mutualan skuy. Rt aja",
        "Ping! mutualan yuk sm nak esema xixixi",
        "Ping! mutualan kuy rt aje dn ku ad emot",
        "Ping! mutualan yuk! tp aku kpop stan jg. rt aja yaa",
        "Ping! Rt for mutualan -f15",
        "Ping! Mutualan kuy rt aja ya -f",
        "Ping! gaess mutualan yukk rt aja yaa",
        "Ping! mutualan yukk. yang ga masalah aku suka jbjb,rep/rt aja yaa",
        "Ping! mutualan yuk dn aku ada",
        "Ping! mutualan? Rt, auto fb yaaw",
        "Ping! yu mutualan RT aja yaa yg suka jbjb sini mampir langsung FB yaw",
        "Ping! darpada gabut mending kita mutualan aja, di rt aja yups"
    ]
    shuffle(status_options)
    return choice(status_options)


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    pick_status()