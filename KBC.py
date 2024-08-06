print("Welcome to KBC")
print("Here are the rules : \nfirst you will the the questions on the screen \nyou will provide the answers and then will provide you the correct answer")
print("Lets start")
print("First Question :\n In which Year did india got its freedon ? \n A.1920 B.1927 C.1943 D. 1947")
answer1 = input("Enter your Answer:")
if answer1 == '1947':
    print("Answer is correct")
    print("Next question")
    print("Second question : When was the first independence war fought ? \nA.1857 B.1709 C.1876 D.1899")
    answer2 = input("Enter you answer : ")
    if answer2 == "1857":
        print("Answer is correct")
        print("Next question")
        print("Third question : In which year the constitution on india formed ? \n A.1951 B.1957 C.1965 D.1948" )
        answer3 = input("Enter your Answer:")
        if answer3 == '1951':
            print("Answer is correct")
            print("Next question")
            print("Fourth question : In which year bhagat shingh died ? \n A.1920 B.1937 C.1921 D.1923" )
            answer4 = input("Enter your Answer:")
            if answer4 == '1923':
                print("Answer is correct")
                print("Next question")
                print("fifth question : In which year Mahatma Gandhi died ? \n A.1930 B.1937 C.1951 D.1948" )
                answer5 = input("Enter your Answer:")
                if answer5=='1948':
                    print("Answer is correct")
                    print("You correctly answered all questions")
                    print("YOU HAVE WON 1 LAKH RUPEES !!! ENJOY !!!")
                    input("Press enter to close") 
                else:
                    print("Answer is incorrect, you win only 50,000 Rupees for correctly answering the first,Second,third & fourth question")       
                    input("Press enter to close")  
            else :
                print("Answer is incorrect, you win only 30,000 Rupees for the first,Second and third question") 
                input("Press enter to close")    
        else :
            print("Answer is incorrect, you win only 20,000 Rupees for the first & second question") 
            input("Press enter to close")
    else :
        print("Answer is incorrect, you win only 10,000 Rupees for the first question")
        input("Press enter to close")
else :
    print("Answer is incorrect, Game over / You didn't win any money")
    input("Press enter to close")
