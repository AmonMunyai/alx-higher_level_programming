#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included in new node.
 * Return: address of the new element or NULL if it fails.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	temp = *head;

	/* allocate and validate memory */
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	/* populate node */
	node->n = number;

	/* insert node */
	while (temp)
	{
		if (node->n > temp->n && node->n < temp->next->n)
		{
			node->next = temp->next;
			temp->next = node;
			break;
		}
		temp = temp->next;
	}

	return (node);
}
