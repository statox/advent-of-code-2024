A story of perf improvements:

(Yes I should have notes to which changes it corresponds but still the improvements are nice)

```
Result for day 9/2024 - part 2 - livemode True: 6511178035564
         1388 function calls (1361 primitive calls) in 4.676 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      367    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
       58    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       49    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       35    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       34    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       31    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       28    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       28    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:128(<listcomp>)
       28    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:126(_path_join)
       23    0.000    0.000    0.000    0.000 {built-in method posix.stat}
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:140(_path_stat)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:244(_verbose_message)
       21    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1226(_find_parent_path_names)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1236(_get_parent_path)
       20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     19/7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1240(_recalculate)



Result for day 9/2024 - part 2 - livemode True: 6511178035564
         29255 function calls (29228 primitive calls) in 4.236 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    19010    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     8878    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
      367    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
       58    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       49    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       35    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       34    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       31    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       28    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       28    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:128(<listcomp>)
       28    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:126(_path_join)
       23    0.000    0.000    0.000    0.000 {built-in method posix.stat}


Result for day 9/2024 - part 2 - livemode True: 6511178035564
         34128 function calls (34101 primitive calls) in 9.405 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    9.399    9.399    9.401    9.401 solution.py:47(part2)
        1    0.001    0.001    0.001    0.001 solution.py:6(<listcomp>)
      367    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     8879    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
    19010    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
        1    0.000    0.000    0.000    0.000 {method 'write' of '_io.FileIO' objects}
     4893    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    9.402    9.402 base.py:17(wrapper)
        1    0.000    0.000    0.001    0.001 solution.py:5(parseInput)



Result for day 9/2024 - part 2 - livemode True: 6511178035564
         54128 function calls (54101 primitive calls) in 10.126 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   10.118   10.118   10.123   10.123 solution.py:47(part2)
        1    0.001    0.001    0.001    0.001 solution.py:6(<listcomp>)
    10000    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}
      367    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
    14893    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     8879    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
    19010    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}



Result for day 9/2024 - part 2 - livemode True: 6511178035564
         63872 function calls (63845 primitive calls) in 10.169 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   10.144   10.144   10.166   10.166 solution.py:47(part2)
     5239    0.011    0.000    0.011    0.000 {method 'insert' of 'list' objects}
    13751    0.009    0.000    0.009    0.000 {method 'pop' of 'list' objects}
        1    0.001    0.001    0.001    0.001 solution.py:6(<listcomp>)
    10000    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}
    14893    0.001    0.000    0.001    0.000 {built-in method builtins.len}
    19010    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}





Result for day 9/2024 - part 2 - livemode True: 6511178035564
         71261959 function calls (71261932 primitive calls) in 16.444 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   14.040   14.040   16.442   16.442 solution.py:47(part2)
 71213016    2.381    0.000    2.381    0.000 {built-in method builtins.len}
     5239    0.011    0.000    0.011    0.000 {method 'insert' of 'list' objects}
    13751    0.008    0.000    0.008    0.000 {method 'pop' of 'list' objects}
```

```

```

```

```

```
