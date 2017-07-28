fin = open("words.txt", "r")
count_e = 0
total = 0
for word in fin:
    total += 1
    for letter in word:
        if letter == 'e' or letter == "E":
            count_e += 1
            break

print("total: {}".format(total))
print("total e: {}".format(count_e))
without_e = total - count_e
print("words without e: {}".format(without_e))
print(100 * (without_e / total))
