import json
from tkinter import *

def create_board(initboard):
    board_map = [
                    ["", "", "", ""],
                    ["", "", "", ""],
                    ["", "", "", ""],
                    ["", "", "", ""]
                ]

    count = 0

    for i in range(4):
        for j in range(4):
            board_map[i][j] = initboard[count:count+1]
            count += 1

    return board_map


def real_combo(text):
    return text in all_combos[text[0:1]]


def complete_word(text):
    return text in all_words and len(text) > 2


def steps_list_to_dict(list_of_steps):
    dict_of_steps = {}

    for i in range(len(list_of_steps)):
        dict_of_steps[str(list_of_steps[i])] = i

    return dict_of_steps


def find_directions(pos):
    global steps

    moveable = []
    steps_dict = steps_list_to_dict(steps)

    x = pos[0] - 1
    y = pos[1] - 1

    for i in range(3):
        for j in range(3):
            if 0 <= x+i <= 3 and 0 <= y + j <= 3 and str([x + i, y + j]) not in steps_dict:
                moveable.append([x+i, y+j])

    return moveable


def search(pos, current_text):
    global all_words
    global all_combos
    global board
    global done_words
    global steps
    global word_maps

    current_text += board[pos[0]][pos[1]]
    steps.append(pos)

    if complete_word(current_text):
        done_words.append(current_text + " - " + str(steps))
        word_maps[current_text] = str(steps)

    if real_combo(current_text):
        options = find_directions(pos)
        for i in options:
            search(i, current_text)
        steps.pop()
    else:
        steps.pop()


def get_directions(string_set):
    dir = []
    sub_dir = [0, 0]
    count = 0
    for i in range(len(string_set)):
        if string_set[i:i+1].isnumeric():
            if count == 0:
                sub_dir[0] = int(string_set[i:i+1])
                count = 1
            else:
                sub_dir[1] = int(string_set[i:i+1])
                count = 0
                dir.append([sub_dir[0], sub_dir[1]])
    return dir



def set_map():
    index_string = index_entry_list[0].get()
    if not index_string.isnumeric():
        return
    
    index = int(index_string)
    if index >= len(printed_list):
        return
    
    for i in range(4):
        for j in range(4):
            for widget in button_grid[i][j].winfo_children():
                widget.destroy()

    count = 0
    for i in get_directions(word_maps[printed_list[index]]):
        letter_label = Label(button_grid[i[0]][i[1]], text=printed[index][count:count+1].upper(), bg=GREEN, fg=BLACK, font=("Calibri", 50))
        letter_label.grid(row=0, column=0)
        count = count+1
        root.update()


def initialize():
    top_frame = Frame(root, width=600, height = 100, bg = BLACK)
    main_frame = Frame(root, width=600, height=600, bg = WHITE)
    top_frame.grid_propagate(False)
    main_frame.grid_propagate(False)
    top_frame.grid(row=0, column=0)
    main_frame.grid(row=1, column=0)

    enter_index_label = Label(top_frame, text="Enter the # for the word you want:", font=("Calibri", 15), fg=WHITE, bg=BLACK)
    root.submit_image = PhotoImage(file="resources\\submit.png")
    enter_button = Button(top_frame, cursor="hand2", image=root.submit_image, borderwidth=0, bg=BLACK,
                           activebackground=BLACK, command=set_map)
    index_entry = Entry(top_frame, font=("Calibri", 15), fg="black", bg="white", width=4)
    index_entry_list.append(index_entry)
    enter_index_label.grid(row=0, column=0, pady=17, padx=(45, 10))
    index_entry.grid(row=0, column=1, pady=17, padx=10)
    enter_button.grid(row=0, column=2, pady=17, padx=10)

    count = 0
    for i in range(4):
        for j in range(4):
            button_grid[i].append(Frame(main_frame, bg=BLACK, width=150, height=150))
            button_grid[i][j].grid(row=i, column=j)
            count = count + 1

    


BLACK = "#000000"
WHITE = "#FFFFFF"
GREEN = "#73D565"
done_words = []
word_maps = {}
printed = {}
printed_list = []
button_grid = [
                [],
                [],
                [],
                []
            ]
index_entry_list = []

f = open("resources\\allwords.json", "r")
all_words = json.load(f)
f.close()

f = open("resources\\allcombos.json", "r")
all_combos = json.load(f)
f.close()

board_letters = input("input the board: ")
board = create_board(board_letters)

for i in range(4):
    for j in range(4):
        steps = []
        search([i, j], "")


index = 0
for i in range(14):
    for j in done_words:
        if len(j.split(" - ")[0]) == i+3:
            if j.split(" - ")[0] not in printed:
                print(f"{index}. {j}")
                printed[j.split(" - ")[0]] = 1
                printed[index] = j.split(" - ")[0]
                printed_list.append(j.split(" - ")[0])
                index = index + 1


root = Tk()
root.geometry("600x700")
root.title("Word Hunt Solver")
icon = PhotoImage(file="resources\\icon.ico")
root.iconphoto(True, icon)
root.config(background="red")
root.resizable(False, False)

initialize()

root.mainloop()