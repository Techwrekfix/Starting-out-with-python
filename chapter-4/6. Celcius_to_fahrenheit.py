#This program converts Celcius temperature to Fahrenheit

print('Celcius Temperature\tFahrenheit Equilvalent')
print('-------------------\t----------------------')
#using loop to display the table
for celcius in range(21):
    fahrenheit = format((9/5)*celcius + 32,'.2f')
    print('\t',celcius,'\t\t\t',fahrenheit)
