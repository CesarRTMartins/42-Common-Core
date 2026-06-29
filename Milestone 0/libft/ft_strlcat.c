/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 15:40:10 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/21 15:44:06 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	dest_len;
	size_t	src_len;
	size_t	sum;

	i = 0;
	sum = 0;
	dest_len = ft_strlen(dst);
	src_len = ft_strlen(src);
	if (size > dest_len)
		sum = dest_len + src_len;
	else
		return (src_len + size);
	while (src[i] && (dest_len + 1) < size)
		dst[dest_len++] = src[i++];
	dst[dest_len] = '\0';
	return (sum);
}
/*
int main(void)
{
    char buffer1[20] = "Ola";
    char buffer2[20] = "Ola";
    char buffer3[20] = "Ola";

    size_t ret1 = ft_strlcat(buffer1, " Mundo", 20);   // Caso 1: cabe tudo
    size_t ret2 = ft_strlcat(buffer2, " Mundo", 8);    // Caso 2: cabe 
    size_t ret3 = ft_strlcat(buffer3, " Mundo", 3);    
    printf("Caso 1:\n");
    printf(" Resultado: \"%s\"\n", buffer1);
    printf(" Retorno: %zu\n\n", ret1);

    printf("Caso 2:\n");
    printf(" Resultado: \"%s\"\n", buffer2);
    printf(" Retorno: %zu\n\n", ret2);

    printf("Caso 3:\n");
    printf(" Resultado: \"%s\"\n", buffer3);
    printf(" Retorno: %zu\n\n", ret3);

    return 0;
}*/
