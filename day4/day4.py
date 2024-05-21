line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().upper()
# column_map = {'A': 0, 'B': 1, 'C': 2}
# column = column_map[position[0]]
# row = int(position[1]) - 1
# map[row][column] = "X"
map_cordinates = {
    "A1":(0, 0), "B1":(0, 1), "C1":(0, 2),
    "A2":(1, 0), "B2":(1, 1), "C2":(1, 2),
    "A3":(2, 0), "B3":(2, 1), "C3":(2, 2)
}
row, item = map_cordinates[position]
map[row][item] = "X"
print(f"{line1}\n{line2}\n{line3}")