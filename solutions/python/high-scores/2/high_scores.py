class HighScores:
    def __init__(self, scores):
        self.scores  = list(map(int,scores))
        
    def latest(self):
        return self.scores[-1] 
        
    def personal_best(self):
        return max(self.scores)
        
    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]
 
scores = ["9", "88", "56", "3"]       
c = HighScores(scores)
print(c.latest())
print(c.personal_best())
print(c.personal_top_three())