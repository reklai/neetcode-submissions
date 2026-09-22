class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        res = []
        prod = 0
        for i in range(0, len(nums)):
            if i == 0:
                pre.append(nums[i])
                prod = nums[i]
                continue
            prod = prod * nums[i]
            pre.append(prod)
        prod = 0
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post.append(nums[i])
                prod = nums[i]
                continue
            prod = prod * nums[i]
            post.append(prod)
        post.reverse()
        for i in range(0, len(nums)):
            if i == 0:
                res.append(post[i + 1])
                continue
            if i == len(nums) - 1:
                res.append(pre[i - 1])
                break
            res.append(pre[i - 1] * post[i + 1])
        return res