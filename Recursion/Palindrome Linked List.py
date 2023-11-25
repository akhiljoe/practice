# # Given the head of a singly linked list, return true if it is a palindrome  or false otherwise.


class Solution(object):
    def isPalindrome(self, head):
        if len(head)<=1:
            return True
        if head[0]!=head[-1]:
            return False
        else:
            return self.isPalindrome(head[1:-1])

if __name__ == '__main__':
    instance = Solution()
    head = [2,2]
    print(instance.isPalindrome(head))