import pygame as pg
import random
import time

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

def stop_funct():
    for event in pg.event.get():
        if event.type != pg.KEYDOWN:
            continue
        if event.key == pg.K_SPACE:
            return True
    return False

def draw_text(text, size, txt_color, x, y):
    text_font = pg.font.SysFont("Comic Sans", size)
    img = text_font.render(text, True, txt_color)
    screen.blit(img, (x, y))

def return_random_list(len = 100):
    list_a = []
    for _ in range(len):
        list_a.append(random.randint(1, 601))
    return list_a

def return_reversed_list(len = 100):
    list_a = [] 
    for i in range(1, len+1):
        list_a.append(i*6)
    return list_a[::-1]

def return_pyramid_list(len = 100):
    list_a = [None] * len
    pointer_a = 0
    pointer_b = len - 1

    for i in range(1, len+1):
        if i%2 == 0:
            list_a[pointer_a] = i*6
            pointer_a += 1
        else:
            list_a[pointer_b] = i*6
            pointer_b -= 1
    return list_a

def return_pyramid_inverted_list(len = 100):
    list_a = [None] * len
    pointer_a = len // 2 - 1
    pointer_b = len  // 2 

    for i in range(1, len+1):
        if i%2 == 0:
            list_a[pointer_a] = i*6
            pointer_a -= 1
        else:
            list_a[pointer_b] = i*6
            pointer_b += 1
    return list_a

def return_random_list_few_different(len = 100):
    list_a = []
    for _ in range(len):
        list_a.append(random.randint(1, 6)*100)
    return list_a

def return_higher_lower_list(len = 100):
    list_a = [] 
    for i in range(0, len):
        if i%2 == 0:
            list_a.append((i+2)*6)
        else:
            list_a.append(i*6)
    return list_a

def draw_list(lista, index=-10, red=[]):
    z = 50
    pg.draw.rect(screen, (0, 0, 0), (50, 50, 900, 620))
    pg.time.wait(10)
    for i in range(len(lista)):
        if i == index:
            pg.draw.rect(screen, (0, 255, 0), (z, 670-lista[i], 9, lista[i]))
        elif i in red:
            pg.draw.rect(screen, (255, 0, 0), (z, 670-lista[i], 9, lista[i]))       
        else:
            pg.draw.rect(screen, (255, 255, 255), (z, 670-lista[i], 9, lista[i]))
        z+=9
    pg.display.update()



def bubble_sort(list_a):
    for i in range(len(list_a)-1):
        was_changed = False
        for j in range(len(list_a) - 1 - i):
            
            if (list_a[j] > list_a[j+1]):
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                was_changed = True
            draw_list(list_a, j+1, [j])
            if stop_funct():
                return
        if not was_changed:
            break

def selection_sort(list_a):
    size = len(list_a)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if list_a[j] < list_a[min_index]:
                min_index = j
            draw_list(list_a, i, [j,min_index])
            if stop_funct():
                return
        (list_a[i], list_a[min_index]) = (list_a[min_index], list_a[i])

def insertion_sort(list_a):
    n = len(list_a)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        if stop_funct():
            return
        
        key = list_a[i] 
        j = i-1
        draw_list(list_a, i)
        while j >= 0 and key < list_a[j]:
            
            list_a[j+1] = list_a[j]
            draw_list(list_a, i, [j])
            j -= 1
        list_a[j+1] = key

def bogo_sort(list_a):
    while not sorted(list_a) == list_a:
        random.shuffle(list_a)
        draw_list(list_a)
        if stop_funct():
            break

def merge_sort(list_a):
    list_b = list_a.copy()
    list_c = []
    def mergeSort(arr_a):
        if len(arr_a) > 1:
            mid = len(arr_a)//2
            left_arr = arr_a[:mid]
            right_arr = arr_a[mid:]
 
            mergeSort(left_arr)
            mergeSort(right_arr)
            
            for _ in range(len(left_arr)+len(right_arr)):
                list_c.pop()
            
            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                x = list_c+arr_a[:k]+left_arr[j:]+right_arr[i:]+list_b[len(list_c)+len(left_arr)+len(right_arr):]
                
                draw_list(x, k+len(list_c), [i+len(list_c), j+len(list_c)+len(right_arr)])
                if left_arr[i] <= right_arr[j]:
                    arr_a[k] = left_arr[i]
                    i += 1
                else:
                    arr_a[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                x = list_c+arr_a[:k]+left_arr[i:]+right_arr[j:]+list_b[len(list_c)+len(left_arr)+len(right_arr):]
                
                draw_list(x, k+len(list_c), [j+len(list_c)+len(right_arr)])
                arr_a[k] = left_arr[i]
                i += 1
                k += 1
 
            while j < len(right_arr):
                x = list_c+arr_a[:k]+left_arr[i:]+right_arr[j:]+list_b[len(list_c)+len(left_arr)+len(right_arr):]
                
                draw_list(x, k+len(list_c), [i+len(list_c)])
                arr_a[k] = right_arr[j]
                j += 1
                k += 1
            list_c.extend(arr_a)
        else:
            list_c.extend(arr_a)
            
    mergeSort(list_a)

def quick_sort(list_a):

    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]
                
                draw_list(lst, j, [i])
            else:
                draw_list(lst, j, [])
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        
        draw_list(lst, -10, [i, j])
        return i + 1
 
    def quickSort(lst, low, high):
        if low < high:
            p = partition(lst, low, high)
            quickSort(lst, low, p - 1)
            quickSort(lst, p + 1, high)

    quickSort(list_a, 0, len(list_a) - 1)

