# widgets = ['1', '2', '3', '4', '5', '6', '7' , '8', '9', '*', '0', '#']

# index = 0

# while index < len(widgets):
#     widget = widgets[index]
#     if index % 3 == 0 and index !=0:
#         print()
#     print(widget.center(3, " "), end="")
#     index += 1
# else:
#     print()

# for i in widgets:
#     if widgets.index(i) % 3 == 0 and widgets.index(i) != 0:
#         print()
#     print(i.center(3), end="")

widgets = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'], 
    ['*', '0', '#']
]
for block in widgets:
    for stroke in block:
        print(stroke.center(3, " "), end="")
    print("")
