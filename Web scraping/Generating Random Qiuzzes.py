# This program file creates quizzes with questions and answers
# in random order, along with the answer key

# the keys are the states and values are their capitals
import random
capitals = {'Alabama': 'Montgomery', 
            'Alaska': 'Juneau',
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock',
            'California': 'Sacramento', 
            'Colorado': 'Denver', 
            'Connecticut': 'Hartford',
            'Delaware': 'Dover',
            'Florida': 'Tallahassee', 
            'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu',
            'Idaho': 'Boise',
            'Illinois': 'Springfield',
            'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines',
            'Kansas': 'Topeka',
            'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 
            'Maine': 'Augusta', 
            'Maryland': 'Annapolis',
            'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 
            'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 
            'Missouri': 'Jefferson City', 
            'Montana': 'Helena', 
            'Nebraska': 'Lincoln', 
            'Nevada': 'Carson City',
            'New Hampshire': 'Concord',
            'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 
            'New York': 'Albany', 
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 
            'Ohio': 'Columbus', 
            'Oklahoma': 'Oklahoma City', 
            'Oregon': 'Salem', 
            'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 
            'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 
            'Tennessee': 'Nashville', 
            'Texas': 'Austin', 
            'Utah': 'Salt Lake City', 
            'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 
            'Washington': 'Olympia',
            'West Virginia': 'Charleston', 
            'Wisconsin': 'Madison', 
            'Wyoming': 'Cheyenne'}

# Generating teh 35 files
for quizNum in range(35):
    # create the quiz and anzwer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answeKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')
    
    #write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    
# Loop through all 50 states, ataching eah question to the answers
for questionNum in range(50):
    
    #getting the correct and wrong answers
    correctAns = capitals[states[questionNum]]
    wrongAns = list(capitals.values())
    
    del wrongAns[wrongAns.index(correctAns)]
    wrongAns = random.sample(wrongAns, 3)
    ansOptions = wrongAns + [correctAns]
    random.shuffle(ansOptions)

    # write the question and answer options ti the quiz file
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
    
    for i in range(4):
        quizFile.write('   %s. %s\n' % ('ABCD'[i], ansOptions[i]))
    quizFile.write('\n')
    
    # writing the answer key to a file
    answeKeyFile.write('%s. %sn' % (questionNum + 1, 'ABCD'[ansOptions.index(correctAns)]))
quizFile.close()
answeKeyFile.close()





















