import numpy as np
from fastai.text import *

class NextWord():
    def __init__(self, predicter, sentence, classification=None):
        self.predicter = predicter
        self.classification = classification
        self.sentence = sentence
    
    def predict_next(self):
        sen = " ".join(self.sentence.split(" ")[-12:])
        self.next = self.predicter.predict(sen, 1, temperature=0.9).split(" ")[-1]
    
    def print_next(self):
        print (self.next)
    
    def valid_word(self):
        return self.next not in ["\n", " ", '', '"', "/", "'", "..", ":"]
    
    def valid_comma_points(self):
        if self.next not in [",", "."]:
            return True
        else:
            return (not set([",", "."]) & set(self.sentence.split(" ")[-4:])) and (len(self.sentence.split(" ")) > 8)
    
    def valid_class(self):
        if self.classification:
            for i in range(6):
                score = self.classification.predict(" ".join(self.sentence.split(" ")[-np.random.randint(i,10):]))
                if score[-1][1] > 0.5:
                    return True
            return False
        return True
        
    def valid(self):
        if self.valid_comma_points() and self.valid_word() and self.valid_class():
            self.sentence += " " + self.next
#             print(self.sentence)
            return True
        return False
        
                
    def generate(self, num):
        counter=0
        while(len(self.sentence.split(" ")) < num):
            self.predict_next()
            if self.valid():
                counter = 0
            else:
                counter+=1
            if counter == 20:
                counter = 0
                self.sentence = " ".join(self.sentence.split(" ")[:-1])
        print(self.sentence)