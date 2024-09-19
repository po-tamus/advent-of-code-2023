"""
red green or blue cubes in the bag
secret number of cubes of each color in bag per round
grab and see handful of random cubes a few times


example input: 
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

determine which games are possible if there are 12 red, 13 green, and 14 blue
"""

import re

def end_of_test(func):
    def wrapper_func(*args, **kwargs):
        func()
        print("----END OF TEST----")

def regex_test():
    test_string = "Game 1: the test worked"

    regex = re.sub("Game .: ", "", test_string)

    print(regex)
    
    substring = regex.find("helo")

    print(substring)

# declaring the maximum values in a dictionary
maximums = {
    "red": 12, 
    "green": 13, 
    "blue": 14
}

# declaring path
path = "cube-conundrum.txt"

# reading from text file
with open(path, "r") as f: 
    text_input = f.read()

# split to individual lines (based on newline)
games = text_input.split("\n")

def possible_games(games):

# finding sum, initialize to 0
    sum = 0

# iterate through games (lines) to find which ones are possible
# using regex search to find the part of the title that has the number (Game: X), using group to find the string from the regex obj
 
    for game in games: 
        possible = True
        game_title = re.search("Game .*:", game).group(0)

        # printing the number from the title, accounting for how many digits it has
        print(re.search("\d+", game_title).group(0))
        
        # saving that number
        game_number = int(re.search("\d+", game_title).group(0))

        # splitting the line into individual rounds 
        rounds = re.sub("Game .: ", " ", game).split(";")

        print(rounds)

        for round in rounds: 
            
            """
            would be much more robust to use regex instead of indexing
            the regex above was implemented after the disaster that is below this comment - refer to that
            for related applications
            """
            r = round.find("red") - 3
            g = round.find("green") - 3
            b = round.find("blue") - 3

            counts = {
                "red": round[r:r+2],
                "green": round[g:g+2], 
                "blue": round[b:b+2]
            }

            for color, count in counts.items():
                print([color, count])
                if count.isnumeric() and int(count) > maximums[color]:
                    possible = False
        
        if possible == True: 
            sum += game_number 

    return sum

print(possible_games(games))
