/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 12:10:08 by crodrigo          #+#    #+#             */
/*   Updated: 2025/11/27 12:58:40 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static char	*get_newline(char *str, int fd)
{
	ssize_t		readbytes;
	char		*buffer;
	char		*tmp;

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
	static char	*rest[1024];
	char		*line;

	if (fd < 0 || fd >= 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	rest[fd] = get_newline(rest[fd], fd);
	if (!rest[fd])
		return (NULL);
	line = set_newline(rest[fd]);
	if (!line)
	{
		free(rest[fd]);
		rest[fd] = NULL;
		return (NULL);
	}
	rest[fd] = clean_rest(rest[fd]);
	return (line);
}
/*
int main(void)
{
int fd1 = open("test1.txt", O_RDONLY);
int fd2 = open("test2.txt", O_RDONLY);
int fd3 = open("test3.txt", O_RDONLY);

if (fd1 < 0 || fd2 < 0 || fd3 < 0)
{
    perror("Erro ao abrir ficheiros");
    return (1);
}

char *l1;
char *l2;
char *l3;

while (1)
{
    l1 = get_next_line(fd1);
    l2 = get_next_line(fd2);
    l3 = get_next_line(fd3);

    if (!l1 && !l2 && !l3)
        break;

    if (l1)
    {
        printf("[FILE 1] %s", l1);
        free(l1);
    }
    if (l2)
    {
        printf("[FILE 2] %s", l2);
        free(l2);
    }
    if (l3)
    {
        printf("[FILE 3] %s", l3);
        free(l3);
    }

    printf("--------\n");
}

close(fd1);
close(fd2);
close(fd3);

return 0;

}*/
