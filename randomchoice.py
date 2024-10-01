import random


alternative_list = []

# Fråga användaren hur många alternativ de vill mata in
amount_alternative = int(input("How many alternatives do you have?: "))

# Samla in alternativen från användaren
for i in range(amount_alternative):
    alternativ = input(f"Input alternative {i + 1}: ")
    alternative_list.append(alternativ)

# Slumpa fram ett alternativ
slumpat_val = random.choice(alternative_list)
print(f"The randomly selected alternative is: {slumpat_val}")

