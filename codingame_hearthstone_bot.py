import sys
import math
import random

class Card:
    def __init__(self, card_id, location, card_type, cost, attack, defense, abilities=None):
        self.card_id = card_id
        self.location = location
        self.card_type = card_type
        self.cost = cost
        self.attack = attack
        self.defense = defense
        self.abilities = abilities

def card_value(card):
    cost = card.cost
    attack = card.attack
    defense = card.defense
    abils = card.abilities
    
    if abils != None:
        abls = len(abils) - abils.count('-')
    else:
        abls = 0
    
    value = attack + defense + abls - cost*2
    
    if card.abilities != None and 'G' in card.abilities:
        value += 1000
    if attack == 0:
        value -= 2000
    #if cost > 10:
    #    value -= 2000
    if abs(attack - defense) > 4:
        value -= 1000
    if defense < 2:
        value -= 2000

    return value

turn = 0
# game loop
while True:
    turn += 1
    for i in range(2):
        player_health, player_mana, player_deck, player_rune = [int(j) for j in input().split()]
        if i == 0:
            my_hp = player_health
            my_mana = player_mana
            my_deck = player_deck
            my_rune = player_rune
        else:
            enemy_hp = player_health
            enemy_mana = player_mana
            enemy_deck = player_deck
            enemy_rune = player_rune
            
    opponent_hand = int(input())
    card_count = int(input())
    choose_card = []
    my_hand = []
    my_board = []
    enemy_board = []
    
    for i in range(card_count):
        card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw = input().split()
        card_number = int(card_number)
        instance_id = int(instance_id)
        location = int(location)
        card_type = int(card_type)
        cost = int(cost)
        attack = int(attack)
        defense = int(defense)
        my_health_change = int(my_health_change)
        opponent_health_change = int(opponent_health_change)
        card_draw = int(card_draw)
        
        card = Card(instance_id, location, card_type, cost, attack, defense, abilities)
        
        if card.location == 0 and turn <= 30:
            choose_card.append(card)
        elif card.location == 0 and turn > 30:
            my_hand.append(card)
        elif card.location == 1 and turn > 30:
            my_board.append(card)
        elif card.location == -1 and turn > 30:
            enemy_board.append(card)
        
    if turn <= 30:
        values = [card_value(choose_card[0]), card_value(choose_card[1]), card_value(choose_card[2])]
        best = max(values)
        pick_card = values.index(best)
        print("PICK", pick_card)
    else:
        command = []
        for card in my_hand:
            if len(my_board) < 6 and card.cost <= my_mana and card.card_type == 0:
                command.append('SUMMON ' + str(card.card_id))
                if 'C' in card.abilities:
                    my_board.append(card)
                my_mana -= card.cost
            if len(my_board) > 0 and card.cost <= my_mana and card.card_type == 1:
                command.append('USE ' + str(card.card_id) + ' ' + str(my_board[0].card_id))
                my_mana -= card.cost
            if len(enemy_board) > 0 and card.cost <= my_mana and card.card_type == 2:
                command.append('USE ' + str(card.card_id) + ' ' + str(enemy_board[0].card_id))
                my_mana -= card.cost
        target = []
        for card in enemy_board:
            if 'G' in card.abilities:
                target.append(card)
        for card in my_board:
            if target == []:
                a = ''
                for c in enemy_board:
                    if card.attack >= c.defense and card.attack + card.defense <= c.attack + c.defense:
                        a = 'ATTACK ' + str(card.card_id) + ' ' + str(c.card_id)
                        break
                if a != '':
                    command.append(a)
                else:
                    command.append('ATTACK ' + str(card.card_id) + ' -1')
            else:
                b = ''
                for c in target:
                    if card.attack >= c.defense:
                        b = 'ATTACK ' + str(card.card_id) + ' ' + str(c.card_id)
                        break
                if b != '':
                    command.append(b)
                else:
                    x = random.choice(target)
                    command.append('ATTACK ' + str(card.card_id) + ' ' + str(x.card_id))
        print(';'.join(command))
