import sys
import resource
import time

# Get CLI arguments
algorithm = sys.argv[1]
order_of_fields = sys.argv[2]

path_to_goal = ""
cost_of_path = ""
nodes_expanded = ""
search_depth = ""
max_search_depth = ""
running_time = ""

def bfs(initialState, goalTest):

    frontier = Queue.new(initialState)
    explored = Set.new()

    while not frontier.isEmpty():
            state = frontier.dequeue()
            explored.add(state)

            if goalTest(state)
                return SUCCESS(sate)

            for neighbor in state.neighbors():
                if neighbor not in frontier and explored:
                        frontier.enqueue(state)


def search(algorithm, order_of_fields ):
    if algorithm == "bfs":
        bfs(order_of_fields)



# Run search and take time
start_time = time.time()
search(algorithm, order_of_fields )
end_time = time.time()
running_time = end_time - start_time

# max_ram_usage
max_ram_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024

# Write file
#
# path_to_goal: ['Up', 'Left', 'Left']
# cost_of_path: 3
# nodes_expanded: 181437
# search_depth: 3
# max_search_depth: 66125
# running_time: 5.01608433
# max_ram_usage: 4.23940217

f = open("output.txt", "w")
f.write("path_to_goal: " + path_to_goal + "\n")
f.write("cost_of_path: " + cost_of_path + "\n")
f.write("nodes_expanded: " + nodes_expanded + "\n")
f.write("search_depth: " + search_depth + "\n")
f.write("max_search_depth: " + max_search_depth + "\n")
f.write("running_time: " + str(running_time) + "\n")
f.write("max_ram_usage: " + str(max_ram_usage) + "\n")
f.close()
