class HashTable:
    def __init__(self, size=53):
        self.KeyMap = [0 for i in range(size)]

    def __hash(self, key):
        total = 0
        WEIRD_PRIME = 31
        for i in range(min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96
            total = (total * WEIRD_PRIME + value) % len(self.KeyMap)
        return total

    def Set(self, Key, Value):
        index = self.__hash(Key)
        if self.Get(Key):
            return "Key Already Exist"
        if self.KeyMap[index] == 0:
            self.KeyMap[index] = [[Key, Value]]
        else:
            self.KeyMap[index].append([Key, Value])

    def Get(self, Key):
        index = self.__hash(Key)
        if self.KeyMap[index] == 0:
            return None
        for i in self.KeyMap[index]:
            if i[0] == Key:
                return i[1]

    def GetKeys(self):
        Keys = []
        for i in self.KeyMap:
            if i == 0:
                pass
            else:
                for j in i:
                    Keys.append(j[0])
        return Keys

    def GetValues(self):
        Values = []
        for i in self.KeyMap:
            if i == 0:
                pass
            else:
                for j in i:
                    if j[1] not in Values:
                        Values.append(j[1])
        return Values


l = HashTable()
l.Set("Make", 9)
l.Set("Cake", "Cat")
l.Set("Laugh", 7)
l.Set('dv', 78)
l.Set('v', 78)
l.Set('v', 67)