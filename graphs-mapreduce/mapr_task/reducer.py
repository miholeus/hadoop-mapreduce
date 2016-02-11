# coding: utf-8

"""
Реализуйте reducer в задаче поиска кратчайшего пути с помощью Hadoop Streaming.

Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:

Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
Список исходящих вершин (через "," в фигурных скобках).
Пример работы reducer на второй итерации обработки следующего графа:

Sample Input:
1	0	{2,3,4}
10	INF	{}
10	INF	{}
2	1	{}
2	1	{5,6}
3	1	{}
3	1	{}
4	1	{}
4	1	{7,8}
5	2	{}
5	INF	{9,10}
6	2	{}
6	INF	{}
7	2	{}
7	INF	{}
8	2	{}
8	INF	{}
9	INF	{}
9	INF	{}
Sample Output:
1	0	{2,3,4}
10	INF	{}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	2	{9,10}
6	2	{}
7	2	{}
8	2	{}
9	INF	{}
"""

import sys

lastNode = None
storage = dict()

for line in sys.stdin:
    node,weight,children = line.strip().split("\t")
    cur_children = children[1:-1].split(',') if children != '{}' else []
    if lastNode and lastNode != node:
        print(storage['node'] + "\t" + storage['weight'] + '\t{%s}' % (','.join(storage['children'])))
        storage['node'] = node
        storage['weight'] = weight
        storage['children'] = cur_children
    else:
        storage['node'] = node
        if 'weight' in storage and storage['weight'] != 'INF':
            storage['weight'] = min(storage['weight'], weight)
        else:
            storage['weight'] = weight

        if 'children' in storage and storage['children']:
            if cur_children:
                storage['children'] = storage['children'] + cur_children
        else:
            storage['children'] = cur_children
    lastNode = node

if lastNode:
    print(storage['node'] + "\t" + storage['weight'] + '\t{%s}' % (','.join(storage['children'])))
