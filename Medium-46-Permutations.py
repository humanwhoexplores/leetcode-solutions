class Solution:
    
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, decision_space, fixed_path, result):
        if not decision_space:
            result.append(fixed_path)
            return
        
        
        for i in range(len(decision_space)):
            # in this line the magic happens, decision space decreases by 1, fixed_path increases by 1
            self.dfs(decision_space[:i] + decision_space[i+1:], fixed_path+[decision_space[i]], result)