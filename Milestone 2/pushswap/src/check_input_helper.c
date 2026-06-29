/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_input_helper.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 11:22:27 by crodrigo          #+#    #+#             */
/*   Updated: 2026/02/16 13:14:28 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

char	*join_args(int argc, char **argv)
{
	int		i;
	char	*tmp;
	char	*res;

	res = ft_strdup("");
	if (!res)
		return (NULL);
	i = 1;
	while (i < argc)
	{
		tmp = ft_strjoin(res, argv[i]);
		free(res);
		if (!tmp)
			return (NULL);
		res = ft_strjoin(tmp, " ");
		free(tmp);
		if (!res)
			return (NULL);
		i++;
	}
	return (res);
}

void	free_split(char **split)
{
	int	i;

	if (!split)
		return ;
	i = 0;
	while (split[i])
	{
		free(split[i]);
		i++;
	}
	free(split);
}
