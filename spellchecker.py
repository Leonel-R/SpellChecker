# write your solution here
text = input("Write text:")
parts = text.split()
word_bank = []
with open("wordlist.txt") as file:
    for line in file:
        word = line.strip()
        word_bank.append(word)
for check in parts:
    if check.lower() not in word_bank:
        print(f"*{check}* ",end="")
    else:
        print(f"{check} ", end="")
