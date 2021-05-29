score_input = int(input())
max_score_input = int(input())

percentage = score_input / max_score_input

if 0.9 <= percentage <= 1:
    print("A")
elif percentage>=0.8:
    print("B")
elif percentage>=0.7:
    print("C")
elif percentage>=0.6:
    print("D")
else:
    print("F")