class TrieNode:
    def __init__(self):
        self.is_word = False
        self.data = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.data.get(letter)
            if not child:
                node.data[letter] = TrieNode()
            node = node.data[letter]
        node.is_word = True
    def search(self, word):
        cur = ''
        ans = []
        node = self.root
        for letter in word:
            node = node.data.get(letter)
            cur += letter
            if not node:
                return ans
            if (node.is_word == True):
                ans.append(cur)
        return ans

trie = Trie()
s = "abcdefg"
d = ['ab','abc','abcd','bcd','bcde','bde','efg']
for x in d:
    trie.insert(x)
print(trie.root.data)
for i in range(0,len(s)):
    lst = trie.search(s[i:])
    if(len(lst)!=0):
        print(lst)