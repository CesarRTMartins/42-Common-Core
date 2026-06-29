/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 10:09:22 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/23 10:35:29 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static	unsigned int	ft_substr_count(char const *s, char c)
{
	size_t	i;
	size_t	count;

	i = 0;
	count = 0;
	while (s[i])
	{
		if (s[i] != c && (s[i + 1] == c || s[i + 1] == '\0'))
		{
			count++;
		}
		i++;
	}
	return (count);
}

static unsigned int	ft_substr_len(char const *s, char c)
{
	unsigned int	i;

	i = 0;
	while (s[i] && s[i] != c)
		i++;
	return (i);
}

static char	**ft_free(char **str, int i)
{
	while (i >= 0)
	{
		free(str[i]);
		i--;
	}
	free(str);
	return (NULL);
}

char	**ft_split(char const *s, char c)
{
	char	**str;
	int		i;
	int		j;

	str = malloc((ft_substr_count(s, c) + 1) * sizeof(char *));
	if (!s || !str)
		return (0);
	i = 0;
	j = 0;
	while (s[i] != '\0')
	{
		if (s[i] != c)
		{
			str[j] = ft_substr(s, i, ft_substr_len(&s[i], c));
			if (!str[j])
				return (ft_free(str, j));
			j++;
			i += ft_substr_len(&s[i], c);
		}
		else
			i++;
	}
	str[j] = 0;
	return (str);
}
/*
#include <stdio.h>
int main(void)
{
    char **res = ft_split("Altitudes;Canon;Tornado", ';');
    for (int i = 0; res[i]; i++)
        printf("%s\n", res[i]);
}*/
