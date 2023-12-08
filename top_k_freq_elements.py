class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        for i in  nums:
            freq[i] += 1
            
        '''
        For sorting the items based on the freq - we can use a bucket sort ( 0 to n buckets => len(nums) + 1 buckets) where in          each bukcet denotes the freq
        
        {
        1:3,
        2:2,
        3:1
        }
         0   1   2    3   4  5  6
        [[],[3],[2], [1],[],[],[]]
        
    
        '''
        
        freq_bucket = [[] for i in range(len(nums)+1)]
        
        for key, value in freq.items():
            '''
            here the value will be theindex and the key will the be the elt we are uinserting in the bucket
            '''
            freq_bucket[value].append(key)
        # print('freq_bucket:',freq_bucket)
            
        res = []
            
        for i in range(len(freq_bucket)-1, 0, -1):
            # print('index', i)
            # print('bucket elt', freq_bucket[i] )
            '''
            now we need to iterate in reverse to obtain the top k elts - 
            but also keep in mind if there is no elt in that 
            bucket - we need to move to the previous one
            
            '''
            for n in freq_bucket[i]:
                # print(n)
                res.append(n)
                if len(res) == k:
                    return res
                
            
        
                                        