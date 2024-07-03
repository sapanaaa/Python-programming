class alist:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]


# Usage:
l1 = alist([1, 'star', 50, 29])
element = l1[1]
print(element)