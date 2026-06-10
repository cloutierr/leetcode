class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def count(self, node: self.Node, d: dict[int: self.Node]):
        ret = 1
        if node.next is not None:
            ret += self.count(node.next, d)
        d.pop(node.val)
        return ret
        

    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        My immediate intuition is insert the numbers adjacent to each number into a dictionary. If the number is already a key in the dictionary, it connects to at least one other number. This issue is I need to know whether one group connects to another group: like if i have [1,2,3,4] and [6,7,8,9] and a [5] shows up, I need to know that it doesn't just connect to one of them, it connects both groups to form a group of 9. 
        Could attach an array as the key's value and update it as we go. Basically remove all non-edge numbers (meaning remove dict entries that are connected on both sides) when we connect an adjacent node to them (and the length of the key's array is already greater than 1, which means that there's another node connected to the other side of it).

        Alright let's run through an example real quick to make sure we've got it worked out.
        nums[0] = 4
        dict[3] = [4]
        dict[5] = [4]
        nums[1] = 5
        dict.get(5) is not None so:
        dict[5][len-1] == 5-1 so:
        dict[6] = [4,5]
        dict[dict[5-1][0]-1] += [5]  # we need to update both arrays which would be O(n) when inserting into index 0. Not good. Could I not just add one array to the other first? That's also O(n)

        Maybe we can use a linked list so that we just need to count the number of continuous nodes at the end.
        Each key is going to store a Node with its value and attach itself to the node of its neighbor. How would we remove the neighbor's key value pair?
        We're not going to remove any since there could be duplicates in nums: we have to first check whether our number has already been found.
        I also want to change up the way that we're doing it slightly: I'm going to store an existing value rather than the values that we're looking for. I will check +/-1 in each direction of the incoming value to determine if it can be added to a chain.

        Alright, I think that works. Let's code it up.
        '''
        longest = 0
        hashMap : dict[int: self.Node] = {}  # each entry stores a number and a representative LinkedList node

        for num in nums:
            if hashMap.get(num) is not None:
                continue  # we've already handled this number
            
            if hashMap.get(num-1) is not None and hashMap.get(num+1) is not None:
                # this number connects 2 chains
                prev = hashMap[num-1]
                nxt = hashMap[num+1]
                # connections prev <-> curr
                prev.next = self.Node(num)
                prev.next.prev = prev  # really high quality code here. the kind of code faang only dreams of
                # connections curr <-> next
                nxt.prev = prev.next
                nxt.prev.next = nxt
                # add to hashMap
                hashMap[num] = prev.next
            elif hashMap.get(num-1) is not None:
                prev = hashMap[num-1]
                prev.next = self.Node(num)
                prev.next.prev = prev
                hashMap[num] = prev.next
            elif hashMap.get(num+1) is not None:
                nxt = hashMap[num+1]
                nxt.prev = self.Node(num)
                nxt.prev.next = nxt
                hashMap[num] = nxt.prev
            else:
                hashMap[num] = self.Node(num)  # disconnected node

        while hashMap:  # should return False if empty
            count = 0
            value: self.Node = next(iter(hashMap.values()))
            while value.prev is not None:
                value = value.prev  # find the head of the linked list
            count += self.count(value, hashMap)
            if count > longest:
                longest = count

        return longest
