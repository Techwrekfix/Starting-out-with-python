#This program calculates assement of property taxes

def main():
    property_value = float(input('Enter the actual value of the property: '))
    assessment_value = calculate_assessment_value(property_value)
    property_tax = calculate_property_tax(assessment_value)

    #Displaying the assessment value and property tax
    print('The assessment value of the property = $'\
          ,format(assessment_value,',.2f'),'\nThe property tax '\
          'on the assessment value = $',format(property_tax,',.2f'),sep='')

#Defining the assessment value funtion
def calculate_assessment_value(property_value):
    value = 0.6 * property_value
    return value
#Defining the property tax function
def calculate_property_tax(assessment_value):
    tax = (assessment_value * 0.72) / 100
    return tax
main()
