"""

The program will allow a user three attempts to guess the correct answer to a question.
The question is: "What is the capital of California?" The correct answer is "Sacramento".

We first set maximum number of attempts to three.
Then we create a loop to iterate three times.
For each loop, iteration, we ask the user for their answer, input.
Then going off of the user's answer, we compare answers to see if it is correct.
If it is correct, program will print "Correct!", then the loop will terminate withh a break statement.

However, if the user's answers were incorrect within the maximum tries, we print 
"You have used up your allotment of guesses." 
Then print "The correct answer is "California".

"""


"""

main
    question = "What is the capital of California?"
    answer = "California"
    ask(question, answer)

ask
    attempts = 0
    loop three times
        increment attempts
        ask user input()
        check to see if user input is equal to answer
            if correct, print "Correct!", exit loop

    if incorrect
        print to user "You have used up your allotment of guesses."
        print the correct answer "The correct answer is "California"

main

"""


def main():
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask(question, answer)


def ask(question, answer, max_attempts=3):

    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break

    if ans != answer:
        print("You have used up your allotment of guesses.")


main()
