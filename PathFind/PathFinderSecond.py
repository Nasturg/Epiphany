from heapq import *
import sys


# import json

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
num = int(sys.argv[3])

if num == 1:
    graph = {'A': [(34, 'B')],
             'B': [(34, 'A'), (82, 'C')],
             'C': [(82, 'B'), (35, 'D'), (42, 'E'), (36, 'F'), (63, 'G'), (88, 'M'), (186, 'N'), (289, 'O')],
             'D': [(35, 'C'), (43, 'E'), (53, 'F'), (55, 'G'), (120, 'M'), (218, 'N'), (321, 'O')],
             'E': [(42, 'C'), (43, 'D'), (74, 'F'), (108, 'M')],
             'F': [(36, 'C'), (53, 'D'), (74, 'E'), (94, 'G'), (88, 'M')],
             'G': [(63, 'C'), (55, 'D'), (94, 'F')],
             'H': [(51, 'N')],
             'I': [(51, 'O')],
             'J': [(75, 'M')],
             'K': [(75, 'N')],
             'L': [(75, 'O')],
             'M': [(88, 'C'), (120, 'D'), (108, 'E'), (88, 'F'), (75, 'J'), (101, 'N'), (204, 'O')],
             'N': [(186, 'C'), (218, 'D'), (51, 'H'), (75, 'K'), (101, 'M'), (106, 'O')],
             'O': [(289, 'C'), (321, 'D'), (51, 'I'), (75, 'L'), (204, 'M'), (106, 'N')]}
elif num == 2:
    graph = {'A': [(2, 'M'), (3, 'P')],
             'M': [(2, 'A'), (2, 'N')],
             'N': [(2, 'M'), (2, 'B')],
             'P': [(3, 'A'), (4, 'B')],
             'B': [(4, 'P'), (2, 'N')]}

visited = dijkstra(start, goal, graph)


cur_node = goal
# print(f'\npath from {goal} to {start}: \n {goal} ', end='')

print('{s}'.format(s=goal))
while cur_node != start:
    cur_node = visited[cur_node]
    print('{cur_node}'.format(cur_node=cur_node))
