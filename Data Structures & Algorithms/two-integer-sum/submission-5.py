class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cpy_nums=sorted(nums)
        i=0
        j=len(nums)-1
        while(i<j):
            if(cpy_nums[i]+cpy_nums[j])>target:
                j-=1
            elif(cpy_nums[i]+cpy_nums[j])<target:
                i+=1
            elif(cpy_nums[i]+cpy_nums[j])==target:
                val1=cpy_nums[i]
                val2=cpy_nums[j]
                index1=nums.index(val1)
                if val1==val2:
                    index2=nums.index(val2,index1+1)
                else:
                    index2=nums.index(val2)
                return sorted([index1, index2])


