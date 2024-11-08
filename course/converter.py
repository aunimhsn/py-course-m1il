KMH_TO_MPH = 1.609

speed_kmh = float(input('Veuillez saisir une vitesse en kmh : '))
speed_mph = speed_kmh / KMH_TO_MPH

# print(f'{speed_kmh} km/h = {round(speed_mph, 2)} mph')
print(f'{speed_kmh} km/h = {speed_mph:.2f} mph')

