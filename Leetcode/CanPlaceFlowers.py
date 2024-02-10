from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1 and flowerbed[i] == 0: 
                flowerbed[i] = 1
                return True
            
            if len(flowerbed) == 1 and flowerbed[i] == 1:
                return False
            
            if len(flowerbed) == 1 and n == 1: 
                return True
            if n == 0:
                return True
            
            if flowerbed[i] == 0:
                if i == 0:
                    if i+1 < len(flowerbed) and flowerbed[i+1] == 0: #Valida que el siguiente sea 0 siempre y cuando el primer elemento sea 0
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed)-1: #Valida que el anterior sea 0 siempre y cuando el ultimo elemento sea 0
                    if i-1 >= 0 and flowerbed[i-1] == 0: #Valida que el anterior sea 0
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0: #Elmentos anteriores y siguientes deben ser 0
                        flowerbed[i] = 1
                        n -= 1
            
        return n == 0
# Test cases
print(Solution().canPlaceFlowers([0,0,0,0,0], 3))  # True

        