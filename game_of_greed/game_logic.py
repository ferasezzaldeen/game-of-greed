
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
    @staticmethod   
    def validate_keepers(roll,keeper):

        roll_counter=Counter(roll).most_common()
        keeper_counter=Counter(keeper).most_common()
        # for x in keeper:
        #     if k==" ":
        #         return False
    
        if len(keeper)>len(roll):
                return False
        
        for i in keeper_counter:
            if i not in roll_counter:
                return False

        if len(keeper_counter)==3 and keeper_counter[2][1] == 2:
            return True

        for i in keeper_counter:
            if roles[i] ==0:
                return False
        return True
    @staticmethod
    def get_scorers(test_input):
        result=[]
        input_counter=Counter(test_input).most_common()
        for i in input_counter:
            if roles[i] !=0:
                for x in range(i[1]) :
                    result.append(i[0])


        return tuple(result)
                



        



        
            

       


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

    def play(self, roller=None):
        roller=roller or Game.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        decision = input("> ")

        if decision == "y":
            var1 = True
            round_num = 1
            dice_num = 6
            print(f"Starting round {round_num}")
            while var1:
                print(f"Rolling {dice_num} dice...")
                dice = roller(dice_num)

                sentence = "*** "
                for x in dice:
                    sentence = sentence + str(x) + " "
                sentence = sentence + "***"
                print(sentence)

                if  not Game.get_scorers(dice):
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    print(f"You banked {0} points in round {round_num}")
                    # round_num += 1
                    print(f"Total score is {self.balance} points")
                    dice_num=6
                    round_num+=1
                    print(f"Starting round {round_num}")

                    continue
                    


                print("Enter dice to keep, or (q)uit:")
                dice_to_keep = input("> ") 
                dice_to_keep= dice_to_keep.replace(' ', '')
                if dice_to_keep == "q":
                    var1 = False
                    print(f"Thanks for playing. You earned {self.balance} points")
                else :
                    
                   
                    dice_to_keep=[int(i) for i in dice_to_keep ]
                    while not Game.validate_keepers(dice,tuple(dice_to_keep)) and var1: 
                        print("Cheater!!! Or possibly made a typo...")
                        print(sentence)
                        print("Enter dice to keep, or (q)uit:")
                        dice_to_keep=input("> ")
                        dice_to_keep= dice_to_keep.replace(' ', '')
                        if dice_to_keep=="q":
                            var1=False
                        else:
                            

                            dice_to_keep= [int(i) for i in dice_to_keep ]

                    if dice_to_keep=="q":
                        print(f"Thanks for playing. You earned {self.balance} points")
                        continue
                    if len(dice_to_keep)==dice_num:
                        shelf_score =1500
                    else:
                        shelf_score = self.calculate_score(dice_to_keep)

                    self.shelf(shelf_score)
                    dice_num = dice_num - len(dice_to_keep) 
                    print(f"You have {self.shelved} unbanked points and {dice_num} dice remaining")
                    if dice_num==0:
                        dice_num=6
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    decision2 = input("> ")
                    while decision2!="r" and decision2!="b" and decision2!="q":
                        print("please enter the correct input")
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
                        print(f"Starting round {round_num}")

                    elif decision2 == "q":
                        print(f"Thanks for playing. You earned {self.balance} points")
                        var1 = False
                    
                    
        else: 
            print("OK. Maybe another time")


if __name__ == "__main__":
    game = Game()
    game.play()

