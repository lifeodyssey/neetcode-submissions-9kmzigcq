class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        charSet = set()  # 存储当前窗口的字符
        left = 0         # 左指针
        maxLength = 0    # 最大长度
        
        # right指针从0到n-1遍历（只遍历一次！）
        for right in range(n):
            # 如果s[right]已经在窗口中，缩小窗口
            while s[right] in charSet:
                charSet.remove(s[left])  # 移除左边字符
                left += 1               # 左指针右移
            
            # 现在可以安全地添加s[right]
            charSet.add(s[right])
            # 更新最大长度
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
