> Реализуйте mapper для задачи Cross-Correlation, который для каждого объекта из кортежа
> создает stripe.
>
> Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
>
> Mapper пишет данные в виде key / value, где key - объект, value - соответствующий stripe > (пример: a:1,b:2,c:3)

# Sample Input:

a b
a b a c

# Sample Output:

a	b:1
b	a:1
a	b:1,c:1
b	a:2,c:1
a	b:1,c:1
c	b:1,a:2
