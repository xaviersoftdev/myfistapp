hours = int(input('Please enter hours: '))
minutes = int(input('Please enter minutes: '))
second = int(input('Please enter seconds: '))
day_selec = input('Please select between [PM/AM]: ')
day_selec = day_selec.upper()
if hours == 12:
    hours = 0
if day_selec == 'PM':
    hours = hours + 12
calcula_total = hours * 3600 + minutes * 60 + second
print('This is total seconds: %s' %calcula_total)
