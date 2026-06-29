# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crodrigo <crodrigo@student.42porto.co>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/09 11:23:19 by crodrigo          #+#    #+#              #
#    Updated: 2026/02/09 11:23:23 by crodrigo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME    = push_swap

SRC     = src/push_swap.c src/check_input.c src/check_input_helper.c src/utils.c src/create_stack.c \
          src/basic_moves.c src/rotate_moves.c src/comp_movs1.c \
          src/comp_movs2.c src/comp_movs3.c

OBJS    = $(SRC:.c=.o)

CC      = cc
CFLAGS  = -Wall -Wextra -Werror -g
RM      = rm -f
INCLUDE = -I include -I libft

LIBFT   = ./libft/libft.a

# ---------------------- RULES ----------------------

all: $(NAME)

$(NAME): $(OBJS) $(LIBFT)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)

$(LIBFT):
	$(MAKE) -C ./libft

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
	$(MAKE) -C ./libft clean
	$(RM) $(OBJS)

fclean: clean
	$(MAKE) -C ./libft fclean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re

