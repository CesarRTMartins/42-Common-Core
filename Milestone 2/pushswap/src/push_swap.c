/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: crodrigo <crodrigo@student.42porto.co>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 11:22:57 by crodrigo          #+#    #+#             */
/*   Updated: 2026/02/16 13:13:57 by crodrigo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	is_sorted(t_stack *st)
{
	t_stack	*s;

	s = st;
	while (s->next)
	{
		if (s->n > s->next->n)
			return (0);
		s = s->next;
	}
	return (1);
}

static void	push_swap(t_stack **sa, t_stack **sb, int size)
{
	if (size == 2 && !is_sorted(*sa))
		swap_move(sa, NULL, "sa");
	else if (size == 3)
		small_sort(sa);
	else if (size > 3 && !is_sorted(*sa))
		big_sort(sa, sb);
}

int	main(int ac, char **av)
{
	t_stack	*sa;
	t_stack	*sb;
	char	**nums;
	char	*joined;
	int		size;

	if (ac < 2)
		return (0);
	joined = join_args(ac, av);
	if (!joined)
		print_error_and_exit(NULL, NULL);
	nums = ft_split(joined, ' ');
	free(joined);
	if (!nums || !nums[0] || !is_correct_input(nums))
		print_error_and_exit(NULL, nums);
	sa = create_stack_from_split(nums);
	free_split(nums);
	sb = NULL;
	size = get_stack_size(sa);
	get_main_index(sa, size);
	push_swap(&sa, &sb, size);
	free_stack(&sa);
	free_stack(&sb);
	return (0);
}
