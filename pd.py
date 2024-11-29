import tkinter

rows = 25
cols = 25
tile_size = 40

window_width = tile_size * cols
window_height = tile_size * rows
class tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("sort")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = window_width, height = window_height)
canvas.pack()
window.update()

numbers = input("Enter data: ").split()
numbers = [int(num) for num in numbers]
numbers.sort()

def binary_search(sorted_array, x):
    min_index = 0
    max_index = len(sorted_array)
    while len(sorted_array) > 1:
        middle = (min_index + max_index) // 2
        if sorted_array[middle] > x:
            max_index = middle
        elif sorted_array[middle] < x:
            min_index = middle
        else:
            return middle
        
print(numbers)
print(binary_search(numbers, 1000))

window.mainloop()