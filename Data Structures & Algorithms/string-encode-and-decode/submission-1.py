class Solution:

    def encode(self, strs: List[str]) -> str:
        se=""
        for i in strs:
            se=se+str(len(i))+"#"+i
        return se


    def decode(self, s):
        res = []

        i = 0

        while i < len(s):

            num = ""

            # collect digits
            while s[i] != "#":
                num += s[i]
                i += 1

            length = int(num)

            # skip #
            i += 1

            word = s[i:i+length]

            res.append(word)

            # jump ahead
            i += length

        return res