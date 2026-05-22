class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uni1="".join(sorted(s));
        uni2="".join(sorted(t));

        if(uni1==uni2):
            return True
        return False