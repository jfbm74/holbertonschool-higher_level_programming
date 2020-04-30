#include "lists.h"
/**
 * insert_node - Return new node
 * @head: Address of first node
 * @number: Value of new node
 * Return: New node if exits
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *pivot;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
	pivot = *head;
	new->next = NULL;
	if (new->n < pivot->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (pivot->next != NULL)
		{
			pivot = pivot->next;
			if (new->n < pivot->n)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
	}
	current->next = new;
	return (new);
}
