A = input('Enter your full name')
a = int(input('Enter the number of at bats'))
b = int(input('Enter the number of singles'))
c = int(input("enter the number of doubles"))
d = int(input('Enter the number of triples'))
f = int(input('Enter the number of home runs'))

Av_bat = (b + c + d + f) / a
SLG = ((b * 1) + (c * 2) + (d * 3) + (f * 4)) / a
Total_bats = (b + c + d + f)
print('The player', A, " had :", Total_bats, b, c, d, f)
print('His batting average was', Av_bat)
print('his slugging percentage was', SLG)
