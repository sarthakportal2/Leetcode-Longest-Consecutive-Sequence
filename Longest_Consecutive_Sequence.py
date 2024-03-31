class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #T(C(N))=O(N) and S(C(N)==(O(N*2))) as it requires non contiuous memory allocation iteratively
        if not nums:return 0#initalizing nums list
        nums=sorted(list(set(nums)))#sorting nums array/list
        out,unitdist=1,1#Graph's Unit distance and Output declare
        for i in range(len(nums)):#iterate through sorted nums 's length
            if nums[i-1]+1==nums[i]:unitdist+=1#incremnting UnitDist from array's right to left indx
            else:unitdist=1#Graph's unit distance val 
            out=max(out,unitdist)#aximum output declare

        return out#printing output


           # nums=nums.sort() #len(nums)
