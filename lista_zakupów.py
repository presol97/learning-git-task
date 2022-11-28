shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
sklepy = ("piekarnia", "warzywniak")
shop_1, shop_2 = sklepy

print("lista zakupów")

for ele in range(0, 1):
    print(" Idę do", shop_1, "i kupuję tam", shopping_list["piekarnia"], "\n", "Idę do", shop_2, "i kupuję tam", shopping_list["warzywniak"]),

pieczywo = len(["chleb", "bułki", "pączek"])
warzywa = len(["marchew", "seler", "rukola"])
zakupy = pieczywo + warzywa
print("w sumie kupuję", zakupy, "produktów")
