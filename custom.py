import common
import random
def polka_box(image_matrix):
    height = len(image_matrix)
    width = len(image_matrix[0])
    center_row = height // 2
    center_col = width // 2
    size_of_dot = 10
    #random.randint(50,70)
    for i in range(random.randint(100,150)):
        center_row = random.randint((size_of_dot//2),height-(size_of_dot//2)-1)
        center_col = random.randint((size_of_dot//2),width -(size_of_dot//2)-1)
    
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for row in range(center_row - (size_of_dot//2), center_row + (size_of_dot//2)):
            for col in range(center_col - (size_of_dot//2), center_col + (size_of_dot//2)):
                image_matrix[row][col] = rand_color
    return image_matrix

my_pic = common.read_file("free-stock.jpg")

custom_filter = polka_box(my_pic)

common.write_file("custom_free-stock.jpg",custom_filter)