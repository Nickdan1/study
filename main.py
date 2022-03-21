import arcade
import random
def main():

    #print(float(5+8))
    #print(int(5+8))
    #print(int(5//10))
    #print(float(5/10))
    #print(int(5*10))
    #An object is simply a collection of
    #data (variables) and methods (functions) that act on those data.
    #Similarly, a class is a blueprint for that object.
    list1 = [7,4,5,7,1,8,9,23,7,34,75,87]
    print(list1[:2],list1[0],list1[9:])
    loop1 = open("house.txt", "r")
    all_lines = loop1.readline()
    arcade.open_window(800,900,"house",True)
    arcade.start_render()
    
    arcade.open_window(800,900,"house",True)

    arcade.start_render()
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
