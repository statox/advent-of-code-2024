Use fixed length list to keep track of seen direction on each spot

```
Result for day 6/2024 - part 2 - livemode True: 1753
         64425 function calls (64385 primitive calls) in 7.882 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239    6.858    0.001   13.798    0.003 solution.py:38(isLoopingGrid)
        1    0.899    0.899   14.708   14.708 solution.py:77(part2)
     5239    0.112    0.000    6.939    0.001 solution.py:43(<listcomp>)
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
    11847    0.001    0.000    0.001    0.000 point.py:40(isInBound)
     5923    0.001    0.000    0.002    0.000 point.py:9(__add__)
     5923    0.001    0.000    0.003    0.000 {method 'add' of 'set' objects}
    10504    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     5938    0.001    0.000    0.001    0.000 point.py:5(__init__)
     5923    0.001    0.000    0.001    0.000 point.py:37(__hash__)
     5923    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000   14.708   14.708 base.py:17(wrapper)
        1    0.000    0.000    0.000    0.000 solution.py:17(<listcomp>)
      521    0.000    0.000    0.000    0.000 point.py:34(__eq__)
        1    0.000    0.000    0.000    0.000 solution.py:82(<listcomp>)
       33    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1536(find_spec)
        1    0.000    0.000    0.000    0.000 base.py:38(<listcomp>)
```

Replace `Point` class with raw tuple in `isLoopingGrid`

```
Result for day 6/2024 - part 2 - livemode True: 1753
         19505116 function calls (19505076 primitive calls) in 9.665 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239    8.113    0.002   13.654    0.003 solution.py:38(isLoopingGrid)
 18941590    0.729    0.000    0.729    0.000 {method 'append' of 'list' objects}
        1    0.691    0.691   14.356   14.356 solution.py:77(part2)
     5239    0.100    0.000    4.794    0.001 solution.py:43(<listcomp>)
   509589    0.019    0.000    0.019    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
    11847    0.001    0.000    0.001    0.000 point.py:40(isInBound)
     5923    0.001    0.000    0.002    0.000 point.py:9(__add__)
     5923    0.001    0.000    0.003    0.000 {method 'add' of 'set' objects}
     5938    0.001    0.000    0.001    0.000 point.py:5(__init__)
     5923    0.001    0.000    0.001    0.000 point.py:37(__hash__)
        1    0.001    0.001    0.001    0.001 {built-in method builtins.compile}
     5923    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000   14.357   14.357 base.py:17(wrapper)
      521    0.000    0.000    0.000    0.000 point.py:34(__eq__)
        1    0.000    0.000    0.000    0.000 solution.py:82(<listcomp>)
        1    0.000    0.000    0.000    0.000 solution.py:17(<listcomp>)
```

Stop using `Point.isInBound()` and use condition directly in `isLoopingGrid`

```
Result for day 6/2024 - part 2 - livemode True: 1753
         57398698 function calls (57398658 primitive calls) in 17.346 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239    9.697    0.002   21.359    0.004 solution.py:38(isLoopingGrid)
 18947493    3.831    0.000    5.941    0.000 point.py:9(__add__)
 18952747    2.111    0.000    2.111    0.000 point.py:5(__init__)
 18941590    0.864    0.000    0.864    0.000 {method 'append' of 'list' objects}
        1    0.696    0.696   22.067   22.067 solution.py:74(part2)
     5239    0.109    0.000    4.831    0.001 solution.py:43(<listcomp>)
   509589    0.025    0.000    0.025    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
    17086    0.004    0.000    0.004    0.000 point.py:40(isInBound)
     5923    0.001    0.000    0.003    0.000 {method 'add' of 'set' objects}
     5923    0.001    0.000    0.001    0.000 point.py:37(__hash__)
     5923    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000   22.067   22.067 base.py:17(wrapper)
        1    0.000    0.000    0.000    0.000 solution.py:17(<listcomp>)
      521    0.000    0.000    0.000    0.000 point.py:34(__eq__)
        1    0.000    0.000    0.000    0.000 solution.py:79(<listcomp>)
       33    0.000    0.000    0.000    0.000 {built-in method posix.stat}
```

Replace set with a 2d list in `isLoopingGrid`

```
Result for day 6/2024 - part 2 - livemode True: 1753
         76340268 function calls (76340228 primitive calls) in 20.346 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239   10.214    0.002   24.392    0.005 solution.py:38(isLoopingGrid)
 18947493    3.951    0.000    6.083    0.000 point.py:9(__add__)
 18958656    2.311    0.000    2.311    0.000 point.py:40(isInBound)
 18952747    2.133    0.000    2.133    0.000 point.py:5(__init__)
 18941590    0.893    0.000    0.893    0.000 {method 'append' of 'list' objects}
        1    0.699    0.699   25.103   25.103 solution.py:72(part2)
     5239    0.108    0.000    4.867    0.001 solution.py:43(<listcomp>)
   509589    0.027    0.000    0.027    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
     5923    0.001    0.000    0.003    0.000 {method 'add' of 'set' objects}
     5923    0.001    0.000    0.001    0.000 point.py:37(__hash__)
     5923    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000   25.103   25.103 base.py:17(wrapper)
        1    0.000    0.000    0.000    0.000 solution.py:17(<listcomp>)
      521    0.000    0.000    0.000    0.000 point.py:34(__eq__)
        1    0.000    0.000    0.000    0.000 solution.py:77(<listcomp>)
       33    0.000    0.000    0.000    0.000 {built-in method posix.stat}
```

