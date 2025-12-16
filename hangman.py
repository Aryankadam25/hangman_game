import random

words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat",
          "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar",
          "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", 
          "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", 
          "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", 	"elephant")

#dictionary for hangman art 
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" 0 ",
                  "   ",  
                  "   "),
               2:(" 0 ",
                  " |  ",
                  "   "),
               3:(" 0 ",
                  " |  ",
                  " / "),
               4:(" 0 ",
                  " | ",
                  "/ \\"),
               5:(" 0 ",
                  "\\| ",
                  "/ \\"),
               5:(" 0 ",
                  "\\| ",
                  "/ \\"),
               6:(" 0 ",
                  " \\|/ ",
                  "/ \\")}


def display_hangman(wrong_gusses):
   for line in hangman_art[wrong_gusses]:
      print(line)


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_gusses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_gusses)
        display_hint(hint)
        guess = input("enter a letter:").lower()


        if len(guess)!=1 or not guess.isalpha():
            print("!!!!!!invalid input. please enter a single alphabet character !!!!!!")
            continue
        
      

        if guess in guessed_letters:
            print("you already guessed that letter. try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range((len(answer))):
               if answer[i] == guess:
                  hint[i] = guess
        else:
            wrong_gusses += 1
            if wrong_gusses == 6:
                display_hangman(wrong_gusses)
                print("sorry!! you lost the game")
                is_running = False
                print(f"the correct answer is : {answer}")
            else:
               print(f"wrong guess!! you have {6-wrong_gusses} gusses left")
            
        if "_" not in hint:
            is_running = False
            print("congratulations!! you guessed the word correctly")

               

        

if __name__ == "__main__":
    main()