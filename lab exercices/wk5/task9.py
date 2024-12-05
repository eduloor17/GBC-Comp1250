for i in range(1, 21):
    # skip the number 6 and 13
    if i <= 5 or (7 <= i <= 12) or i >= 14:
        print(i, end=" - ")