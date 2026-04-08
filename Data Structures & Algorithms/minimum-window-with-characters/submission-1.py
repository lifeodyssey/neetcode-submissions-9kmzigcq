class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        window=defaultdict(int)
        required=len(need)
        formed=0

        required=len(need)
        formed=0

        left=0
        ans_len=float("inf")
        ans_l=0
        ans_r=0

        for right in range(len(s)):
            ch=s[right]
            window[ch]+=1
            if ch in need and window[ch]==need[ch]:
                formed+=1
            while formed==required:
                if right-left+1<ans_len:
                    ans_len=right-left+1
                    ans_l=left
                    ans_r=right
                left_ch=s[left]
                window[left_ch]-=1
                if left_ch in need and window[left_ch]<need[left_ch]:
                    formed-=1
                left+=1
        if ans_len==float("inf"):
            return ""
        return s[ans_l:ans_r+1]