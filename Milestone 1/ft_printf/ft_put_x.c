/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_x.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 15:17:45 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/06 15:17:52 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static	int	recursive(unsigned long tmp, int uppercase)
{
	int				count;
	unsigned long	digit;
	char			c;

	count = 0;
	if (tmp > 15)
		count += recursive(tmp / 16, uppercase);
	digit = tmp % 16;
	if (digit < 10)
		c = digit + '0';
	else
	{
		if (uppercase == 1)
			c = (digit - 10) + 'A';
		else
			c = (digit - 10) + 'a';
	}
	count += ft_put_c(c);
	return (count);
}

int	ft_put_x(unsigned int n, int uppercase)
{
	if (n == 0)
	{
		write (1, "0", 1);
		return (1);
	}
	return (recursive(n, uppercase));
}
