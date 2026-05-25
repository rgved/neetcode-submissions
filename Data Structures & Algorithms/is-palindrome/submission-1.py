class Solution:
    def isPalindrome(self, s: str) -> bool:
        c="".join(char.lower() for char in s if char.isalnum())
        noSpace=c.replace(" ","")
        forward=[]
        back=[]
        for i in range(0,len(noSpace)):
            forward.append(noSpace[i])
        for i in range(len(noSpace)-1,-1,-1):
            back.append(noSpace[i])

        return back==forward
            