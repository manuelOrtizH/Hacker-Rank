#Manuel Ortiz Hernández at 2020
#Linked Lists. Extracted from: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

def insert_node_at_tail(head, data):
    return head
                
            
if __name__ == '__main__':
    
    llist_count = int(input())
    llist = SinglyLinkedList()
    print('--------\n')

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insert_node_at_tail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
    

    
