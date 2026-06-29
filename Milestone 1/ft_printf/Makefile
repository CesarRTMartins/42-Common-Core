# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crodrigo <crodrigo@student.42porto.co      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/06 14:24:00 by crodrigo          #+#    #+#              #
#    Updated: 2025/11/06 14:24:35 by crodrigo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

RM = rm -f

CC = clang

CFLAGS = -Wall -Werror -Wextra

SRC = ft_printf.c ft_put_c.c ft_put_d.c ft_put_p.c ft_put_s.c \
ft_put_u.c  ft_put_x.c

SRC-OBJ = $(SRC:.c=.o)

%.o:		%.c
			$(CC) -c $(CFLAGS) $^

all:		$(NAME)
		
$(NAME):	$(SRC-OBJ)	
			ar rcs $(NAME) $(SRC-OBJ) 

clean:
			$(RM) $(SRC-OBJ)

fclean:		clean
			$(RM) $(NAME)

re:			fclean $(NAME)
