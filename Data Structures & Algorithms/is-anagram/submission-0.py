class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
        
        ## O(n) time and O(n) space, supports are unicode characters
        #     fm_s = {}
        #     for char in s:
        #         fm_s[char] = fm_s.get(char, 0) + 1
            
        #     fm_t = {}
        #     for char in t:
        #         fm_t[char] = fm_t.get(char, 0) + 1
        #     return fm_s == fm_t

            temp = [0]*26
            cp_a = ord('a') #97

            for char in s:
                temp[ord(char) - cp_a] += 1
            for char in t:
                temp[ord(char) - cp_a] -= 1
            
            return temp == [0]*26

        return False