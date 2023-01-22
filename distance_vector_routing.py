from copy import deepcopy      #importing this library to copy lists
import time                    #importing this library to calculate total time

lines = []
routes = open("routes.txt", "r+") #reading from a text file which has informations on nodes and links
for line in routes:
    line = line.rstrip()          #stripping the whitespaces and newlines before and after each lines
    line = line.split(" ")        #splitting each lines into lists based on whitespaces in between the elements
    lines.append(line)            #appending the read texts into a list
    
#Finding out the number of nodes from the list of nodes and links provided that the nodes are named in a serial order
nodes = 0
for line in lines:
    for i in range(2):
        if int(line[i]) > nodes:
            nodes = int(line[i])


routing_all = []
for i in range(1, nodes+1):                  #looping through all the nodes
    total_routes = []
    for line in lines:                       #looping through the list in "lines"
        if i == int(line[0]):                #checking if node matches with the first element in the list
            temp_list = []
            temp_list.append(int(line[1]))   #appending second element into a temporary list as the destination node
            temp_list.append(int(line[1]))   #appending second element into a temporary list as the next node
            temp_list.append(int(line[2]))   #appending third element into a temporary list as the link cost
            total_routes.append(temp_list)   #appending the temporary list into another temporary list
            
        if i == int(line[1]):                #checking if node matches with the second element in the list
            temp_list = []
            temp_list.append(int(line[0]))   #appending first element into a temporary list as the destination node
            temp_list.append(int(line[0]))   #appending first element into a temporary list as the next node
            temp_list.append(int(line[2]))   #appending third element into a temporary list as the link cost
            total_routes.append(temp_list)   #appending the temporary list into another temporary list
            
    routing_all.append(total_routes)         #appending the second temporary list into the "routing_all" list which contains destination nodes, next nodes and link costs of each nodes in ascending order  

#Printing the initial routing tables of the nodes in a serial fashion (from 1 to 6 in this case)

for i in range(nodes):
    print("Initial routing table of node", i+1, "=", routing_all[i])
    print("\n")

connected = []
for i in range(nodes):         #looping for number of nodes times
    conn = []
    count = len(routing_all[i])
    for j in range(count):          #looping for count (length of each element in the "routing_all" list) times
        node = routing_all[i][j][0]
        conn.append(node)
    connected.append(conn)         #appending the connected nodes into the list such as nodes 2, 3, 4 and 5 are connected to node 1; nodes 1, 4 and 5 are connected to 2 and so on 

def update_routes():
    for i in range(nodes):               #looping for number of nodes times
        for n in connected[i]:           #looping through the "connected" list which describes the connection of the nodes
            to_update = routing_all[n-1]           #getting the routing table of the connected nodes
            
            for j in range(len(to_update)):        #looping through the elements of the routing table
                if to_update[j][0] == i+1:         #comparing the elements in the routing table with the current nodes
                    basic_dist = to_update[j][2]   #if above condition satisfies, assigning the distance between the nodes as "basic_nodes"
                    break
                    
            for j in range(len(to_update)):        #Again looping through the elements of the routing table
                if to_update[j][0] != i+1:         #checking if the elements in the routing table do not match with the current node
                    temp_dist = basic_dist + to_update[j][2]   #if it is not current node, calculate the distance to the other nodes through the connected nodes
                    
                    for k in range(len(routing_all[i])):              #looping for length of routing table of the current node
                        if to_update[j][0] == routing_all[i][k][0]:   #checking if the node in routing table of the connected node lies in the routing table of the current node
                            if temp_dist < routing_all[i][k][2]:      #if above condition satisfies, check if the new distance is less than the old distance
                                routing_all[i][k][2] = temp_dist      #if the new distance is less, update the distance
                                routing_all[i][k][1] = n              #update the next node
                                break
                                
                    end_count = len(routing_all[i])                   #length of routing table of the current node             
                    for k in range(len(routing_all[i])):              #This loop could have been placed in the above loop (didn't take risk to further complicate things)
                        if to_update[j][0] == routing_all[i][k][0]:   #checking if the node in routing table of the connected node lies in the routing table of the current node
                            break                                     #if so, it is already updated, so breaking the loop
                        if k == end_count - 1:                        #if the loop didn't break and reached to the end of routing table
                            nothing = []                              
                            nothing.append(to_update[j][0])           #appending the new node to the temporary list
                            nothing.append(n)                         #appending the current connected node as the next node
                            nothing.append(temp_dist)                 #appending the link cost
                            routing_all[i].append(nothing)            #appending the temporary list into the routing table of the current node
                            break
                            
        print(routing_all)                                            #printing the whole routing table
        print("\n")

iteration = 1
start = time.time()                            #start_time
while True:
    print("Iteration", iteration)
    routing_prev = deepcopy(routing_all)       #copying the "routing_all" list to "routing_prev" for later comparision
    update_routes()                            #calling update_routes function to update the routes
    if routing_prev == routing_all:            #checking if the routing tables have changed
        print("Well, Yeah!")
        end = time.time()                      #end_time  
        print("Total time =", end - start)
        break                                  #breaking the loop if there is no change in the routes of the routing tables
    else:
        print("let's try this again!")
        iteration += 1