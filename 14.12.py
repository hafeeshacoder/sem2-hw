class StringMerger:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def merge_strings(self):
        merged = ""
        min_len = min(len(self.word1), len(self.word2))
        for i in range(min_len):
            merged += self.word1[i] + self.word2[i]
            merged += self.word1[min_len:] + self.word2[min_len:]
        return merged
merger = StringMerger(input("Enter the 1st string:"), input("Enter second string:"))
print(merger.merge_strings())  

class Flowerbed:
    def __init__(self, flowerbed, n):
        self.flowerbed = flowerbed
        self.n = n

    def can_place_flowers(self):
        count = 0
        self.flowerbed = [0] + self.flowerbed + [0]  # Pad the flowerbed with empty plots
        
        for i in range(1, len(self.flowerbed) - 1):
            if self.flowerbed[i] == 0 and self.flowerbed[i - 1] == 0 and self.flowerbed[i + 1] == 0:
                self.flowerbed[i] = 1
                count += 1
                if count >= self.n:
                    return True
        return False
flowerbed = Flowerbed([1, 0, 0, 0, 1], 1)
print(flowerbed.can_place_flowers())  
