/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 11:23:13 by crodrigo          #+#    #+#             */
/*   Updated: 2026/02/16 12:08:27 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_putstr(char *s)
{
	while (*s)
	{
		write(1, &*s, 1);
		s++;
	}
}

void	free_stack(t_stack **lst)
{
	t_stack	*c;

	if (!lst || !*lst)
		return ;
	while (*lst)
	{
		c = (*lst)->next;
		free(*lst);
		*lst = c;
	}
	*lst = NULL;
}

void	print_error_and_exit(t_stack **sa, char **split)
{
	if (sa && *sa)
		free_stack(sa);
	if (split)
		free_split(split);
	write(2, "Error\n", 6);
	exit(1);
}

int	absolute(int n)
{
	if (n < 0)
		return (-n);
	return (n);
}
