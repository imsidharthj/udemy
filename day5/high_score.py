scores = [int(i) for i in input().split()]
max_score = scores[0]
for score in scores[1:]:
    if score > max_score:
        max_score = score
print("The highest score in the class is: ", max_score)
