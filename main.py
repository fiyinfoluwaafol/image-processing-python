import copy
import common

def blur(image_matrix):
    image_matrix_copy = copy.deepcopy(image_matrix)
    for i in range(2,len(image_matrix_copy)-2):
        for j in range(2,len(image_matrix_copy[i])-2):
            pixel = image_matrix_copy[i][j]
            top_top1 = image_matrix_copy[i-2][j-2]
            top_top2 = image_matrix_copy[i-2][j-1]
            top_top3 = image_matrix_copy[i-2][j]
            top_top4 = image_matrix_copy[i-2][j+1]
            top_top5 = image_matrix_copy[i-2][j+2]
            top_left = image_matrix_copy[i-1][j-1]
            top = image_matrix_copy[i-1][j]
            top_right = image_matrix_copy[i-1][j+1]
            right_right2 = image_matrix_copy[i-1][j+2]
            right_right3 = image_matrix_copy[i][j+2]
            right_right4 = image_matrix_copy[i+1][j+2]
            right_right5 = image_matrix_copy[i+2][j+2]
            right = image_matrix_copy[i][j+1]
            bottom_right = image_matrix_copy[i+1][j+1]
            bottom_bottom4 = image_matrix_copy[i+2][j+1]
            bottom_bottom3 = image_matrix_copy[i+2][j]
            bottom_bottom2 = image_matrix_copy[i+2][j-1]
            bottom_bottom1 = image_matrix_copy[i+2][j-2]
            bottom = image_matrix_copy[i+1][j]
            bottom_left = image_matrix_copy[i+1][j-1]
            left_left4 = image_matrix_copy[i+1][j-2]
            left_left3 = image_matrix_copy[i][j-2]
            left_left2 = image_matrix_copy[i-1][j-2]
            left = image_matrix_copy[i][j-1]
            avg_red = int((pixel[0]+top_left[0]+top[0]+top_right[0]+right[0]+bottom_right[0]+bottom[0]+bottom_left[0]+left[0]+top_top1[0]+top_top2[0]+top_top3[0]+top_top4[0]+top_top5[0]+right_right2[0]+right_right3[0]+right_right4[0]+right_right5[0]+bottom_bottom1[0]+bottom_bottom2[0]+bottom_bottom3[0]+bottom_bottom4[0]+left_left2[0]+left_left3[0]+left_left4[0])/25)
            avg_blue = int((pixel[1]+top_left[1]+top[1]+top_right[1]+right[1]+bottom_right[1]+bottom[1]+bottom_left[1]+left[1]+top_top1[1]+top_top2[1]+top_top3[1]+top_top4[1]+top_top5[1]+right_right2[1]+right_right3[1]+right_right4[1]+right_right5[1]+bottom_bottom1[1]+bottom_bottom2[1]+bottom_bottom3[1]+bottom_bottom4[1]+left_left2[1]+left_left3[1]+left_left4[1])/25)
            avg_green = int((pixel[2]+top_left[2]+top[2]+top_right[2]+right[2]+bottom_right[2]+bottom[2]+bottom_left[2]+left[2]+top_top1[2]+top_top2[2]+top_top3[2]+top_top4[2]+top_top5[2]+right_right2[2]+right_right3[2]+right_right4[2]+right_right5[2]+bottom_bottom1[2]+bottom_bottom2[2]+bottom_bottom3[2]+bottom_bottom4[2]+left_left2[2]+left_left3[2]+left_left4[2])/25)
            image_matrix[i][j][0] = avg_red
            image_matrix[i][j][1] = avg_green
            image_matrix[i][j][1] = avg_blue

    return image_matrix

my_pic = common.read_file("free-stock.jpg")

blur_filter = blur(my_pic)

common.write_file("blurrier_free-stock.jpg",blur_filter)