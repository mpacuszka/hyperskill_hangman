scores = input().split()
# put your python code here
correct, incorrect = 0, 0
for score in scores:
    if score == "C":
        correct += 1
    elif score == "I":
        incorrect += 1
    if incorrect == 3:
        print("Game over")
        break
else:
    print("You won")
print(correct)
