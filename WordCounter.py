import string


class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [[] for i in range(self.MAX)]

    def getHashKey(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def addWord(self, key):

        modify = False
        h = self.getHashKey(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key, element[1] + 1)
                modify = True
        if not modify:
            self.arr[h].append((key, 1))

    def __getitem__(self, key):
        h = self.getHashKey(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.getHashKey(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

    def printWordCount(self):
        count = 0
        diffWords = 0
        for i in range(len(self.arr)):
            for index, element in enumerate(self.arr[i]):
                print(element[0] + ': ' + str(element[1]) + '\r')
                count +=1
                diffWords += element[1]
        print('Unique word count = ' + str(count))
        print('Total word count = ' + str(diffWords))


if __name__ == '__main__':
    table = HashTable()
    with open('/Users/samlindaman/PycharmProjects/PoemWordCounter/venv/poem.txt', 'r') as file:
        for line in file:
            line = line.translate(str.maketrans('', '', string.punctuation))
            for word in line.split():
                table.addWord(word.lower())

    table.printWordCount()
