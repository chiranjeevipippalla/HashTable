#Code for Hashing using Separate Chaining.

#We are creating a HashNode class here.
#Each time you enter a data node, it will first pass through this.
#Each node will enter into the bucket of array.
class HashNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class HashTable:
    #Initialize the hashtable size in the __init__(self) method
    def __init__(self):
        self.table = [None]*101

    #Generate a hash value to save each of the HashNodes in the array. This will return the bucket index.
    def hash(self, key):
        hashed = 0

        for i in range(len(key)):
            hashed = (256*hashed + ord(key[i]))%101

        return hashed

    #Adding the elements into the hashtable.
    def add(self, key, value):
        bucket = self.hash(key)

        if not self.table[bucket]:
            self.table[bucket] = HashNode(key, value)
        else:
            temp = self.table[bucket]
            while temp.next:
                temp = temp.next

            temp.next = HashNode(key, value)

    #Finding an element in the hashtable.
    def find(self, key):
        bucket = self.hash(key)

        if not self.table[bucket]:
            return False
        else:
            temp = self.table[bucket]
            while temp:
                if temp.key == key:
                    return temp.value
                temp = temp.next

            return False

    #Delete an element from the hashtable
    def delete(self, key):
        bucket = self.hash(key)

        if not self.table[bucket]:
            return False
        else:
            if self.table[bucket].key == key:
                self.table[bucket] = None
            else:
                temp = self.bucket[key]
                while temp:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        return

                    temp = temp.next

                return False





        
