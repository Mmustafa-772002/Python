# the 2d list is a list of lists
# the nested loop is a loop inside a loop 
# the 2d list is used to store the data in the form of rows and columns
# the nested loop is used to iterate over the 2d list
number_grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

print(number_grid[2][1])

for row in number_grid:
    print(row)
for row in number_grid:
      for col in row :
          print(col)