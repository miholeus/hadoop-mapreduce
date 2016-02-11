# coding: utf-8

"""
Реализуйте mapper в задаче поиска кратчайшего пути с помощью Hadoop Streaming.

Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:

Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
Список исходящих вершин (через "," в фигурных скобках)

Пример работы mapper на второй итерации обработки следующего графа:

Sample Input:
1	0	{2,3,4}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	INF	{9,10}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}
Sample Output:
1	0	{2,3,4}
2	1	{}
3	1	{}
4	1	{}
2	1	{5,6}
5	2	{}
6	2	{}
3	1	{}
4	1	{7,8}
7	2	{}
8	2	{}
5	INF	{9,10}
9	INF	{}
10	INF	{}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}
"""

import sys

for line in sys.stdin:
    node,weight,children = line.strip().split("\t")
    adj_list = children[1:-1].strip().split(",")
    print(node + "\t" + weight + "\t" + children)
    if adj_list:
        for child_node in adj_list:
            if child_node:
                weight_child = weight if weight == 'INF' else str(int(weight)+1)
                print(child_node + "\t" + weight_child + "\t" + "{}")
