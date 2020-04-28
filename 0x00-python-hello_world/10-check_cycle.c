#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: linked list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *header = list;
	listint_t *checker = header;

	while (header != NULL && checker != NULL && check->next != NULL)
	{
		header = header->next;
		checker = check->next->next;

		if (checker == header)
		{
			return (1);
		}
	}
	return (0);
}
