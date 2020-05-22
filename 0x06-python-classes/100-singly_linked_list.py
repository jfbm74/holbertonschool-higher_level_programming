#!/usr/bin/python3
"""This module creates a Class Node and Class SinglyLinkedList"""


class Node:
    """Class Node with a constuctor method"""

    def __init__(self, data, next_node=None):
        """
        Initializes square
        Args:
            data: data for __data attribute
            next_node: the address of the next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        getter function of data
        Returns:
            data of node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter function of data
        Args:
            value: value for __data attribute
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        getter function of next_node
        Returns:
            next_node of the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter function of next_node
        Args:
            value: value for __next_node attribute
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class Node with a constuctor method"""

    def __init__(self):
        """
        Initializes square
        """
        self.__head = None

    def __str__(self):
        """
        brings the string version of a list
        Returns:
            list in form of a string
        """
        if self.__head is None:
            return ""
        else:
            str_list = ""
            temp = self.__head
            while temp:
                str_list += str(temp.data)
                temp = temp.next_node
                if temp is not None:
                    str_list += "\n"
            return str_list

    def sorted_insert(self, value):
        """
        inserts a node in order
        Args:
            value: value for __data attribute
        """
        if self.__head is None or self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            temp = self.__head
            while temp.next_node and temp.next_node.data < value:
                temp = temp.next_node
            temp.next_node = Node(value, temp.next_node)
