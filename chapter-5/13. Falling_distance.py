#This program calculates fallin distance
#in a given time

def main():
    print('Time(seconds)\tFalling Distance(metres)')
    print('-------------\t-----------------------')
    for values in range(1,11):
        print(' ',values,'\t\t\t',format\
              (calculate_falling_distance(values),'.2f'))
        
def calculate_falling_distance(time):
    distance = (9.8 * time**2)/2
    return distance
main()
