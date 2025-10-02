class Solution:
    def isValid(self, s: str) -> bool:
        bracket_maping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        checking_list = []
        for ch in s:
            if ch in bracket_maping:
                checking_list.append(ch)
            elif not checking_list:
                return False
            elif ch == bracket_maping[checking_list[-1]]:
                checking_list.pop()
            else:
                return False

        if not checking_list:
            return True
        else:
            return False