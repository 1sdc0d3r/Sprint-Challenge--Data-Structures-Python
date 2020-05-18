class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next


class RingBuffer:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.tones = []
        self.head = None
        self.tail = None

    def append(self, item):
        new_tone = Node(item)
        if not self.head:
            self.tones.append(item)
            self.head = new_tone
            self.tail = new_tone
        elif len(self.tones) < self.capacity:
            self.tones.append(item)
            new_tone.next = self.head
            self.head.prev = new_tone
            self.head = new_tone
        else:
            new_tone.next = self.head
            self.head.prev = new_tone
            self.head = new_tone
            self.tones = [new_tone.value if tone ==
                          self.tail.value else tone for tone in self.tones]
            self.tail = self.tail.prev

    def get(self):
        return self.tones


buffer = RingBuffer()

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')

buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('h')

print(buffer.get())
# print("head", buffer.head.value)
# print("head", buffer.head.next.value)
# print("tail", buffer.tail.value)


# new_tones = []
# for tone in self.tones:
#     if tone == self.tail.value:
#         new_tones.append(new_tone.value)
#     else:
#         new_tones.append(tone)
# self.tones = new_tones
