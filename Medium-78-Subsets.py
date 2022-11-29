class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # let's find the subsets
        res = []
        self.dfs(nums , [], res)
        return res
    
    
    def dfs(self, decision_space, path, result):
        
        # let's DFS dude. 
        result.append(path)
        for i in range(len(decision_space)):
            self.dfs(decision_space[i+1:], path + [decision_space[i]] , result)