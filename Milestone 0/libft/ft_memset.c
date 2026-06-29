/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 16:10:29 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/21 16:12:30 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*p;
	unsigned char	x;
	size_t			i;

	p = s;
	x = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		p[i] = x;
		i++;
	}
	return (s);
}
/*
#include <stdio.h>
int main()
{
    unsigned char c[] = "ola boas people";

    ft_memset(c, 'X', 5);

    printf("%s\n", c);
}*/
