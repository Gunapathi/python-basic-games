import random

word_list = ["ardvark", "baloon", "camel"]
chosen_word = random.choice(word_list)
print(f"chosen word is {chosen_word}")

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
total_life = 6
while not end_of_game:
    print(f"Remaining life {total_life}")
    guess = input("Guess a word ").lower()

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        total_life -= 1
        if total_life == 0:
            end_of_game = True
            print("You Loose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win.")