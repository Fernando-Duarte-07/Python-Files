Kilometers = float(input("Enter kilometers per hour"))

MPH = Kilometers * 0.621371

print(Kilometers, "Kilometers/hour =", f'{MPH:0.2f}')

Aussie_price = float(input("Enter Aussie price"))
US_price = Aussie_price * 0.68350
print("$", Aussie_price, 'Aussie price = ', '$%0.2f' % US_price)