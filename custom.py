import common
import random
def polka_box(image_matrix):
    height = len(image_matrix)
    width = len(image_matrix[0])
    center_row = height // 2
    center_col = width // 2

    
    for i in range(random.randint(1,40)):
        center_row = random.randint(25,height-24)
        center_col = random.randint(25,width -24)
    
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for row in range(center_row - 25, center_row + 25):
            for col in range(center_col - 25, center_col + 25):
                image_matrix[row][col] = rand_color
    return image_matrix

my_pic = common.read_file("free-stock.jpg")

custom_filter = polka_box(my_pic)

common.write_file("custom_free-stock.jpg",custom_filter)