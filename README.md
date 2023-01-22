# distance-vector-routing
Simulation of Distance Vector Routing algorithm using python

This is based on the assumption that one knows the algorithm of Distance Vector Routing. To know about the algorithm, refer to this [link](https://www.youtube.com/watch?v=dmS1t2twFrI&t).

**Before running this program in terminal, make sure to place the input file containing routes in the same directory as this python (.py) file**


1. First we have a input file "routes.txt" which contains the informations on nodes and links of a network. The content in the file is shown below:<br>
	1 2 2<br>
	1 3 6<br>
	1 4 7<br>
	1 5 2<br>
	2 4 10<br>
	2 5 2<br>
	3 5 2<br>
	4 6 3<br>
	5 6 1<br>
 
   The first two numbers denote the nodes and the third or last number denotes the cost of the link.

2. Read the input file and prepare the list with the contents of the file.

3. Find out the number of the nodes from the list prepared from the input file.

4. From the list, prepare the routing table of all the nodes in the network. Here, "routing_all" has the routing table of all the nodes.

5. Prepare the list of the nodes which are connected to the current nodes such as 

	[[2, 3, 4, 5], [1, 4, 5], [1, 5], [1, 2, 6], [1, 2, 3, 6], [4, 5]]
	
	In the above list, nodes 2, 3, 4 and 5 are connected to the first node i.e. node 1; nodes 1, 4 and 5 are connected to the second node and so on.

6. Update the routes of the current nodes looping through the connected nodes. If there is new node in the connected nodes and the routing table of the current node has no information about that new node, then append the node into the routing table of the current node.

7. Check if the routing tables of the nodes changed or not. If changed, run again a new iteration. If it did not change, stop the iteration as it has reached the stable state.

8. Display the time taken to reach the stable state.