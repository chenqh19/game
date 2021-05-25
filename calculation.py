import math
from random import choice
from copy import deepcopy
import treys


def pat_to_num(pattern):
    if pattern == 's':
        return 0
    if pattern == 'h':
        return 1
    if pattern == 'd':
        return 2
    if pattern == 'c':
        return 3

def fig_to_num(figure):
    if figure == 'T':
        return 10
    if figure == 'J':
        return 11
    if figure == 'Q':
        return 12
    if figure == 'K':
        return 13
    if figure == 'A':
        return 14
    return int(figure)

def num_to_card(num):
    ans = ''
    fig = int(num/4)
    pat = num % 4
    if fig == 10:
        ans = ans + 'T'
    elif fig == 11:
        ans = ans + 'J'
    elif fig == 12:
        ans = ans + 'Q'
    elif fig == 13:
        ans = ans + 'K'
    elif fig == 14:
        ans = ans + 'A'
    else:
        ans = ans + str(fig)
    if pat == 0:
        ans = ans + 's'
    elif pat == 1:
        ans = ans + 'h'
    elif pat == 2:
        ans = ans + 'd'
    else:
        ans = ans + 'c'
    return ans
    


def sampling(my_cards, known_cards, num_of_samples):
    cards = [i for i in range(8,60)]
    prob_array = []
    for card in known_cards:
        num = fig_to_num(card[0])*4+pat_to_num(card[1])
        cards.remove(num)
    for card in my_cards:
        num = fig_to_num(card[0])*4+pat_to_num(card[1])
        cards.remove(num)
    win = 0
    for i in range(num_of_samples):
        sampled = []
        oppo = []
        c = deepcopy(cards)
        for i in range(5-len(known_cards)):
            new_sample = choice(c)
            c.remove(new_sample)
            new_sample = num_to_card(new_sample)
            sampled.append(new_sample)
        for j in range(2):
            new_sample = choice(c)
            c.remove(new_sample)
            new_sample = num_to_card(new_sample)
            oppo.append(new_sample)
        f = deepcopy(known_cards)
        m = deepcopy(my_cards)
        oppo_result = evaluation(oppo, known_cards+f)
        my_result = evaluation(m, known_cards+f)
        if my_result < oppo_result:
            win = True
        else:
            win = False
        valid = True
        # We need to find out those invalid samples: opposite will never do stupid bets like that



'''
def sampling(my_cards, known_cards, num_of_samples):
    cards = [i for i in range(8,60)]
    prob_array = []
    mine = []
    known = []
    for card in known_cards:
        num = fig_to_num(card[0])*4+pat_to_num(card[1])
        known.append(num)
        cards.remove(num)
    for card in my_cards:
        num = fig_to_num(card[0])*4+pat_to_num(card[1])
        mine.append(num)
        cards.remove(num)
    win = 0
    for i in range(num_of_samples):
        sampled = []
        oppo = []
        c = deepcopy(cards)
        for i in range(5-len(known)):
            new_sample = choice(c)
            c.remove(new_sample)
            sampled.append(new_sample)
        for j in range(2):
            new_sample = choice(c)
            c.remove(new_sample)
            oppo.append(new_sample)
        f = deepcopy(known)
        m = deepcopy(mine)
        my_all_cards = m + f + sampled
        my_all_cards.sort()
        my_ans = check_type(my_all_cards)
        oppo_all_cards = oppo + f + sampled
        oppo_all_cards.sort()
        oppo_ans = check_type(oppo_all_cards)
        if my_ans > oppo_ans:
            win += 1
        elif my_ans == oppo_ans:
            win += 0.5
    return win/num_of_samples


def check_type(all_cards):
    num_of_fig = []
    num_of_pat = []
    for i in range(13):
        num_of_fig.append(0)
    for j in range(4):
        num_of_pat.append(0)
    for card in all_cards:
        num_of_fig[int(card/4)-2] += 1
        num_of_pat[int(card%4)] += 1
    # four of a kind
    if max(num_of_fig) == 4:
        return 8 
    # full house
    if max(num_of_fig) == 3:
        temp = deepcopy(num_of_fig)
        temp.remove(3)
        if max(temp) >= 2:
            return 7
    # flush
    if max(num_of_pat) >= 5:
        return 6
    # straight

    # three of a kind
    if max(num_of_fig) == 3:
        return 4
    # two pairs
    if max(num_of_fig) == 2:
        temp = deepcopy(num_of_fig)
        temp.remove(2)
        if max(temp) >= 1:
            return 3
    # one pair
    if max(num_of_fig) == 2:
        return 2
    return 1

'''

def evaluation(my_cards, known_cards):
    hand = []
    for new_card in my_cards:
        hand.append(treys.Card.new(new_card))
    board = []
    for new_card in known_cards:
        board.append(treys.Card.new(new_card))
    evaluator = treys.Evaluator()
    if len(board) != 0 and len(hand) != 0:
        return evaluator.evaluate(board, hand)
    else:
        return 10000



'''
def prob_calculation(known_cards):
    prob_array = []
    patterns = [[],[],[],[]]
    figure = []
    for card in known_cards:
        figure.append(fig_to_num(card[0]))
        patterns[pat_to_num(card[1])] += 1
    figure.sort()
    # calculate probabilities
    prob_array.append(cal_one_pair(figure))
    prob_array.append(cal_two_pairs(figure))
    prob_array.append(cal_three_of_a_kind(figure))
    prob_array.append(cal_straight(figure))
    prob_array.append(cal_flush(patterns))
    prob_array.append(cal_full_house(figure))
    prob_array.append(cal_four_of_a_kind(figure))
    prob_array.append(cal_straight_flush(known_cards))
    
    return prob_array

def cal_one_pair(figure):
    one_pair_prob = 0
    for i in range(len(figure)-1):
        if figure[i] == figure[i+1]:
            one_pair_prob = 1
            one_pair_fig = figure[i]
    if one_pair_prob != 1:
        for j in range(len(figure)/2+1,8):
            one_pair += (1 - one_pair_prob)*(j-1)/13
    return one_pair_prob, one_pair_fig

def cal_two_pairs(figure):
    two_pair_prob = 0
    two_pairs_fig = []
    for i in range(len(figure)-1):
        if figure[i] == figure[i+1]:
            if len(two_pairs_fig) == 0:
                two_pairs_fig.append(figure[i])
            elif figure[i] not in two_pairs_fig:
                two_pair_prob = 1
                two_pairs_fig.append(figure[i])
    if two_pairs_prob != 1:
        
    return two_pair_prob, two_pairs_fig


def cal_three_of_a_kind(figure):
    three_of_a_kind_prob = 0
    pair = 0
    for i in range(len(figure)-2):
        if figure[i] == figure[i+1]:
            pair += 1
            if figure[i] == figure[i+2]:
                three_of_a_kind_prob = 1
                three_of_a_kind_fig = figure[i]
    if figure[-2] == figure[-1]:
        pair += 1
    if three_of_a_kind_prob != 1:
        if pair == 0:
            

    return


def cal_straight(figure):
    
    return



def cal_flush(pattern):


    return

def cal_full_house(figure):

    return


def cal_four_of_a_kind(figure):


    return

def cal_straight_flush(known_cards):

    return

'''