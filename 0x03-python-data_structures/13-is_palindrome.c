#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: first node of the list
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int len = 1;
	int i, j = 0;
	listint_t *pivot = NULL;

	pivot = *head;
	if (*head == NULL || pivot->next == NULL)
		return (1);
	while (pivot->next != NULL)
	{
		len++;
		pivot = pivot->next;
	}
	int array[len];

	pivot = *head;
	for (i = 0; i < len; i++)
	{
		array[i] = pivot->n;
		pivot = pivot->next;
	}
	for (i = 0, j = (len - 1); i < j; i++, j--)
	{
		if (array[i] != array[j])
			return (0);
	}
	return (1);
}