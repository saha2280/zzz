##

from tkinter import *
import time
import random


game_width = 500
game_height = 500
snake_item = 10
snake_color1 = "red"
snake_color2 = "yellow"
snake_x=24
snake_y=24
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 5

virtual_game_x = game_width/snake_item 
virtual_game_y = game_height/snake_item

tk =Tk()
tk.title("игра змейка на Python")
tk.resizable (0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

present_color1 = "blue"
present_color2 = "black"
presents_list = []
presents_size = 5
for i in range(presents_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x*snake_item,y*snake_item,x*snake_item+snake_item,y*snake_item+snake_item,fill=present_color2)
    id2 = canvas.create_oval(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=present_color1)
    presents_list.append([x, y, id1, id2])
print(presents_list)
  

def snake_paint_item(canvas, x, y) :
    global snake_list
    id1 = canvas.create_rectangle(x*snake_item,y*snake_item,x*snake_item+snake_item,y*snake_item+snake_item,fill=snake_color2)
    id2 = canvas.create_rectangle(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=snake_color1)
    snake_list.append([x,y,id1,id2])
    print(snake_list)

snake_paint_item(canvas, snake_x, snake_y)

def check_can_we_delete_snake_item():
    if len (snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])

def check_if_we_found_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            #print("found!!!")
            snake_size = snake_size + 1
        #print(snake_x, snake_y)

def snake_move(event):
    global snake_x
    global snake_y
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav 
    snake_paint_item(canvas, snake_x, snake_y)
    check_if_we_found_present()

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)
