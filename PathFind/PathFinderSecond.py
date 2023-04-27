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


# start = str(input('START: '))
start = str(sys.argv[1])
# goal = str(input('END: '))
goal = str(sys.argv[2])
num = int(sys.argv[3])
# num = 4
# graph = json.dumps(sys.argv[3])

# '''

#  Field 0
if num == 0:
    graph = {
        'A': [(34, 'B')],
        'B': [(34, 'A'), (82, 'C')],
        'C': [(82, 'B'), (34, 'D'), (41, 'E'), (60, 'F'), (92, 'G'), (89, 'M'), (186, 'N'), (290, 'O')],
        'D': [(34, 'C'), (43, 'E'), (90, 'F'), (118, 'G'), (120, 'M'), (217, 'N'), (321, 'O')], 
        'E': [(41, 'C'), (43, 'D'), (74, 'F'), (108, 'M')],
        'F': [(60, 'C'), (90, 'D'), (74, 'E'), (43, 'G'), (38, 'M')],
        'G': [(92, 'C'), (118, 'D'), (43, 'F')],
        'H': [(51, 'N')],
        'I': [(51, 'O')],
        'J': [(75, 'M')],
        'K': [(75, 'N')],
        'L': [(75, 'O')],
        'M': [(89, 'C'), (120, 'D'), (108, 'E'), (38, 'F'), (75, 'J'), (100, 'N'), (204, 'O')],
        'N': [(186, 'C'), (217, 'D'), (51, 'H'), (75, 'K'), (100, 'M'), (107, 'O')],
        'O': [(290, 'C'), (321, 'D'), (51, 'I'), (75, 'L'), (204, 'M'), (107, 'N')]
    }
    #  Field 1
elif num == 1:

    graph = {
        'A': [(123, 'B'), (23, 'D')],
        'B': [(123, 'A'), (76, 'C'), (103, 'D'), (147, 'E')],
        'C': [(76, 'B'), (75, 'E'), (62, 'L')],
        'D': [(23, 'A'), (103, 'B')],
        'E': [(147, 'B'), (75, 'C'), (132, 'F')],
        'F': [(132, 'E'), (170, 'G')],
        'G': [(170, 'F'), (61, 'H'), (129, 'I')],
        'H': [(61, 'G'), (71, 'I'), (84, 'J')],
        'I': [(71, 'H'), (129, 'G'), (84, 'K')],
        'J': [(84, 'H')],
        'K': [(84, 'I')],
        'L': [(62, 'C')]
    }

    #  Field 2
elif num == 2:
    graph = {
        'A': [(123, 'B'), (23, 'D')],
        'B': [(123, 'A'), (76, 'C'), (103, 'D'), (313, 'J')],
        'C': [(76, 'B'), (241, 'J'), (62, 'L')],
        'D': [(23, 'A'), (103, 'B')],
        'E': [(78, 'F'), (68, 'K')],
        'F': [(78, 'E')],
        'G': [(68, 'H'), (82, 'I')],
        'H': [(68, 'G'), (89, 'K')],
        'I': [(82, 'G'), (127, 'J')],
        'J': [(313, 'B'), (241, 'C'), (127, 'I')],
        'K': [(68, 'E'), (89, 'H')],
        'L': [(62, 'C')]
    }

elif num == 3:
    #  Field 3

    graph = {
        'A': [(123, 'B'), (23, 'D')],
        'B': [(123, 'A'), (76, 'C'), (103, 'D'), (147, 'E'), (321, 'I')],
        'C': [(76, 'B'), (75, 'E'), (249, 'I'), (62, 'M')],
        'D': [(23, 'A'), (103, 'B')],
        'E': [(147, 'B'), (75, 'C'), (132, 'H'), (177, 'I')],
        'F': [(166, 'G'), (70, 'H')],
        'G': [(166, 'F'), (99, 'H')],
        'H': [(132, 'E'), (70, 'F'), (99, 'G')],
        'I': [(321, 'B'), (249, 'C'), (177, 'E'), (132, 'J'), (70, 'L')],
        'J': [(132, 'I'), (65, 'L')],
        'K': [(79, 'L')],
        'L': [(70, 'I'), (65, 'J'), (79, 'K')],
        'M': [(62, 'C')]
    }

elif num == 4:
    #  Field 4

    graph = {
        'A': [(40, 'P')],
        'B': [(40, 'P'), (75, 'C'), (83, 'D'), (147, 'E'), (229, 'L')],
        'C': [(75, 'B'), (75, 'E'), (157, 'L'), (62, 'O')],
        'D': [(83, 'B'), (11, 'C'), (67, 'E'), (149, 'L')],
        'E': [(147, 'B'), (75, 'C'), (133, 'I'), (85, 'L'), (67, 'D')],
        'F': [(226, 'H'), (60, 'I')],
        'G': [(24, 'H')],
        'H': [(226, 'F'), (24, 'G'), (169, 'I')],
        'I': [(133, 'E'), (60, 'F'), (169, 'H')],
        'J': [(60, 'L'), (35, 'N')],
        'K': [(31, 'M')],
        'L': [(229, 'B'), (157, 'C'), (85, 'E'), (46, 'N'), (149, 'D'), (60, 'J')],
        'M': [(31, 'K'), (63, 'N')],
        'N': [(35, 'J'), (46, 'L'), (63, 'M')],
        'O': [(62, 'C')],
        'P': [(132, 'B'), (40, 'A')]
    }
# '''

visited = dijkstra(start, goal, graph)

cur_node = goal
# print(f'\npath from {goal} to {start}: \n {goal} ', end='')

print('{s}'.format(s=goal))
while cur_node != start:
    cur_node = visited[cur_node]
    print('{cur_node}'.format(cur_node=cur_node))
