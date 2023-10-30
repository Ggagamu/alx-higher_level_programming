#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to list.
 * Return: 0 if no cycle, 1 cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;
	while (list && fast && fast->next)
	{
		list = list->next;
		fast = fast->next->next;

		if (list == fast)
		{
			list = slow;
			slow =  fast;
			while (1)
			{
				fast = slow;
				while (fast->next != list && fast->next != slow)
				{
					fast = fast->next;
				}
				if (fast->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
