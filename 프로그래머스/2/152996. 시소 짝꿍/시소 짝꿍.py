from collections import defaultdict
def solution(weights):
    ans = 0
    weightCounter = defaultdict(int)
    
    for weight in weights: weightCounter[weight] += 1
    
    for weight in sorted(set(weights)):
        ans += weightCounter[weight] * (weightCounter[weight] - 1) // 2
        ans += weightCounter[weight] * weightCounter[weight*2]
        ans += weightCounter[weight] * weightCounter[weight*3/2]
        ans += weightCounter[weight] * weightCounter[weight*4/3]
    
    return ans





