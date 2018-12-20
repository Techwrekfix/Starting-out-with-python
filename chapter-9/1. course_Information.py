#This proram is about course information

#Algorithm in pseudocode
#1.The create_dictionary function creates three different
#  dictionaries(Room_number,Instructor and Meeting_time) and
#  returns a refrence to the dictionaries
#
#2. Inside the main fucntion:
#       1.ask user enter a course number
#       2.if user input is in room_number and instructor and meeting_time:
#               displays their values in the dictionary


#CODE

def create_dictionary():
    room_number = {'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244,
                   'CM241':1411}
    
    instructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich',
                 'NT110':'Burke','CM241':'Lee'}

    meeting_time = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.',
                    'CS103':'10:00 a.m.','NT110':'11:00 a.m.',
                    'CM241':'1:00 p.m.'}
                 
    return room_number,instructor,meeting_time

def main():
    room_number,instructor,meeting_time = create_dictionary()
    
    course_number = input('Please enter a course number: ')

    #determine if course number is in dictionary
    if course_number in room_number and instructor and meeting_time:
        print('Room Number:',room_number[course_number])
        print('Instructor:',instructor[course_number])
        print('Meeting Time:',meeting_time[course_number])
    else:
        print('Entry not found')
        
main()
    