def main():
    lst = return_random_list()
    draw_list(lst)
    time_to_sort = 0.0
    running = True
    sorting = False
    sorting_method = "bubble"
    screen.fill((120,120,120))
    
    while running:
        draw_list(lst)
        draw_text("Key Functions: ", 30, (0,0,0), 975, 50)
        draw_text("Randomization Patterns: ", 20, (0,0,0), 1000, 90)
        draw_text("1. Random Array", 20, (0,0,0), 1010, 110)
        draw_text("2. Reversed Array", 20, (0,0,0), 1010, 130)
        draw_text("3. Pyramid", 20, (0,0,0), 1010, 150)
        draw_text("4. Inverse Pyramid", 20, (0,0,0), 1010, 170)
        draw_text("5. Mostly The Same", 20, (0,0,0), 1010, 190)
        draw_text("6. Almost Sorted", 20, (0,0,0), 1010, 210)
        draw_text("Sorting Algorithms: ", 20, (0,0,0), 1000, 230)
        draw_text("Q. Bubble Sort", 20, (0,255,0) if sorting_method == "bubble" else (0,0,0), 1010, 250)
        draw_text("W. Insertion Sort", 20, (0,255,0) if sorting_method == "insertion" else (0,0,0), 1010, 270)
        draw_text("E. Selection Sort", 20, (0,255,0) if sorting_method == "selection" else (0,0,0), 1010, 290)
        draw_text("R. Merge Sort", 20, (0,255,0) if sorting_method == "merge" else (0,0,0), 1010, 310)
        draw_text("T. Quick Sort", 20, (0,255,0) if sorting_method == "quick" else (0,0,0), 1010, 330)
        draw_text("Y. Bogo Sort", 20, (0,255,0) if sorting_method == "bogo" else (0,0,0), 1010, 350)
        draw_text("Other Functions: ", 20, (0,0,0), 1000, 370)
        draw_text("SPACE. Start/Stop Sort", 20, (0,0,0), 1010, 390)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if pos[0] >= 1230 and pos[1] <= 50:
                    running = False
                elif (pos[0] >= 1180 and pos[1] <= 50): 
                    pg.display.toggle_fullscreen()
                    screen.fill((120,120,120))

            if event.type == pg.QUIT:
                running = False

            if event.type != pg.KEYDOWN:
                continue
            if event.key == pg.K_1 and not sorting:
                lst = return_random_list()
            elif event.key == pg.K_2 and not sorting:
                lst = return_reversed_list()
            elif event.key == pg.K_3 and not sorting:
                lst = return_pyramid_list()
            elif event.key == pg.K_4 and not sorting:
                lst = return_pyramid_inverted_list()
            elif event.key == pg.K_5 and not sorting:
                lst = return_random_list_few_different()
            elif event.key == pg.K_6 and not sorting:
                lst = return_higher_lower_list()
            elif event.key == pg.K_q and not sorting:
                sorting_method = "bubble"
            elif event.key == pg.K_w and not sorting:
                sorting_method = "insertion"
            elif event.key == pg.K_e and not sorting:
                sorting_method = "selection"
            elif event.key == pg.K_r and not sorting:
                sorting_method = "merge"
            elif event.key == pg.K_t and not sorting:
                sorting_method = "quick"
            elif event.key == pg.K_y and not sorting:
                sorting_method = "bogo"
            elif event.key == pg.K_SPACE and not sorting:
                screen.fill((120,120,120))
                sorting = True

        if sorting:
            start_time = time.time()
            if sorting_method == "bubble":
                bubble_sort(lst)
            elif sorting_method == "insertion":
                insertion_sort(lst)
            elif sorting_method == "selection":
                selection_sort(lst)
            elif sorting_method == "bogo":
                bogo_sort(lst)
            elif sorting_method == "merge":
                merge_sort(lst)
            elif sorting_method == "quick":
                quick_sort(lst)
            time_to_sort = round(time.time() - start_time, 2)
            sorting = False

        pg.draw.rect(screen, (255, 0, 0), (1230, 0, 50, 50))
        pg.draw.rect(screen, (0, 0, 255), (1180, 0, 50, 50))
        pg.draw.rect(screen, (255, 255, 255), (1185, 5, 40, 40), 2)
        draw_text("x", 30, (255,255,255), 1247, 0)
        draw_text("Time to sort(s): "+str(time_to_sort), 30, (0,0,0), 50, 670)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()