from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        # 1) 前缀和：prefix[i] = sum(height[0..i-1])
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + height[i]

        # 2) suffix_max_idx[i] = i..n-1 中最高柱子的下标（取最左的最高）
        suffix_max_idx = [0] * n
        suffix_max_idx[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            best = suffix_max_idx[i + 1]
            if height[i] >= height[best]:
                suffix_max_idx[i] = i
                continue
            suffix_max_idx[i] = best

        # 3) 从左到右围盆地
        water = 0
        left = 0

        while left < n - 1:
            right = left + 1

            # 找第一个 >= 左墙的右墙
            while right < n and height[right] < height[left]:
                right += 1

            # 找不到就用右侧最高的柱子当右墙
            if right == n:
                right = suffix_max_idx[left + 1]

            bound = min(height[left], height[right])
            width = right - left - 1

            if width > 0:
                inside_sum = prefix[right] - prefix[left + 1]  # O(1) 求中间柱子和
                water += bound * width - inside_sum

            left = right

        return water
