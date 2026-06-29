/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_u.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 14:29:26 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/06 14:31:24 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_put_u(unsigned int arg)
{
	int			count;
	long int	nbr;

	count = 0;
	nbr = (long int)arg;
	if (nbr < 0)
	{
		nbr *= -1;
		nbr = 4294967294 + nbr;
	}
	if (nbr < 10)
	{
		ft_put_c(arg + '0');
		return (1);
	}
	count += ft_put_d(nbr / 10) + 1;
	ft_put_c(nbr % 10 + '0');
	return (count);
}
