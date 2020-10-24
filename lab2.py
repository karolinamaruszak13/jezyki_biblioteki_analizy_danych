import re

class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def delete_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]

    def add_edge(self, vertex, edge):
        if vertex in self.vertices and edge in self.vertices:
            if vertex not in self.vertices[edge] and edge not in self.vertices[vertex]:
                self.vertices[vertex].append(edge)
                self.vertices[edge].append(vertex)

    def delete_edge(self, v, u):
        if v in self.vertices and u in self.vertices:
            if u in self.vertices[v] and v in self.vertices[u]:
                self.vertices[u].remove(v)
                self.vertices[v].remove(u)

    def get_neighbors(self, vertex):
        return [v for v in self.vertices[vertex]]

    def __str__(self):
        result = []
        for v in self.vertices:
            if self.vertices[v]:
                for e in self.vertices[v]:
                    result.append(v + e)
            else:
                result.append(v)
        return str(result)

    def bfs(self, vertex):
        visited = []
        queue = []
        queue.append(vertex)
        visited.append(vertex)
        while queue:
            c = queue.pop(0)
            print(c, end=" ")
            for u in self.get_neighbors(c):
                if u not in visited:
                    queue.append(u)
                    visited.append(u)

    def dfs(self, vertex):
        visited = []
        stack = []
        stack.append(vertex)
        visited.append(vertex)
        while stack:
            c = stack.pop()
            print(c, end=" ")
            for u in self.get_neighbors(c):
                if u not in visited:
                    stack.append(u)
                    visited.append(u)


def generate_sentences_from_txt(file):
    sentence = [" "]
    for row in open(file, "r", encoding='utf-8'):
        for letter in row:
            if letter == "\n":
                sentence.append(" ")
            else:
                sentence.append(letter)
            if letter == ".":
                sentence.pop(0)
                yield ''.join(sentence)
                sentence = []


def generate_tokens_from_txt(file):
    import string
    r = re.compile(r'[\s{}]+'.format(re.escape(string.punctuation)))
    for row in open(file, "r", encoding='utf-8'):
        for word in row.split(" "):
            if r.split(word)[0]:
                yield r.split(word)[0]
            for special_characer in string.punctuation:
                if special_characer in word:
                    yield special_characer
                    break

        # for letter in row:
        #     yield letter


def generate_sentences_from_conll(file):
    sentence = []
    for row in open(file, "r", encoding='utf-8'):
        word = re.findall(r'"(.*?)"', row)[0]
        if word in [".", "?", "...", "!"]:
            result = " ".join(sentence) + word
            result = result.replace(" ,", ",")
            result = result.replace("( ", "(")
            result = result.replace(" )", ")")
            yield result
            sentence = []
        else:
            sentence.append(word)


def generate_tokens_from_conll(file):
    for row in open(file, "r", encoding='utf-8'):
        word = re.findall(r'"(.*?)"', row)[0]
        yield word
        # word = list(re.findall(r'"(.*?)"', row)[0])
        # if " " in word:
        #     word.remove(" ")
        # for letter in word:
        #     yield letter




graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'E')
graph.add_edge('B', 'F')
graph.bfs('A')
print()
graph.dfs('A')
# t = generate_sentences_from_txt('nkjp.txt')
tt = generate_tokens_from_txt('nkjp.txt')
# c = generate_sentences_from_conll('nkjp.conll')
# cc = generate_tokens_from_conll('nkjp.conll')

for line in tt:
    print(line)
