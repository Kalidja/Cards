dealer_names = []

try:
    with open("DealerNames.txt", "r", encoding="utf-8") as file:
        dealer_names = file.read()
except Exception as e:
    print(e)
