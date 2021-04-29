from os import system

#clears cache at boot
#system('rm -rf ~/.cache')


i = 0   #temporary exit condition
while i<1:
    #writes the current time to a text file, then store it in a variable '''time'''
    system('echo $(date +%R) > date.txt')
    fp = open('date.txt', 'r')
    time = fp.read()
    #close the file
    fp.close()
    #take hours and minutes and makes them integers
    h = int(time[:2])
    m = int(time[3:])

    if h > 8:
        sleep
    print(h, m)

    i += 1   #momentary exit from while loop
#print(f'the time is: {time}')
