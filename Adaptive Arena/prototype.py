import numpy as np
import random

pHealth = 100
cHealth = 100
pChLvl = 0
cChLvl = 0

in_History = []
pattern = {}
probabilty = [1/3,1/3,1/3] # A,D,C
in_op = None
out_op = None
msg = None

def take_input():
    global in_op, pChLvl
    inp = int(input("Choose Your Move: [1: Attack, 2: Defend, 3: Charge, 4: Special]: "))

    while True:
        if inp < 1 or inp > 4:
            inp = int(input("Invalid Input. Please Input again: "))
        else:
            if inp == 1: in_op = 'A'
            elif inp == 2: in_op = 'D'
            elif inp == 3: in_op = 'C'
            else:
                if pChLvl < 50:
                    inp = int(input("ERROR: You don't have enough charge level. Please input again: "))
                else: in_op = 'S'
            
            return

def display():
    global pHealth, cHealth, pChLvl, cChLvl
    print()
    print( "-------Stats--------")
    print(f" P Health       : {pHealth}")
    print(f" P Charge Level : {pChLvl}")
    print(f" C Health       : {cHealth}")
    print(f" C Charge Level : {cChLvl}")
    print( "--------------------")
    print()

def add_pattern(key,X):
    global pattern
    if key in pattern:
        pattern[key].append(X)
    else:
        pattern[key] = [X]

def update_pattern(lvl):
    global in_History
    in_History.append(in_op)
    
    for L in range(1,lvl+1):
        if len(in_History) > 7:
            key = "".join(in_History[-(L+1):-1])
            Z = in_History[-1]
            add_pattern(key,Z)

def normalize_prob():
    global probabilty
    total = sum(probabilty)
    
    if total <= 0:
        probabilty = [1/3,1/3,1/3]
    else:
        for i in range(3):
            probabilty[i] /= total

def cal_probability(key):
    global probabilty, pattern
    lst = pattern[key]
    total = len(lst)

    if total != 0:
        probabilty[0] = lst.count('A') / total
        probabilty[1] = lst.count('D') / total
        probabilty[2] = lst.count('C') / total
    else:
        probabilty = [1/3,1/3,1/3]
    
    normalize_prob()

def choose_ans():
    global probabilty
    sorted_prob = sorted(probabilty, reverse=True)
    best = sorted_prob[0]
    scnd = sorted_prob[1]

    if best - scnd > 0.15:
        max_idx = probabilty.index(best)
        return ['A','D','C'][max_idx]
    else:
        return np.random.choice(['A','D','C'],p=probabilty)

def predict_ans(lvl):
    global probabilty, in_History, pattern
    probabilty = [1/3,1/3,1/3]
    probs = []
    pLen = []

    for L in range(lvl,0,-1):
        if len(in_History) < L:
            continue
            
        key = "".join(in_History[-L])

        if key in pattern:
            cal_probability(key)
            probs.append(probabilty.copy())
            pLen.append(len(pattern[key]))
    
    if len(probs) == 0:
        return random.choice(['A','D','C'])
    else:
        mx = idx = -10000
        for i in range(len(probs)):
            pMax = max(probs[i])
            score = pMax * pLen[i]

            if score > mx:
                mx = score
                idx = i
        
        probabilty = probs[idx]
        return choose_ans()

def return_ans():
    global out_op, cChLvl
    op = predict_ans(Level)

    X = random.randint(1,100)
    if cChLvl >= 50 and X > 50:
        out_op = 'S'
        return

    if op == 'A': out_op = 'D'
    elif op == 'D': out_op = 'C'
    else: out_op = 'A'

def check_ans():
    global pHealth, cHealth, pChLvl, cChLvl, in_op, out_op,msg
    if in_op == 'S':
        cHealth = 0
        msg = "You Special was successful"
        return
    
    if out_op == 'S':
        pHealth = 0
        msg = "Comp's Special was successful"
        return

    if in_op == 'A':
        if out_op != 'D': cHealth -= 10
        else: msg = ("Your Attack has failed")
        
    if in_op == 'C':
        if out_op != 'A': pChLvl += 10
        else: msg = ("You have failed to Charge")
    
    if out_op == 'A':
        if in_op != 'D': pHealth -= 10
        else: msg = ("Your Defence was successful")
        
    if out_op == 'C':
        if in_op != 'A': cChLvl += 10
        else: msg = ("Comp has failed to Charge")
        

if __name__ == "__main__":
    print("Welcome To Adaptive Arena")
    Level = 1
    abc = {
        "A": "Attack",
        "D": "Defend",
        "C": "Charge",
        "S": "Special"
    }

    while True:
        msg = None
        
        display()
        take_input()
        predict_ans(Level)
        return_ans()
        check_ans()
        update_pattern(Level)

        print(f"Comp Chose: {abc[out_op]}")
        if msg != None:
            print(msg)

        if cHealth <= 0:
            print("\nOPPONENT FALLEN\n")
            if Level >= 5:
                break
            else:
                Level += 1
                print(f"Level {Level}\n")
                cChLvl = 0
                pChLvl = 0
                pHealth = 100
                cHealth = 100
                continue
        
        if pHealth <= 0:
            print("\nYOU DIED\n")
            break
    
    print("exiting game")