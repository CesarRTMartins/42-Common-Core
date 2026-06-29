/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 11:10:49 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/23 11:16:27 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_isalnum(int c)
{
	if ((c > 47 && c < 58)
		|| (c >= 'a' && c <= 'z' )
		|| (c >= 'A' && c <= 'Z' ))
		return (1);
	else
		return (0);
}
/*
#include <stdio.h>
int main() 
{
    printf("%d", isalnum(65));
}*/
