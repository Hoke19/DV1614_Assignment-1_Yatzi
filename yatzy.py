#!/usr/bin/env python3


import random
from collections import namedtuple
#-----------------------------------------Score Pad------------------------------------------------
Score_Pad = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0,
             'Pairs': 0, 'twopairs': 0, 'threeofakind': 0, 'fourofakind': 0,
             'smallstraight': 0, 'largestraight': 0, 'fullhouse': 0, 'chance': 0, 'yatzy': 0}
#-----------------------------------------Categories List------------------------------------------
categories = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes',
              'Pairs', 'twopairs', 'threeofakind', 'fourofakind',
              'smallstraight', 'largestraight', 'fullhouse', 'chance', 'yatzy']
#-----------------------------------------Random Dice Generator------------------------------------
def RollDices(dice_number):
    count = 1
    while count <= dice_number:
        num = random.randint(1, 6)
        yield num
        count += 1
#-----------------------------------------CAT Ones-------------------------------------------------
def Ones(player_choice_list):
    '''Try to get as many ones as possible. The points given is equal to the number of dice showing one.'''
    Cat_Score = player_choice_list.count(1) * 1
    return Cat_Score
#-----------------------------------------CAT Twos-------------------------------------------------
def Twos(player_choice_list):
    '''Try to get as many twos as possible. The points given is equal to 2 * the number of dice showing two.'''
    Cat_Score = player_choice_list.count(2) * 2
    return Cat_Score
#-----------------------------------------CAT Threes-----------------------------------------------
def Threes(player_choice_list):
    '''Try to get as many threes as possible. The points given is equal to 3 * the number of dice showing three.'''
    Cat_Score = player_choice_list.count(3) * 3
    return Cat_Score
#-----------------------------------------CAT Fours------------------------------------------------
def Fours(player_choice_list):
    '''Try to get as many fours as possible. The points given is equal to 4 * the number of dice showing four.'''
    Cat_Score = player_choice_list.count(4) * 4
    return Cat_Score
#-----------------------------------------CAT Fives------------------------------------------------
def Fives(player_choice_list):
    '''Try to get as many fives as possible. The points given is equal to 5 * the number of dice showing five.'''
    Cat_Score = player_choice_list.count(5) * 5
    return Cat_Score
#-----------------------------------------CAT Sixes------------------------------------------------
def Sixes(player_choice_list):
    '''Try to get as many sixes as possible. The points given is equal to 6 * the number of dice showing six.''' 
    Cat_Score = player_choice_list.count(6) * 6
    return Cat_Score
#-----------------------------------------CAT Pair-------------------------------------------------
def Pairs(player_choice_list):
    '''Try to get a pair of any number. The points given is equal to the two dice added together.'''
    Cat_Score = 0
    befor_scoring_list = []

    for i in range(1, 7):
        if player_choice_list.count(i) > 1:
            befor_scoring_list.append(i)
            Cat_Score = 2 * max(befor_scoring_list)
    return Cat_Score
#-----------------------------------------CAT Two Pairs--------------------------------------------
def Two_Pairs(player_choice_list):
    '''Try to get two distinct pairs. The score is equal to the four dice added together.'''
    Cat_Score = 0
    List_Histogram= []
    befor_scoring_list = []

    for i in range(1, 7):
        List_Histogram.append(player_choice_list.count(i)) 

        if 1 < player_choice_list.count(i) < 4:
            befor_scoring_list.append(i)
            
            if len(befor_scoring_list) == 2:
                Cat_Score = 2 * sum(befor_scoring_list)
        
        elif 4 <= player_choice_list.count(i) :
            befor_scoring_list.append(i)
            Cat_Score = 4 * sum(befor_scoring_list)

    return Cat_Score
#-----------------------------------------CAT Three of a kind--------------------------------------
def Three_of_a_Kind(player_choice_list):
    '''Try to get three dice showing the same number . The score is equal to the three dice added together.'''
    Cat_Score = 0

    for i in range(1, 7):
        if player_choice_list.count(i) >= 3:
            Cat_Score = 3 * i
   
    return Cat_Score
