class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_count_map = {}
        for char in s:
            if char in character_count_map.keys():
                character_count_map[char] += 1
            else:
                character_count_map[char] = 1

        for char in t:
            if char not in character_count_map.keys():
                return False
            else:
                character_count_map[char] -= 1
                if character_count_map[char] == 0:
                    character_count_map.pop(char)

        if not character_count_map:
            return True
        else:
            return False