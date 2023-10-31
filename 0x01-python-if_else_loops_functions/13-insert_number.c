#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - Inserts number into a sorted singly linked list
 * @head: Pointer to head
 * @number: Integer
 * Return: Address of new node on success, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *act;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else if (number <= (*head)->n)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		act = *head;
		while (act->next != NULL && number > act->next->n)
		{
			act = act->next;
		}
		new->n = number;
		new->next = act->next;
		act->next = new;
		return (new);
	}
	return (NULL);
}
