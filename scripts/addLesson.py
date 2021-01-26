def getDate():
    d = input('Enter the date of the lesson (mm/dd/yyyy): ')

    return d

def getStandards():
    s = input('Enter the standards: ')

    return s

def getVideoLinks():
    l = input('Enter the video links, separated by commas: ')

    return l

def getLesson():
    w = input('Enter the lesson name: ')

    return w

data = []
lesson = []

running = input('Ready to enter a lesson? (y or n) ')
if running == 'y':
    running = True
else:
    running = False

while running:
    lesson.append(getDate())
    lesson.append(getStandards())
    lesson.append(getLesson())
    lesson.append(getVideoLinks())

    print(lesson)
    dataCheck = input('Does the data look correct? (y or n) ')

    while dataCheck == 'n':
        if dataCheck == n:
            print('What is incorrect?')
            print('1. Date')
            print('2. Standards')
            print('3. Lesson')
            print('4. Video')
            errLoc = int(input())

        if errLoc == 1:
           lesson[0] = getDate()
        elif errLoc == 2:
           lesson[1] = getStandards()
        elif errLoc == 3:
           lesson[2] = getLesson()
        elif errLoc == 4:
           lesson[3] = getVideoLinks()


        print(lesson)
        dataCheck = input('Does the data look correct? (y or n) ')


    running = input('Ready to enter a lesson? (y or n) ')
    if running == 'y':
        running = True
    else:
        running = False
