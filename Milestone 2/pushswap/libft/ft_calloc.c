/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 11:16:43 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/23 11:17:02 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

#include <stdlib.h>

void	*ft_calloc(size_t n, size_t size)
{
	void	*ptr;

	ptr = malloc (n * size);
	if (ptr == 0)
		return (NULL);
	ft_bzero(ptr, n * size);
	return (ptr);
}
