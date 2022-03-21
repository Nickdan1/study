import arcade
import random
def main():
    our_color = [arcade.color.LAVENDER,arcade.color.BLUE,
                 arcade.color.GREEN,arcade.color.BOSTON_UNIVERSITY_RED,
                 arcade.color.ORANGE,arcade.color.ATOMIC_TANGERINE,arcade.color.YELLOW]
    arcade.open_window(800,600,"file editing")
    joke_open = open("house.txt", "r")
    all_lines = joke_open.readlines()

    arcade.start_render()
    for line in all_lines:
        rec_data = line.split(",")
        center_x = int(rec_data[0])
        center_y = int(rec_data[1])
        width = int(rec_data[2])
        height = int(rec_data[3])
        color = random.choice(our_color)
        rectangle = arcade.create_rectangle(center_x,center_y,width,height,color)
        rectangle.draw()

    arcade.finish_render()
    arcade.run()
main()
