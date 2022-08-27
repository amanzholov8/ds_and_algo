class TrieNode:
  def __init__(self):
    self.children = dict()
    self.isWordEnd = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for ch in word:
      if not ch in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.isWordEnd = True

  def search(self, word):
    node = self.root
    for ch in word:
      if not ch in node.children:
        return False
      node = node.children[ch]
    return node.isWordEnd

  def prefix(self, prefix):
    node = self.root
    for ch in prefix:
      if not ch in node.children:
        return False
      node = node.children[ch]
    return True