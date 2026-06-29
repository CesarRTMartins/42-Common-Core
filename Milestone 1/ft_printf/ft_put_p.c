/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_p.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 14:31:33 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/06 14:32:04 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static	int	recursive(unsigned long tmp)
{
	int				count;
	unsigned long	digit;
	char			c;

	count = 0;
	if (tmp > 15)
		count += recursive(tmp / 16);
	digit = tmp % 16;
	if (digit < 10)
		c = digit + '0';
	else
		c = (digit - 10) + 'a';
	count += ft_put_c(c);
	return (count);
}

int	ft_put_p(void *arg)
{
	int				count;
	unsigned long	tmp;

	tmp = (unsigned long)arg;
	if (tmp == 0)
		return (write(1, "(nil)", 5));
	count = 0;
	write(1, "0x", 2);
	count += 2;
	count += recursive(tmp);
	return (count);
}
