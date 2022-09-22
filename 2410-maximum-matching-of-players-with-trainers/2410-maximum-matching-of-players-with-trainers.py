# Using Sorting
class Solution:
    def matchPlayersAndTrainers(self, play, trai):
        play.sort()
        trai.sort()

        i = len(play)-1
        j = len(trai)-1
        cnt = 0
        while i > -1 and j > -1:
            if play[i] > trai[j]:
                i -= 1
            elif play[i] <= trai[j]:
                cnt += 1
                j -= 1
                i -= 1
        return cnt

# Using Priority Queue
class Solution:
    def matchPlayersAndTrainers(self, play, trai):
        play = list(map(lambda x: -1*x, play))
        trai = list(map(lambda x: -1*x, trai))
        heapify(play)
        heapify(trai)
        cnt = 0
        while play and trai:
            p1 = -1*play[0]
            q1 = -1*trai[0]
            if p1 <= q1:
                cnt += 1
                heappop(play)
                heappop(trai)
            else:
                heappop(play)
        return cnt
