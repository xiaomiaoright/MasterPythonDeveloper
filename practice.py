class superDict(dict):
    def __len__(self):
        return 5
    def add_item(self, newKey, newValue):
        self[newKey] = newValue

a = {"a":1}
len(a)
a['b'] = 2
a

a = superDict()
a.add_item('a', 1)
a