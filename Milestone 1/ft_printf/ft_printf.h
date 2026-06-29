/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 14:28:43 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/06 14:37:12 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

int	ft_printf(const char *fmt, ...);
int	ft_put_c(int arg);
int	ft_put_d(int arg);
int	ft_put_p(void *arg);
int	ft_put_s(char *arg);
int	ft_put_u(unsigned int arg);
int	ft_put_x(unsigned int n, int uppercase);
#endif
