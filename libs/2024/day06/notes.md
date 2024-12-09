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
