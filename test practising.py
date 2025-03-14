#imports
import random
import time
import math
#variable list

#starter questions
showing_capabilites = input("would you like to see what you can do? Y/N \n")
if showing_capabilites == "y":
    print("you can practise tables by putting (tables)")
    print("you can practise spellings by putting (words)")
else:
    print("\nok\n")
cleanup = str(input("\ndo you want to do?\n"))
#/starter questions

#tables
if cleanup == "tables":
    #/end of starter
    many_times_tables = int(input("how many times do you want to do this? :"))
    for i in range(many_times_tables):
        randomtablesnumber1 = random.randint(1,10)
        randomtablesnumber2 = random.randint(1,10)
        correct_table = randomtablesnumber2 * randomtablesnumber1
        answertables = int(input(f"what is {randomtablesnumber1} x {randomtablesnumber2} :"))
        if answertables == correct_table:
            print ("you got it right!\n")
        else:
            print("u got it wrong dummy\n")
            time.sleep("1.5")
#/tables

#words

elif cleanup == "words":
    print("here ya go\n")
    grade = 0
    filler_str = "filler string"
    filler_int = 10
    #/variable

    #imports
    language = str(input("what are you doing english or irish "))
    many_times = int(input("how many times do you want to practise this (eg) 50 , 100, 200 :"))
#/words or tables
if language == "english":

    jumbled_word1 = input("put jumbled english word1 : ")
    jumbled_word2 = input("put jumbled english word2 : ")
    jumbled_word3 = input("put jumbled english word3 : ")
    jumbled_word4 = input("put jumbled english word4 : ")
    jumbled_word5 = input("put jumbled english word5 : ")
    jumbled_word6 = input("put jumbled english word6 : ")
    english_word1 = input("put correct spelling word1 : ")
    english_word2 = input("put correct spelling word2 : ")
    english_word3 = input("put correct spelling word3 : ")
    english_word4 = input("put correct spelling word4 : ")
    english_word5 = input("put correct spelling word5 : ")
    english_word6 = input("put correct spelling word6 : ")
    #/variable questions for english

    if language == "english":
        for i in range(int(many_times)):
            number6english = random.randint(1,6) 
            if number6english == 1:
                    answer = input("how do you spell in english " + str(jumbled_word1) + "\n: ")
                    if answer == english_word1:
                        print("correct good job\n")
                    else:
                        print(f"sorry you got it wrong the correct answer is {english_word1}")
            elif number6english == 2:
                answer = input("how do you spell in english " + str(jumbled_word2) + "\n: ")
                if answer == english_word2:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {english_word2}")
            elif number6english == 3:
                answer = input("how do you spell in english " + str(jumbled_word3) + "\n: ")
                if answer == english_word3:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {english_word3}")
            elif number6english == 4:
                answer = input("how do you spell in english " + str(jumbled_word4) + "\n: ")
                if answer != english_word4:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {english_word4}")
            elif number6english == 5:
                answer = input("how do you spell in english" + str(jumbled_word5) + "\n: ")
                if answer == english_word5:
                    print(f"sorry you got it wrong the correct answer is {english_word4}")
            elif number6english == 5:
                answer = input("how do you spell in english" + str(jumbled_word5) + "\n: ")
                if answer == english_word5:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {english_word5}")
            elif number6english == 6:
                answer = input("how do you spell in english " + str(jumbled_word6) + "\n : ")
                if answer == english_word6:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {english_word6}")
        time.sleep(1)
#above is english under is irish
if language == "irish":
    word1 = input("put english word1 : ")
    word2 = input("put english word2 : ")
    word3 = input("put english word3 : ")
    word4 = input("put english word4 : ")
    word5 = input("put english word5 : ")
    word6 = input("put english word6 : ")
    irish_word1 = input("put irish word1 : ")
    irish_word2 = input("put irish word2 : ")
    irish_word3 = input("put irish word3 : ")
    irish_word4 = input("put irish word4 : ")
    irish_word5 = input("put irish word5 : ")
    irish_word6 = input("put irish word6 : ")
    if language == "irish":
        for i in range(int(many_times)):
            number6irish = random.randint(1,6) 
            if number6irish == 1:
                    answer = input("how do you spell in english " + str(word1) + "\n: ")
                    if answer == irish_word1:
                        print("correct good job\n")
                    else:
                        print(f"sorry you got it wrong the correct answer is {irish_word1}")
            elif number6irish == 2:
                answer = input("how do you spell in english " + str(word2) + "\n: ")
                if answer == irish_word2:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {irish_word2}")
            elif number6irish == 3:
                answer = input("how do you spell in english " + str(word3) + "\n: ")
                if answer == irish_word3:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {irish_word3}")
            elif number6irish == 4:
                answer = input("how do you spell in english " + str(word4) + "\n: ")
                if answer != irish_word4:
                        print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {irish_word4}")
            elif number6irish == 5:
                answer = input("how do you spell in english" + str(word5) + "\n: ")
                if answer == irish_word5:
                    print(f"sorry you got it wrong the correct answer is {irish_word5}")
            elif number6irish == 6:
                answer = input("how do you spell in english " + str(word6) + "\n : ")
                if answer == irish_word6:
                    print("correct good job\n")
                else:
                    print(f"sorry you got it wrong the correct answer is {irish_word6}")
        time.sleep(1)
        # end of questions for 6
    # end of irish
    #end of all words for 6

#/words
