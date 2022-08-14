def neighborhood(word, word_set):
    for index in range(len(word)):
        for char in ascii_lowercase:
            if char == word[index]:
                continue
            if (neighbor := word[:index] + char + word[index + 1:]) in word_set:
                yield neighbor

def find_distances(end_word, word_set):
    distances = {end_word: 0}
    queue = deque([end_word])
    while queue:
        word = queue.popleft()
        for next_word in neighborhood(word, word_set):
            if next_word not in distances:
                distances[next_word] = distances[word] + 1
                queue.append(next_word)
    return distances

def find_ladders(begin_word, end_word, word_set, distances):
    ladders = []
    path = [begin_word]
    
    def explore():
        word = path[-1]
        if word == end_word:
            ladders.append(path[:])
            return

        for neighbor in neighborhood(word, word_set):
            if distances[neighbor] != distances[word] - 1:
                continue
            path.append(neighbor)
            explore()
            path.pop()
    
    explore()
    return ladders

class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        word_set = set(word_list) | {begin_word}
        distances = find_distances(end_word, word_set)
        return find_ladders(begin_word, end_word, word_set, distances)