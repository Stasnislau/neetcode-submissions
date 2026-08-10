from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        turn = 0
        skipped = set()
        rToSkip = 0
        dToSkip = 0
        while count['R'] > 0 and count['D'] > 0:
            turn = turn % len(senate)
            if turn in skipped:
                turn += 1
                continue
            party = senate[turn]
            print(party)
            if party == 'R':
                if rToSkip > 0:
                    rToSkip -= 1
                    count['R'] -= 1
                    skipped.add(turn)
                else:
                    dToSkip += 1
            else:
                if dToSkip > 0:
                    dToSkip -= 1
                    count['D'] -= 1
                    skipped.add(turn)
                else:
                    rToSkip += 1
            turn += 1
            
        
        return 'Radiant' if count['R'] > 0 else 'Dire'