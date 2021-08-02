
from random import randint, sample
from collections import Counter
from tests.flo import *
roles={
    (1,1):100,
    (5,1):50,
    (1,3):1000,
    (1,4):2000,
    (1,5):3000,
    (1,6):4000,
    (2,3):200,
    (2,4):400,
    (2,5):600,
    (2,6):800,
    (3,3):300,
    (3,4):600,
    (3,5):900,
    (3,6):1200,
    (4,3):400,
    (4,4):800,
    (4,5):1200,
    (4,6):1600,
    (6,6):2400,
    (6,5):1800,
    (6,4):1200,
    (6,3):600,
    (5,6):2000,
    (5,5):1500,
    (5,4):1000,
    (5,3):500,
    (1,2):200,
    (2,2):0,
    (3,2):0,
    (4,2):0,
    (5,2):100,
    (6,2):0,
    (2,1):0,
    (3,1):0,
    (4,1):0,
    (6,1):0,


}
class GameLogic:

    @staticmethod
    def calculate_score(dice_roll:tuple)->int:
        score=0
        dice_counter=Counter(dice_roll).most_common()

        stright=sorted(dice_roll)
        if stright==[1,2,3,4,5,6]:
            score=1500
            return score
        elif len(dice_counter)==3 and dice_counter[2][1] == 2:
            score=1500
            return score
        for x in dice_counter:
            score+=roles[x]
        return score
    
    @staticmethod
    def roll_dice(num)->tuple:
        return tuple(randint(1,6) for _ in range(0, num))


class Banker:

    def __init__(self) -> None:
        self.shelved=0
        self.balance=0


    def shelf(self,amount):
        self.shelved+=amount

    def bank(self):
        self.balance+=self.shelved
        self.shelved=0
        return self.balance
    
    def clear_shelf(self):
        self.shelved=0
    

class Game(GameLogic, Banker): 

    def play(self, roller):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        decision = input("> ")

        if decision == "y":
            var1 = True
            round_num = 1
            dice_num = 6
            while var1:
                print(f"Starting round {round_num}")
                print(f"Rolling {dice_num} dice...")
                dice = self.roll_dice(dice_num)
                sentence = "*** "
                for x in dice:
                    sentence = sentence + str(x) + " "
                sentence = sentence + "***"
                print(sentence)
                print("Enter dice to keep, or (q)uit:")
                dice_to_keep = input("> ") 
                if dice_to_keep == "q":
                    var1 = False
                    print(f"Thanks for playing. You earned {self.balance} points")
                else:
                    new_list = []
                    for x in dice_to_keep:
                        new_list.append(int(x))
                    tuple_list = tuple(new_list)
                    shelf_score = self.calculate_score(tuple_list)
                    self.shelf(shelf_score)
                    dice_num = dice_num - len(dice_to_keep) 
                    print(f"You have {self.shelved} unbanked points and {dice_num} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    decision2 = input("> ")
                    if decision2 == "r":
                        continue
                    elif decision2 == "b":
                        print(f"You banked {self.shelved} points in round {round_num}")
                        self.bank()
                        round_num += 1
                        print(f"Total score is {self.balance} points")
                        dice_num = 6
                    elif decision2 == "q":
                        print(f"Thanks for playing. You earned {self.balance} points")
                        var1 = False
        else: 
            print("OK. Maybe another time")


if __name__ == "__main__":
    game = Game()
    game.play()

        
    













# dice_roll=(1,5,2,3,4,6)
# stright=sorted(dice_roll)
# print(stright)
# if stright==[1,2,3,4,5,6]:
#     score=1500
#     print (score)