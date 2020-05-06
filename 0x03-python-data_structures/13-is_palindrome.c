#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: first node of the list
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *list = (*head);
	int elements[4096];
	int i = 0, j;

	if (head == NULL || *head == NULL)
		return (1);

	while (list)
	{
		elements[i] = list->n;
		i++;
		list = list->next;
	}
	i--;
	for (j = 0; j <= i ; i--, j++)
	{
		if (elements[i] != elements[j])
			return (0);
	}
	return (1);
}