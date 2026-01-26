def get_item (self, key):
    index = self._hash(key)
    if self.data_map[index] is not None:
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]
    return None

def keys(self):
    all_keys = []
    for i in range(len(self.data_map)):
        if self.data_map[i] is not None:
            for j in range(len(self.data_map[i])):
                all_keys.append(self.data_map[i][j][0])
    return all_keys