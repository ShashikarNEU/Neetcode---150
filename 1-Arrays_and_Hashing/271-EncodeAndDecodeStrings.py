# Good Question
# Thought Process [EDGE CASES!!]
# First, you think about spaces and where to insert them. then you put random char(/) bw spaces to solve it
# But, there can be / alreasy in list of strings Eg:- ["nee/t", "co/de"] (Ur logic is wrong)
# Then add length and try to divide based on that. this will work and length can more than 9 also. So, insert # to know when to stop
# counting eg:- [554#ufuyfu...] (You should know till what range numbers are there)
# even if there are # in list of strings, it won't matter since we can skip them
# https://neetcode.io/solutions/encode-and-decode-strings

class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res
        

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i]!='#':
                length += s[i]
                i+=1
            k = int(length)
            i+=1
            res.append(s[i:i+k])
            i+=(k)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Call the test function
if __name__ == "__main__":
    codec = Codec()
    string = codec.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])
    print(string)
    print(codec.decode(string))
    