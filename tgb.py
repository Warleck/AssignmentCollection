'''
S345905 - Markos Johns
Assignment Part C

Unit Code: ICTPRG301
'''

from time import sleep
import sys
def capitalism(word):
    return word[0].upper() + word[1:]       #This function capitalises the first letter of the first word

def countDown(x):
    #This function writes the song out with the corrosponding numbers for each bottle
    #it also makes sure that the second last verse says one gree bottle and not one green bottles.

    cntDn = ""
    wordList = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    while x > 0:
        bottleholder = "bottle"
        if x > 1:
            bottleholder += "s"
        y = x - 1
        bottleholder2 = "bottle"
        if y > 1 or y == 0:
            bottleholder2 += "s"
        cntDn = cntDn + capitalism(wordList[x]) + ' green ' + bottleholder + '\nHanging on the wall\n' + capitalism(wordList[x]) + ' green ' + bottleholder + '\nHanging on the wall\nAnd if one green bottle\nShould accidently fall\nThere\'ll be ' + wordList[y] + ' green ' + bottleholder2 + '\nHanging on the wall \n \n'
        x -= 1
        
    return cntDn

def songwriter(song):
  myFile = open('Ten Green Bottles.txt', 'w')
  myFile.write(song)
  
  myFile.close()
#this part writes the song to at txt file and overwrites any text file thats currently there with the same name and will also create one if none exist



if __name__ == '__main__':
  song = countDown(10)
  songwriter(song)

#This part executes the program.


print("WRITING FILE, PLEASE WAIT", end="")
sys.stdout.flush()                                  #This is the fake loading bar.
sleep(1)

number_of_dots = 5

for i in range(number_of_dots - 1):
    print(".", end="")
    sys.stdout.flush()
    sleep(1)
print(".")

sleep(2)
print("--FILE WRITING COMPLETE--")
