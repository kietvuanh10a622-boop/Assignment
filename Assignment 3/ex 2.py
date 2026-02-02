while True:
 inches = float(input('Enter inches: '))
    
 if inches < 0 :
        print('The value is negative, program ends')
        break
 
 cm = inches*2.54
 print(f'{inches} inches = {cm} cm')



