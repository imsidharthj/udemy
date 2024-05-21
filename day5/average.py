heights = list(map(int, input().split()))
height = 0
count = 0
for i in heights:
    count = count + 1
    height = height + i
average = height / count
print(f"total height = {height}\nnumber of students = {count}\naverage height = {round(average)}")