#-----------------------------------------CAT Four of a kind---------------------------------------
def Four_of_a_Kind(player_choice_list):
    '''Try to get four dice showing the same number . The score is equal to the four dice added together.'''
    Cat_Score = 0
   
    for i in range(1, 7):  
      if player_choice_list.count(i) >= 4:
          Cat_Score = 4 * i
    
    return Cat_Score
#-----------------------------------------CAT Small straight---------------------------------------
def Small_Straight(player_choice_list):
    '''Try to get the sequence 1, 2, 3, 4, 5 across the dice. Awards 15 points.'''
    Cat_Score = 0  
    player_choice_list.sort()
    
    if player_choice_list == [1, 2, 3, 4, 5]:
        Cat_Score = 15
    
    return Cat_Score
#-----------------------------------------CAT Large straight---------------------------------------
def Large_Straight(player_choice_list):
    '''Try to get the sequence 2, 3, 4 ,5, 6 across the dice. Awards 20 points.'''
    Cat_Score = 0  
    player_choice_list.sort()
    
    if player_choice_list == [2, 3, 4, 5, 6]:
        Cat_Score = 20
    
    return Cat_Score
#-----------------------------------------CAT Full house-------------------------------------------
def Full_House(player_choice_list):
    '''Try to get one Three of a kind and one Pair. The score is equal to all dice added together.'''
    Cat_Score = 0
    player_list = list(player_choice_list)

    for i in range(1, 7):
        if player_choice_list.count(i) == 5:
            Cat_Score = sum(player_list)
            return Cat_Score
    
    for i in range(1, 7):
        if player_choice_list.count(i) == 3:
            for j in range(3):
                player_choice_list.remove(i)
            for i in range(1,7):
                if player_choice_list.count(i) == 2:
                    Cat_Score = sum(player_list)
    
    return Cat_Score
#-----------------------------------------CAT Chance-----------------------------------------------
def Chance(player_choice_list):
    '''Try to get the dice to show as high of a total as possible. Awards the total as points.'''
    Cat_Score = sum(player_choice_list)
    return Cat_Score
#-----------------------------------------CAT Yatzi------------------------------------------------
def Yatzi(player_choice_list):
    '''Try to get all dice showing the same number. Awards 50 points.'''
    Cat_Score = 0
    if len(set(player_choice_list)) == 1:
        Cat_Score = 50    
    
    return Cat_Score
#-----------------------------------------Import Players Name--------------------------------------
def Import_Players_Name():
    '''Get players name until one player type "start" then the game will be started'''
    Player = namedtuple('Player', ['Name', 'Score', 'Dices'])
    Players = Player([], [], [])
    name_flag = 0
    while True:
        player_name = input("Type player <name> to add players or <start> to enter the game:")
        if player_name == '':
            print("Error: You must type a name")
        elif player_name == 'start' and name_flag != 0:
            break
        else:
            Players.Name.append(player_name)
            Players.Score.append(Score_Pad)
            Players.Dices.append(list())
            name_flag +=1
        
    return(Players)
#-----------------------------------------Shuffle players list-------------------------------------
def Shuffle_Players_Order(Players):
    random.shuffle(Players.Name)
    return(Players)
#-----------------------------------------Print Lines With Stars-----------------------------------
def print_stars(lines):
    for i in range(lines):
        print(' '+60*'=')
