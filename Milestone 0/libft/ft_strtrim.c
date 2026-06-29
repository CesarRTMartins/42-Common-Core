/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 12:06:25 by crodrigo          #+#    #+#             */
/*   Updated: 2025/10/21 12:28:16 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdio.h>

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;
	char	*str;

	if (!s1)
		return (NULL);
	if (!set)
		return (ft_strdup(s1));
	start = 0;
	end = (ft_strlen(s1) - 1);
	while (s1[start] && ft_strchr(set, s1[start]))
		++start;
	while (s1[start] && ft_strchr(set, s1[end]))
		--end;
	str = ft_substr(s1, start, ((end - start) + 1));
	return (str);
}
/*
int main(void)
{
    char *res;

    // Teste 1: Remover espaços no início e no fim
    res = ft_strtrim("   hello   ", " ");
    printf("1. '%s'\n", res);
    free(res);

    // Teste 2: Remover múltiplos tipos de caracteres
    res = ft_strtrim("***hello***", "*");
    printf("2. '%s'\n", res);
    free(res);

    // Teste 3: Remover caracteres variados
    res = ft_strtrim("xyzhellozyx", "xyz");
    printf("3. '%s'\n", res);
    free(res);

    // Teste 4: Nenhum caractere a remover
    res = ft_strtrim("hello", " ");
    printf("4. '%s'\n", res);
    free(res);

    // Teste 5: String completamente composta pelos caracteres de 'set'
    res = ft_strtrim("xxxxx", "x");
    printf("5. '%s'\n", res);
    free(res);

    // Teste 6: String vazia
    res = ft_strtrim("", " ");
    printf("6. '%s'\n", res);
    free(res);

    // Teste 7: 'set' é vazio (não corta nada)
    res = ft_strtrim("   hello   ", "");
    printf("7. '%s'\n", res);
    free(res);

    // Teste 8: 'set' é NULL
    res = ft_strtrim("hello", NULL);
    printf("8. '%s'\n", res);
    free(res);

    // Teste 9: 's1' é NULL (deve retornar NULL)
    res = ft_strtrim(NULL, " ");
    printf("9. %s\n", res == NULL ? "NULL" : res);

    // Teste 10: Corta apenas no início
    res = ft_strtrim("###hello", "#");
    printf("10. '%s'\n", res);
    free(res);

    // Teste 11: Corta apenas no fim
    res = ft_strtrim("hello***", "*");
    printf("11. '%s'\n", res);
    free(res);

    return 0;
}*/
