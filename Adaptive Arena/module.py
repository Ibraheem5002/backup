import numpy as np
import random

class MarkovChains:
    def __init__(self):
        self.in_history = []
        self.pattern = {}
        self.probability = [1/3, 1/3, 1/3]  # A, D, C
        self.in_op = None
        self.out_op = None
        self.Level = None

    def add_pattern(self, key, X):
        if key in self.pattern:
            self.pattern[key].append(X)
        else:
            self.pattern[key] = [X]

    def update_pattern(self, lvl):
        self.in_history.append(self.in_op)

        for L in range(1, lvl + 1):
            if len(self.in_history) >= L + 1:
                key = "".join(self.in_history[-(L + 1):-1])
                Z = self.in_history[-1]
                self.add_pattern(key, Z)

    def normalize_prob(self):
        total = sum(self.probability)

        if total <= 0:
            self.probability = [1/3, 1/3, 1/3]
        else:
            for i in range(3):
                self.probability[i] /= total

    def cal_probability(self, key):
        lst = self.pattern[key]
        total = len(lst)

        if total != 0:
            self.probability[0] = lst.count('A') / total
            self.probability[1] = lst.count('D') / total
            self.probability[2] = lst.count('C') / total
        else:
            self.probability = [1/3, 1/3, 1/3]

        self.normalize_prob()

    def choose_ans(self):
        sorted_prob = sorted(self.probability, reverse=True)
        best = sorted_prob[0]
        scnd = sorted_prob[1]

        if best - scnd > 0.15:
            max_idx = self.probability.index(best)
            return ['A', 'D', 'C'][max_idx]
        else:
            return np.random.choice(['A', 'D', 'C'], p=self.probability)

    def predict_ans(self):
        self.probability = [1/3, 1/3, 1/3]
        probs = []
        pLen = []

        for L in range(self.Level, 0, -1):
            if len(self.in_history) < L:
                continue

            key = "".join(self.in_history[-L:])

            if key in self.pattern:
                self.cal_probability(key)
                probs.append(self.probability.copy())
                pLen.append(len(self.pattern[key]))

        if len(probs) == 0:
            return random.choice(['A', 'D', 'C'])
        else:
            mx = -10000
            idx = -1

            for i in range(len(probs)):
                pMax = max(probs[i])
                score = pMax * pLen[i]

                if score > mx:
                    mx = score
                    idx = i

            self.probability = probs[idx]
            return self.choose_ans()

    def return_ans(self):
        op = self.predict_ans()

        if op == "A": self.out_op = "D"
        elif op == "D": self.out_op = "C"
        elif op == "C": self.out_op = "A"

    def predict(self, X, lvl):
        self.in_op = X
        self.Level = lvl

        self.return_ans()
        self.update_pattern(lvl)

        return self.out_op
    
    def fit(self,lst = []):
        self.in_history = lst