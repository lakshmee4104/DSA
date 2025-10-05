
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Creating a Graph is the task here
        ## Art is in creating graph (patterns)
        ## shortest transformation sequence.. No word is visited twice
        ## BFS in undirected graph.

        if beginWord not in wordList:
            wordList.append(beginWord)
        
        patterns = {}
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                pattern = word[0:i]+"*"+word[i+1:]
                if pattern in patterns:
                    patterns[pattern].append(word)
                else:
                    patterns[pattern] = [word]
        
        visitedSet = set()

        bfs_queue = collections.deque([(beginWord, 1)])
        visitedSet.add(beginWord)

        while bfs_queue:
            word, num = bfs_queue.popleft()
            if word == endWord:
                return num
            for i in range(length):
                pattern = word[0:i]+"*"+ word[i+1:]
                for nei in patterns[pattern]:
                    if nei != word and nei not in visitedSet:
                        visitedSet.add(nei)
                        bfs_queue.append((nei, num+1))

        return 0
