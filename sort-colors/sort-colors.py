class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,m=0,0
        n=len(nums)
        h=n-1
        def swap(i,j):
            tmp=nums[i]
            nums[i]=nums[j]
            nums[j]=tmp
        while(m<=h):
            if nums[m]==0:
                swap(l,m)
                l+=1
            elif nums[m]==2:
                swap(m,h)
                h-=1
                m-=1
            m+=1