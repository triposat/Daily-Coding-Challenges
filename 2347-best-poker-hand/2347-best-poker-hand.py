class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits = Counter(suits)
        ranks = Counter(ranks)
        for idx in suits:
            if suits[idx] == 5:
                return "Flush"
        for idx in ranks:
            if ranks[idx] >= 3:
                return "Three of a Kind"
            elif ranks[idx] >= 2:
                return "Pair"
        return "High Card"