from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        # suffix_max_idx[i] = i..n-1 里最高柱子的下标（取最左的那个最高）
        suffix_max_idx = [0] * n
        suffix_max_idx[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            best = suffix_max_idx[i + 1]
            if height[i] >= height[best]:
                suffix_max_idx[i] = i
                continue
            suffix_max_idx[i] = best

        water = 0
        left = 0

        while left < n - 1:
            right = left + 1

            # 找第一个 >= 左墙的右墙
            while right < n and height[right] < height[left]:
                right += 1

            # 如果找不到，就用右侧最高的柱子当右墙
            if right == n:
                right = suffix_max_idx[left + 1]

            bound = min(height[left], height[right])

            # 整盆算：水位 * 宽度 - 中间柱子总面积
            width = right - left - 1
            if width > 0:
                inside_sum = 0
                for k in range(left + 1, right):
                    inside_sum += height[k]
                water += bound * width - inside_sum

            left = right

        return water
