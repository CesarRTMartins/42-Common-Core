/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 12:29:41 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/21 12:44:04 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	unsigned char	x;
	size_t			len;

	x = (unsigned char)c;
	len = ft_strlen(s);
	while (1)
	{
		if ((unsigned char)s[len] == x)
			return ((char *) &s[len]);
		if (len == 0)
			return (NULL);
		len--;
	}
	return (NULL);
}
/*
#include <stdio.h>

int main(void)
{
    const char *texto = "ana";
    char *ptr = ft_strrchr(texto, 'a');

    if (ptr)
        printf("Último 'a' encontrado em: %s\n", texto);
    else
        printf("Caractere não encontrado.\n");
}*/
