class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #import counter and make a dictionary count with key-value pairs
        from collections import Counter
        count=Counter(nums)
        #now create a bucket and fill the values
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        #reverse the buckets
        #check for num and length of the list
        res=[]
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res)==k:
                    return res



            

       