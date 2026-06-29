/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 10:56:13 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/23 11:09:26 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	x;
	size_t			i;
	unsigned char	*ptr;

	i = 0;
	x = (unsigned char)c;
	ptr = (unsigned char *)s;
	while (i < n)
	{
		if (ptr[i] == x)
		{
			return (&ptr[i]);
		}
		i++;
	}
	return (NULL);
}
/*
#include <stdio.h>
int main()
{
    char *d = "addadd123243fggrt";

    ft_memchr(d,'t',30);

	printf("%s", d);
}*/
