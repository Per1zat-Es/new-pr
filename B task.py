membership_type = input("Введите тип членства (золото, серебро, обычный): ").lower()

purchase_amount = float(input("Введите сумму покупки: $"))


discount = 0

if membership_type == "золото":
    if purchase_amount > 100:
        discount = 20
    else:
        discount = 10
elif membership_type == "серебро":
    if purchase_amount > 100:
        discount = 15
    else:
        discount = 5
elif membership_type == "обычный":
    if purchase_amount > 100:
        discount = 5
else:
    print("Неверный тип членства.")
    exit()

discounted_price = purchase_amount * (1 - discount / 100)

print(f"Скидка: {discount}%")
print(f"Цена после скидки: ${discounted_price:.2f}")
