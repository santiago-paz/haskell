-- Ejercicio 1

f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (f n)

