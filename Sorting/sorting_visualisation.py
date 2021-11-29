import pygame
colourList = [(239, 69, 69), (239, 86, 69), (239, 103, 69), (239, 120, 69), (239, 137, 69), (239, 154, 69), (239, 171, 69), (239, 188, 69), (239, 205, 69), (239, 222, 69), (239, 239, 69), (222, 239, 69), (205, 239, 69), (188, 239, 69), (171, 239, 69), (154, 239, 69), (137, 239, 69), (120, 239, 69), (103, 239, 69), (86, 239, 69), (69, 239, 69), (69, 239, 86), (69, 239, 103), (69, 239, 120), (69, 239, 137), (69, 239, 154), (69, 239, 171), (69, 239, 188), (69, 239, 205), (69, 239, 222), (69, 239, 239), (69, 222, 239), (69, 205, 239), (69, 188, 239), (69, 171, 239), (69, 154, 239), (69, 137, 239), (69, 120, 239), (69, 103, 239), (69, 86, 239), (69, 69, 239), (86, 69, 239), (103, 69, 239), (120, 69, 239), (137, 69, 239), (154, 69, 239), (171, 69, 239), (188, 69, 239), (205, 69, 239), (222, 69, 239), (239, 69, 239), (239, 69, 222), (239, 69, 205), (239, 69, 188), (239, 69, 171), (239, 69, 154), (239, 69, 137), (239, 69, 120), (239, 69, 103), (239, 69, 86)]
numberList = [30,4,5,6,36,38,37,32,17,19,8,10,56,50,20,13,14,40,58,21,43,51,1,31,41,16,60,22,34,28,9,12,42,2,27,18,26,47,39,24,57,23,46,53,15,25,7,33,49,59,35,44,45,11,54,29,55,52,3,48]
black = (0,0,0)
def draw_list(display, numbers, y_offset = 10):
    """
    Update the display by displaying the rectangles. Does not update
    :param display: The display to be updated
    :param numbers: The list that is to be displayed
    """
    for i in range(len(numbers)):
        pygame.draw.rect(display,colourList[numbers[i] - 1],[i * 20, y_offset, 20,numbers[i] + 10]) #Height of rectangles are linked to number

def draw_left_right(display, left_arr, right_arr, y):
    """
    Draw the two arrays on the same rows, with a gap in between them
    :param display: The surface
    :param left_arr: The left array
    :param right_arr: The right array
    :param y: The y co-ordinate of the row
    """
    x = 0
    for num in left_arr:
        pygame.draw.rect(display, colourList[num - 1], [x * 20, y, 20, num + 10])
        x += 1
    x += 3 #Leave a gap in between the two arrays
    for num in right_arr:
        pygame.draw.rect(display, colourList[num - 1], [x * 20, y, 20, num + 10])
        x += 1

def check_quit():
    """
    Function to check if there is an event in pygame events that corresponds to a break
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return True
        elif event.type == pygame.K_q:
            pygame.quit()
            return True


def visualise_bubble(numbers):
    pygame.init()  # Start pygame
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((1200, 200))
    n = len(numbers)
    exit = False
    try:
        while not exit:
            while n > 1:
                for i in range(n - 1):
                    temp = numbers[i]
                    if temp > numbers[i + 1]:
                        numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]
                        gameDisplay.fill(black)
                        draw_list(gameDisplay, numbers)
                        pygame.display.update()
                        clock.tick(50) #Since each individual swap is being shown, it is necessary to have a high FPS
                exit = check_quit()
                if exit: break #If the user wants to stop, break the loop. Check_quit() will quit pygame internally
                n -= 1
            exit = True
    except: #If any error occurs in pygame
        print("Error occurred")
    finally:
        pygame.quit()
        input("Press any key to exit...")

def visualise_insertion(nums, FPS = 10):
    n = len(nums)
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((1200, 200))
    try:
        for j in range(1, n):
            next_num = nums[j]
            i = j - 1  # Set i to the index before j
            while i >= 0 and nums[i] > next_num:  # Move the element to the correct place
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = next_num  # Move next_num to the place where the while loop stopped
            display.fill(black)
            draw_list(display,nums)
            pygame.display.update()
            clock.tick(FPS)
            if check_quit(): break #Break the for loop
    except:
        print("Error occurred")
    finally:
        pygame.quit()

def visualise_merge_sort(numbers, FPS = 5):
    """
    Bottom up approach to mergesort
    :param numbers: The list to be sorted
    """
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((1200, 1200))
    display.fill(black)
    draw_list(display, numbers) #Initially, draw the entire list
    pygame.display.update()
    clock.tick(FPS)

    n = len(numbers)
    high = n - 1 #Last index
    current_size = 1
    while current_size < high:
        for start in range(0, n - 1, 2 * current_size):  # Iterate from 0 to n-1, with steps of 2*current_size
            mid = start + current_size - 1 #The point from which left_arr stops and right_arr starts
            end = min((start + 2 * current_size - 1), high)
            n1 = mid - start + 1  # Size of the left array
            n2 = end - mid  # The size of the right array
            # Populate the left_arr and right_arr arrays
            left_arr = [0] * n1
            right_arr = [0] * n2
            for i in range(0, n1):
                left_arr[i] = numbers[start + i]
            for i in range(0, n2):
                right_arr[i] = numbers[mid + i + 1]

            #Show the full list and the left and right sub-arrays

            left_i = 0
            right_i = 0
            temp = [] #List to show the merging taking place
            while left_i < len(left_arr) and right_i < len(right_arr):
                if left_arr[left_i] <= right_arr[right_i]:
                    temp.append(left_arr[left_i])
                    left_i += 1
                else:
                    temp.append(right_arr[right_i])
                    right_i += 1
                display.fill(black) #Reset the display
                draw_list(display, numbers) #Draw the main array
                draw_list(display,temp, y_offset=100) #Upper list, to be merged to
                draw_left_right(display, left_arr[left_i:], right_arr[right_i:], y=200) #The two lists being merged, displaying only the elements that have not been merged into upper list
                pygame.display.update()
                clock.tick(FPS)
            while left_i < len(left_arr): #If there are elements are left over in the left side
                temp.append(left_arr[left_i])
                left_i += 1
                display.fill(black)
                draw_list(display, numbers)
                draw_list(display, temp, y_offset=100)
                draw_left_right(display, left_arr[left_i:], right_arr[right_i:], y=200)
                pygame.display.update()
                clock.tick(FPS)
            while right_i < len(right_arr): #If there are elements left over
                temp.append(right_arr[right_i])
                right_i += 1
                display.fill(black)
                draw_list(display, numbers)
                draw_list(display, temp, y_offset=100)
                draw_left_right(display, left_arr[left_i:], right_arr[right_i:], y=200)
                pygame.display.update()
                clock.tick(FPS)
            assert len(temp) == end - start + 1
            for i in range(len(temp)):
                numbers[start + i] = temp[i]
        current_size *= 2  # Double the size of the sub-array (1,2,4,8,16,...)
    return numbers




if __name__ == "__main__":
    #visualise_bubble(numberList)
    #print(len(colourList))
    visualise_merge_sort(numberList)
    #visualise_insertion(numberList)