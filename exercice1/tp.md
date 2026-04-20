On vous donne : 
- un tableau d'entiers nums
- un entier target

Votre objectif est de trouver deux indices distinct i et j tels que : 
```
nums[i] + nums[j] = target
```

Contraintes : 
- chaque entrée possède exactement une solution
- Une même élément ne peut être utilisé deux fois
- L'ordre des indices dans la réponse n'a pas d'importance
- Le tableau contient au moins 2 éléments

Attendu : 
- proposer une première solution siple 
- Analyse la complexité 
- Proposer une version optimisée si possible

```
# Test 1
2,7,11,15
9

# Test 2
3,2,4
6

# Test 3
3,3
6

# Test 4
-1,-2,-3,-4,-5
-8

# Test 5
1,5,3,8
9

# Test 6
0,4,3,0
0

# Test 7
10,-10,20,5,1
0

# Test 8
1000000,3,5,7,9
1000009

# Test 9
1,2,3,4,5,6,7,8,9
17

# Test 10
-3,4,3,90
0

# Test 11
5,75,25
100

# Test 12
0,1,2,3,4,5
9

# Test 13
8,4,2,7,11,15
9

# Test 14
4,6,2,11,15
10

# Test 15
-10,20,10,30,5
0

# Test 16
1,1,1,2,5,3
5

# Test 17
100,200,300,400,500
900

# Test 18
-5,-4,-3,-2,-1
-3

# Test 19
6,3,8,2,7,12
13

# Test 20
50,25,75,100,-25
50
``` 