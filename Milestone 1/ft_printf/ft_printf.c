/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 14:27:08 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/06 14:38:01 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	check_flag(va_list args, const char str)
{
	if (str == 'c')
		return (ft_put_c(va_arg(args, int)));
	else if (str == 's')
		return (ft_put_s(va_arg(args, char *)));
	else if (str == 'p')
		return (ft_put_p(va_arg(args, void *)));
	else if (str == 'd' || str == 'i')
		return (ft_put_d(va_arg(args, int)));
	else if (str == 'u')
		return (ft_put_u(va_arg(args, unsigned int)));
	else if (str == '%')
		return (ft_put_c('%'));
	else if (str == 'x')
		return (ft_put_x(va_arg(args, unsigned int), 0));
	else if (str == 'X')
		return (ft_put_x(va_arg(args, unsigned int), 1));
	return (0);
}

int	ft_printf(const char *fmt, ...)
{
	int		count;
	va_list	args;

	count = 0;
	va_start(args, fmt);
	if (!fmt)
		return (-1);
	while (*fmt)
	{
		if (*fmt == '%')
		{
			count += check_flag(args, *(fmt + 1));
			fmt++;
		}
		else
			count += ft_put_c(*fmt);
		fmt++;
	}
	va_end(args);
	return (count);
}
/*
int	main(void)
{
	ft_printf("%s", "Ola people");
	return (0);
}*/