Avoid calling twice `Point.isInBound` in `isLoopingGrid`

```
Result for day 6/2024 - part 2 - livemode True: 1753
         152102584 function calls (152102544 primitive calls) in 36.866 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239   13.835    0.003   35.661    0.007 solution.py:38(isLoopingGrid)
 37889063    6.136    0.000    8.505    0.000 point.py:37(__hash__)
 18947493    4.561    0.000    7.556    0.000 point.py:9(__add__)
 18947493    3.050    0.000    7.126    0.000 {method 'add' of 'set' objects}
 18952747    2.996    0.000    2.996    0.000 point.py:5(__init__)
 18956903    2.681    0.000    2.681    0.000 point.py:40(isInBound)
 37889063    2.370    0.000    2.370    0.000 {built-in method builtins.hash}
        1    1.191    1.191   36.864   36.864 solution.py:70(part2)
   509589    0.039    0.000    0.039    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
     3513    0.001    0.000    0.001    0.000 point.py:34(__eq__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
        1    0.000    0.000   36.864   36.864 base.py:17(wrapper)
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000    0.000    0.000 {built-in method posix.replace}
        1    0.000    0.000    0.000    0.000 solution.py:75(<listcomp>)
        1    0.000    0.000    0.000    0.000 solution.py:17(<listcomp>)
       35    0.000    0.000    0.000    0.000 {built-in method posix.stat}
```

Change `Point.__hash__()` from `return hash(f"{self.x};{self.y}")` to `return hash((self.x, self.y))`

```
Result for day 6/2024 - part 2 - livemode True: 1753
         171042365 function calls (171042325 primitive calls) in 39.522 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239   15.591    0.003   38.383    0.007 solution.py:38(isLoopingGrid)
 37889063    5.371    0.000    7.775    0.000 point.py:43(__hash__)
 37896720    4.687    0.000    4.687    0.000 point.py:49(isInBound)
 18947493    4.258    0.000    7.251    0.000 point.py:9(__add__)
 18947493    3.044    0.000    6.765    0.000 {method 'add' of 'set' objects}
 18952747    2.994    0.000    2.994    0.000 point.py:5(__init__)
 37889063    2.404    0.000    2.404    0.000 {built-in method builtins.hash}
        1    1.127    1.127   39.521   39.521 solution.py:67(part2)
   509589    0.039    0.000    0.039    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
     3513    0.001    0.000    0.001    0.000 point.py:34(__eq__)
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000   39.521   39.521 base.py:17(wrapper)
        1    0.000    0.000    0.000    0.000 solution.py:17(<listcomp>)
        1    0.000    0.000    0.000    0.000 solution.py:72(<listcomp>)
       33    0.000    0.000    0.000    0.000 {built-in method posix.stat}
```

Initial solution profiling

```
Result for day 6/2024 - part 2 - livemode True: 1753
         171042401 function calls (171042360 primitive calls) in 45.255 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5239   16.157    0.003   44.046    0.008 solution.py:38(isLoopingGrid)
 37889063    8.711    0.000   11.344    0.000 point.py:37(__hash__)
 37896720    5.146    0.000    5.146    0.000 point.py:41(isInBound)
 18947493    5.021    0.000    8.262    0.000 point.py:9(__add__)
 18952747    3.241    0.000    3.241    0.000 point.py:5(__init__)
 18947493    3.104    0.000    8.794    0.000 {method 'add' of 'set' objects}
 37889063    2.633    0.000    2.633    0.000 {built-in method builtins.hash}
        1    1.196    1.196   45.253   45.253 solution.py:67(part2)
   509589    0.039    0.000    0.039    0.000 {built-in method builtins.len}
        1    0.004    0.004    0.011    0.011 solution.py:16(getOriginalPath)
     3513    0.001    0.000    0.001    0.000 point.py:34(__eq__)
        1    0.000    0.000   45.253   45.253 base.py:17(wrapper)
        2    0.000    0.000    0.000    0.000 solution.py:7(getInitialPosition)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
        1    0.000    0.000    0.000    0.000 solution.py:72(<listcomp>)
       35    0.000    0.000    0.000    0.000 {built-in method posix.stat}
```

```

```

```

```

```

```

```

```

```
