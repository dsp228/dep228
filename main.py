count = int(input("Количество видеокарт: "))

cards =[]
for i in range(count):
    card = int(input(f"{i + 1} Видкокарта: "))
    cards.append(card)

print(f"старый список видеокарт: {cards}")

max = max(cards)

new_cards = []
for card in cards:
    if card != max:
        new_cards.append(card)

print(f"Новый список видеокарт: {new_cards}")