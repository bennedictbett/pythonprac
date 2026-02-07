###Reverse String Practice
#Reverse String O(1)extra memory
class solution:
    def reverse_string(self, s):
        l, r = 0, len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1


#Using stack space: O(n)
class solution:
    def reverse_string(self, s):
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1


 #Using Recusion Space O(n)
class solution:
    def ReverseString(self, s):

        def reverse(l,r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
        reverse(0, len(s) -1)



class solution:
    def lengthOfLastWord(self, s):
        i, length = len(s) -1, 0
        while i[s] == " ":
            i -= 1
        while i >= 0 and i[s] == " ":
            length += 1
            i += 1

        return length   