#-----------------------------------------Players Score--------------------------------------------
def Players_Score(turn, Players, player_index, player_choice_list):
    '''Calculate players scores in diferent categor'''
    if turn == 1:
        print(f'{Players.Name[player_index-1]} score in category Ones is:', Ones(player_choice_list))
        temp1 = dict(Players.Score[player_index-1])
        temp1['Ones'] = Ones(player_choice_list)
        Players.Score[player_index-1] = temp1
        #print(Players.Score[player_index-1])

    elif turn == 2:
        print(f'{Players.Name[player_index-1]} score in category Twos is:', Twos(player_choice_list))
        temp2 = dict(Players.Score[player_index-1])
        temp2['Twos'] = Twos(player_choice_list)
        Players.Score[player_index-1] = temp2
        # print(Players.Score[player_index-1])

    elif turn == 3:
        print(f'{Players.Name[player_index-1]} score in category Threes is:', Threes(player_choice_list))
        temp3 = dict(Players.Score[player_index-1])
        temp3['Threes'] = Threes(player_choice_list)
        Players.Score[player_index-1] = temp3
        # print(Players.Score[player_index-1])

    elif turn == 4:
        print(f'{Players.Name[player_index-1]} score in category Fours is:', Fours(player_choice_list))
        temp4 = dict(Players.Score[player_index-1])
        temp4['Fours'] = Fours(player_choice_list)
        Players.Score[player_index-1] = temp4
        # print(Players.Score[player_index-1])

    elif turn == 5:
        print(f'{Players.Name[player_index-1]} score in category Fives is:', Fives(player_choice_list))
        temp5 = dict(Players.Score[player_index-1])
        temp5['Fives'] = Fives(player_choice_list)
        Players.Score[player_index-1] = temp5
        # print(Players.Score[player_index-1])

    elif turn == 6:
        print(f'{Players.Name[player_index-1]} score in category Sixes is:', Sixes(player_choice_list))
        temp6 = dict(Players.Score[player_index-1])
        temp6['Sixes'] = Sixes(player_choice_list)
        Players.Score[player_index-1] = temp6
        # print(Players.Score[player_index-1])

    elif turn == 7:
        print(f'{Players.Name[player_index-1]} score in category Pairs is:', Pairs(player_choice_list))
        temp7 = dict(Players.Score[player_index-1])
        temp7['Pairs'] = Pairs(player_choice_list)
        Players.Score[player_index-1] = temp7
        # print(Players.Score[player_index-1])
    
    elif turn == 8:
        print(f'{Players.Name[player_index-1]} score in category Two Pairs is:', Two_Pairs(player_choice_list))
        temp8 = dict(Players.Score[player_index-1])
        temp8['twopairs'] = Two_Pairs(player_choice_list)
        Players.Score[player_index-1] = temp8
        # print(Players.Score[player_index-1])
    
    elif turn == 9:
        print(f'{Players.Name[player_index-1]} score in category Three of a Kind is:', Three_of_a_Kind(player_choice_list))
        temp9 = dict(Players.Score[player_index-1])
        temp9['threeofakind'] = Three_of_a_Kind(player_choice_list)
        Players.Score[player_index-1] = temp9
        # print(Players.Score[player_index-1])
    
    elif turn == 10:
        print(f'{Players.Name[player_index-1]} score in category Four of a Kind is:', Four_of_a_Kind(player_choice_list))
        temp10 = dict(Players.Score[player_index-1])
        temp10['fourofakind'] = Four_of_a_Kind(player_choice_list)
        Players.Score[player_index-1] = temp10
        # print(Players.Score[player_index-1])
    
    elif turn == 11:
        print(f'{Players.Name[player_index-1]} score in category Small Straight is:', Small_Straight(player_choice_list))
        temp11 = dict(Players.Score[player_index-1])
        temp11['smallstraight'] = Small_Straight(player_choice_list)
        Players.Score[player_index-1] = temp11
        # print(Players.Score[player_index-1])
    
    elif turn == 12:
        print(f'{Players.Name[player_index-1]} score in category Large Straight is:', Large_Straight(player_choice_list))
        temp12 = dict(Players.Score[player_index-1])
        temp12['largestraight'] = Large_Straight(player_choice_list)
        Players.Score[player_index-1] = temp12
        # print(Players.Score[:player_index-1])
    
    elif turn == 13:
        print(f'{Players.Name[player_index-1]} score in category Full Houseees is:', Full_House(player_choice_list))
        temp13 = dict(Players.Score[player_index-1])
        temp13['fullhouse'] = Full_House(player_choice_list)
        Players.Score[player_index-1] = temp13
        # print(Players.Score[player_index-1])
    
    elif turn == 14:
        print(f'{Players.Name[player_index-1]} score in Chance cat. is:', Chance(player_choice_list))
        temp14 = dict(Players.Score[player_index-1])
        temp14['chance'] = Chance(player_choice_list)
        Players.Score[player_index-1] = temp14
        # print(Players.Score[player_index-1])
    
    elif turn == 15:
        print(f'{Players.Name[player_index-1]} score in Yatzi cat. is:', Yatzi(player_choice_list))
        temp15 = dict(Players.Score[player_index-1])
        temp15['yatzi'] = Yatzi(player_choice_list)
        Players.Score[player_index-1] = temp15
        # print(Players.Score[player_index-1])
