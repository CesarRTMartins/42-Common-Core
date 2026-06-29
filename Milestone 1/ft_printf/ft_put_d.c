/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_d.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 14:33:52 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/06 14:35:28 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_put_d(int arg)
{
	int			count;
	long int	nbr;

	count = 0;
	nbr = (long int)arg;
	if (nbr < 0)
	{
		ft_put_c('-');
		count++;
		nbr *= -1;
	}
	if (nbr > 9)
		count += ft_put_d(nbr / 10);
	count += ft_put_c(nbr % 10 + '0');
	return (count);
}
