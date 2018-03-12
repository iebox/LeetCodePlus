# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers My Submissions Question
# Total Accepted: 110384 Total Submissions: 510092 Difficulty: Medium
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # number1 = l1.val + l1.next.val * 10 + l1.next.next.val * 100
        # number2 = l2.val + l2.next.val * 10 + l2.next.next.val * 100
        number1 = self.listToNumber(l1)
        number2 = self.listToNumber(l2)

        sum = number1 + number2

        return self.numberToList(sum)

    def listToNumber(self, listHead):
    	number = 0
    	n = 0
    	currentNode = listHead
    	while currentNode != None:
    		number += ( currentNode.val * (10 ** n) )
    		currentNode = currentNode.next
    		n += 1
    	# print number
    	return number

    def numberToList(self, number):
    	digitCount = len(str(number))
    	head = ListNode(number % 10)
    	currentNode = head
    	n = 1

    	while n < digitCount:
    		node = ListNode(number/ (10 ** n) % 10)

    		# node.next = head
    		# head = node
    		currentNode.next = node
    		currentNode = node

    		n += 1

    	return head



# score
# Your runtime beats 31.77% of python submissions.

class LinkList(object):
	def __init__(self, values):
		head = ListNode(values[0])
		currentNode = head
		for value in values[1:]:
			node = ListNode(value)
			# node.next = head
			# head = node
			currentNode.next = node
			currentNode = node
			
		self.head = head

	def printList(self, head):
		listShow = ''
		while head != None:
			listShow += '%d -> ' % (head.val)
			head = head.next
		print listShow[:-3]


def test():
    linkList1 = LinkList([2, 4, 9, 4])
    linkList2 = LinkList([5, 6, 4])

    solution = Solution()
    linkListSum = solution.addTwoNumbers(linkList1.head, linkList2.head)

    linkList1.printList(linkListSum)

test()

"""
thinking

1. get the actual 2 numbers
2. calculate the sum
3. reverse the digit and create the list

"""