/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 16:22:21 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/23 10:54:19 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*ptr_dest;

	ptr_dest = dest;
	if (ptr_dest < (unsigned char *) src)
		return (ft_memcpy(dest, src, n));
	else if (ptr_dest > (unsigned char *) src)
	{
		while (n--)
			ptr_dest[n] = ((unsigned char *) src)[n];
	}
	return (dest);
}
/*
#include <stdio.h>
int	main(void)
{
	char str1[20] = "abcdef";
	char str2[20] = "123456";

	ft_memmove(str1, str2, 3);
	printf("%s\n", str1); // Esperado: "123def"

	char str3[20] = "OverlapTest";
	ft_memmove(str3 + 2, str3, 8);
	printf("%s\n", str3); // Esperado: "OvOverlap"

	return (0);
}*/
