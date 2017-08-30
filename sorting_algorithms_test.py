import sorting_algorithms as sa

mass_len = 1000

mass = sa.generate_random_int_mass(mass_len)
print (mass)

sa.apply_sort(sa.bubble_sort, mass)
sa.apply_sort(sa.shake_sort, mass)
sa.apply_sort(sa.selective_sort, mass)
sa.apply_sort(sa.quick_sort, mass)
sa.apply_sort(sa.insert_sort, mass)
sa.apply_sort(sa.shell_sort, mass)
sa.apply_sort(sa.merge_sort, mass)


