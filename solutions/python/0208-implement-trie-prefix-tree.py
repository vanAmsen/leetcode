class TrieNode: 
    def __init__(self):  
        self.children = {} 
        self.is_end_of_word = False 
                  
class Trie:

    def __init__(self):
        self.root = TrieNode() 
               
    def insert(self, word: str) -> None:
        node = self.root 
        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = TrieNode() 
            node = node.children[ch] 
        node.is_end_of_word = True 
                                                                          
    def search(self, word: str) -> bool:
        node = self.root 
        for ch in word: 
            if ch not in node.children: 
                return False 
            node = node.children[ch] 
        return node.is_end_of_word 
                                                                          
    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for ch in prefix: 
            if ch not in node.children: 
                return False 
            node = node.children[ch] 
        return True 
                                                                          


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
