/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:18:29 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/29 11:18:40 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*tmp;
	t_list	*node;

	if (!lst)
		return ;
	node = *lst;
	while (node != NULL)
	{
		tmp = node;
		(*del)(node->content);
		node = node->next;
		free(tmp);
	}
	*lst = NULL;
}
