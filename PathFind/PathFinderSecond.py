from heapq import *
import sys
import json


def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited


# start = 'A'
start = str(sys.argv[1])
# goal = 'B'
goal = str(sys.argv[2])
graph = json.loads(sys.argv[3])


'''
if num == 1:
    graph = {'A': [(2, 'M'), (3, 'P')],
             'M': [(2, 'A'), (2, 'N')],
             'N': [(2, 'M'), (2, 'B')],
             'P': [(3, 'A'), (4, 'B')],
             'B': [(4, 'P'), (2, 'N')]}
elif num == 2:
    graph = {'A': [(2, 'M'), (3, 'P')],
             'M': [(2, 'A'), (2, 'N')],
             'N': [(2, 'M'), (2, 'B')],
             'P': [(3, 'A'), (4, 'B')],
             'B': [(4, 'P'), (2, 'N')]}
'''

visited = dijkstra(start, goal, graph)

cur_node = goal
# print(f'\npath from {goal} to {start}: \n {goal} ', end='')
print('{s}'.format(s=goal))
while cur_node != start:
    cur_node = visited[cur_node]
    print('{cur_node}'.format(cur_node=cur_node))
