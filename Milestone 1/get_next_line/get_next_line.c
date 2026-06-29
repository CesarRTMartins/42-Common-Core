/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 13:08:51 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/27 13:08:54 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*get_newline(char *str, int fd)
{
	ssize_t	readbytes;
	char	*buffer;
	char	*tmp;

	buffer = malloc((sizeof(char) * (BUFFER_SIZE + 1)));
	if (!buffer)
		return (NULL);
	while (!str || !ft_strchr(str, '\n'))
	{
		readbytes = read(fd, buffer, BUFFER_SIZE);
		if (readbytes < 0)
			return (free(buffer), free(str), NULL);
		if (readbytes == 0)
			break ;
		buffer[readbytes] = '\0';
		tmp = str;
		str = ft_strjoin(tmp, buffer);
		if (!str)
			return (free(buffer), NULL);
	}
	free(buffer);
	return (str);
}

static char	*set_newline(char	*str)
{
	int		i;
	char	*line;

	if (!str || !str[0])
		return (NULL);
	i = 0;
	while (str[i] && str[i] != '\n')
		i++;
	if (str[i] == '\n')
		i++;
	line = malloc(i + 1);
	if (!line)
		return (NULL);
	i = 0;
	while (str[i] && str[i] != '\n')
	{
		line[i] = str[i];
		i++;
	}
	if (str[i] == '\n')
		line[i++] = '\n';
	line[i] = '\0';
	return (line);
}

char	*clean_rest(char *str)
{
	int		i;
	int		j;
	char	*new;

	if (!str)
		return (NULL);
	i = 0;
	j = 0;
	while (str[i] && str[i] != '\n')
		i++;
	if (!str[i])
	{
		return (free(str), NULL);
	}
	i += 1;
	new = malloc(ft_strlen(str + i) + 1);
	if (!new)
	{
		return (free(str), NULL);
	}
	while (str[i])
		new[j++] = str[i++];
	new[j] = '\0';
	free(str);
	return (new);
}

char	*get_next_line(int fd)
{
	static char	*rest;
	char		*line;

	if (fd < 0 || fd >= 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	rest = get_newline(rest, fd);
	if (!rest)
		return (NULL);
	line = set_newline(rest);
	if (!line)
	{
		free(rest);
		rest = NULL;
		return (NULL);
	}
	rest = clean_rest(rest);
	return (line);
}
/*int main(void)
{
int fd1 = open("test1.txt", O_RDONLY);

if (fd1 < 0 || fd2 < 0 || fd3 < 0)
{
    perror("Erro ao abrir ficheiros");
    return (1);
}

char *l1;

// Lê 1 linha de cada ficheiro por ciclo
while (1)
{
    l1 = get_next_line(fd1);

    if (!l1)
        break;

    if (l1)
    {
        printf("[FILE 1] %s", l1);
        free(l1);
    }
}

close(fd1);

return 0;

}*/
