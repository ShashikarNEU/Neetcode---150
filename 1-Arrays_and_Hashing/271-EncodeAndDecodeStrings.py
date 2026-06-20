# Good Question
# Thought Process [EDGE CASES!!]
# First, you think about spaces and where to insert them. then you put random char(/) bw spaces to solve it
# But, there can be / alreasy in list of strings Eg:- ["nee/t", "co/de"] (Ur logic is wrong)
# Then add length and try to divide based on that. this will work and length can more than 9 also. So, insert # to know when to stop
# counting eg:- [554#ufuyfu...] (You should know till what range numbers are there)
# even if there are # in list of strings, it won't matter since we can skip them
# https://neetcode.io/solutions/encode-and-decode-strings

from ast import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedWord = ""
        for st in strs:
            l = len(st)
            occurance = str(l) + "#"
            encodedWord += occurance
            encodedWord += st
        return encodedWord

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i+=1
            k = int(num)
            result.append(s[i+1:i+1+k])
            i = i+1+k
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Call the test function
if __name__ == "__main__":
    codec = Codec()
    string = codec.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])
    print(string)
    print(codec.decode(string))
    