#-----------------------------------------Preview Winner-------------------------------------------
def final_table(Players):

    for number in range(len(Players.Name)):
        print(f'\t{Players.Name[number]}', end="\t")
    for row in range(0, 15):
        print('\n')
        print(len(Players.Name)*15*'-')
        print(categories[row], end="\t")
        for column in range(0, len(Players.Name)):
            score = Players.Score[column][categories[row]]
            if row < 7 or 12 < row:
                print(f'        {score}', end="")
            else:
                print(score, end="\t")

def preview_winner(Players):
    final_score = []
    print_stars(2)
    final_table(Players)

    for i in range(len(Players.Name)):
        [name, score] = [Players.Name[i], sum(Players.Score[i].values())]
        final_score.append([name, score])
    
    def sortSecond(val): 
        return val[1]
    
    final_score.sort(key = sortSecond, reverse = True)
    print('\n')
    for part in final_score:
        print(f'\n{part[0]} final score is: {part[1]}')

    print_stars(2)
    for part in final_score:
        if part[1] == final_score[0][1]:
            print(f'\n\tThe Game Winner is {final_score[0][0]} with score :{final_score[0][1]} \n')
    print_stars(2)
#-----------------------------------------Main Body------------------------------------------------
def main():
    '''Main body of the game'''
    Players = Import_Players_Name()
    Shuffle_Players_Order(Players)

    turn = 1
    while turn < 16:
        dice_number = 5
        player_index = 1

        while player_index != len(Players.Name)+1:
            print_stars(1)
            print(f'|             Name of Category: {categories[turn-1]}                         |')
            print_stars(1)
            
            user_input = input(f'Player {player_index}:({Players.Name[player_index-1]}) press enter to roll the dices:')
            player_choice_list =[]

            if user_input == '':
                dice_number = 5
                i = 0

                while dice_number != 0:
                    i += 1
                    count = 0

                    dices = RollDices(dice_number)

                    Players.Dices[player_index-1].clear()

                    for dice in range(dice_number):
                        Players.Dices[player_index-1].append(next(dices))

                    print(f"\n          Your {i} turn")
                    print("Rolled Dices = ", Players.Dices[player_index-1])

                    if i == 3:
                        player_choice_list += Players.Dices[player_index-1]
                        break 

                    while True:

                        while True:
                            player_choice = input("Enter Number to keep or ENTER to Reroll = ")
                            if player_choice == '':
                                break
                            elif int(player_choice) in Players.Dices[player_index-1]:
                                break
                            print("Wrong input, Try again!")
                        
                        if player_choice == '':
                            break
                        count +=1

                        player_choice_list.append(int(player_choice))
                        Players.Dices[player_index-1].remove(int(player_choice))
                        print("Remained Dices = ", Players.Dices[player_index-1])
                        
                    dice_number -= count

            print(f'\n{Players.Name[player_index-1]} final choice is:', player_choice_list)
            
            Players_Score(turn, Players, player_index, player_choice_list)
            
            player_index += 1
        turn += 1

    preview_winner(Players)

if __name__ == '__main__':
    main()
