import tkinter

#loga izmērs

rows = 25
cols = 25
tile_size = 40

window_width = tile_size * cols
window_height = tile_size * rows

#Skaitīšanas kārtošanas funkcija

def counting_sort(numbers):
    if len(numbers) == 0:
        return []

    #maksimālās un minimālās vērtības

    max_num = max(numbers)
    min_num = min(numbers)

    range_of_elements = max_num - min_num + 1
    count = [0] * range_of_elements
    output = [0] * len(numbers)

    for num in numbers:
        count[num - min_num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(numbers) - 1, -1, -1):
        output[count[numbers[i] - min_num] - 1] = numbers[i]
        count[numbers[i] - min_num] -= 1

    return output

#Funkcija skaitļu parādīšanai uz canvas
def display_numbers(original_numbers, sorted_numbers):
    canvas.delete("all")
    canvas.create_text(10, 10, text="Enter data:", fill="white", anchor="nw")
    for index, num in enumerate(original_numbers):
        canvas.create_text(10, 30 + index * 20, text=num, fill="white", anchor="nw")
    
    #Parādīt sakārtotus skaitļus

    canvas.create_text(10, 30 + len(original_numbers) * 20 + 20, text="Sorted data:", fill="white", anchor="nw")
    for index, num in enumerate(sorted_numbers):
        canvas.create_text(10, 50 + len(original_numbers) * 20 + index * 20 + 20, text=num, fill="white", anchor="nw")

#Funkcija skaitļu šķirošanai

def sort_numbers():
    input_numbers = entry.get().split(",")
    input_numbers = [num.strip() for num in input_numbers]
    
    valid_numbers = []
    for num_str in input_numbers:
        try:
            num = int(num_str)
            valid_numbers.append(num)
        except ValueError:
            print(f"Incorrect data: {num_str}")
    
    sorted_numbers = counting_sort(valid_numbers)
    display_numbers(valid_numbers, sorted_numbers)

#Galvenā loga izveide

window = tkinter.Tk()
window.title("counting sort")
window.resizable(False, False)

#Izveidot canvas, lai parādītu skaitļus

canvas = tkinter.Canvas(window, bg="black", width=window_width, height=window_height)
canvas.pack()

#Datu ievade

canvas.create_text(10, 10, text="Enter data:", fill="white", anchor="nw")
entry = tkinter.Entry(window, width=50)
entry.pack()

#Šķirošanas sākums

sort_button = tkinter.Button(window, text="Sort data: ", command=sort_numbers)
sort_button.pack()

window.mainloop()