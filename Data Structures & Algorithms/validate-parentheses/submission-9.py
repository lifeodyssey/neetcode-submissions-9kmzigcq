class Solution:
    def isValid(self, s: str) -> bool:
        close_of = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in close_of:               #
                stack.append(ch)
                continue

            if ch not in close_of.values():          # 判断 value 集合
                return False

            # 3) 是右括号，但栈空：非法
            if not stack:
                return False

            # 4) 弹出一个左括号，看它应该配的右括号是不是当前 ch
            left = stack.pop()
            if close_of[left] != ch:
                return False

        return not stack
