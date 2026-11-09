# CMPS 2200 Recitation 08 Answers

**Name:**Zack Mitra

Place all written answers from `recitation-10.md` here for easier grading.



- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?
W(n, m) = O(n) + O(m) = O(n + m)

The work of reachable is O(n + m), where n is the number of nodes and m is the number of edges. Each reachable node is added to the frontier and processed at most once, contributing O(n) work. Since the graph is undirected, each edge is examined at most twice when visiting neighboring nodes, contributing O(m) work. Therefore, the total worst-case work is O(n + m).




- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?

We only need to call reachable once. Since the graph is undirected, if every node is reachable from one starting node, then the graph is connected. We can determine this by comparing the number of reachable nodes to the total number of nodes.


- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?

W(n, m) = O(1) + O(1) + O(n + m) + O(1)

W(n, m) = O(1) + O(n + m)

The work of connected is O(n + m). The function calls reachable only once, which takes O(n + m) work in the worst case. Selecting a starting node and comparing the number of reachable nodes to the total number of nodes both take O(1) work. Therefore, the overall work is O(n + m).

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

W(n) = n * O(n) = O(n^2)

Yes, the work would change from O(n + m) to O(n^2). With an adjacency matrix, finding a node's neighbors requires checking all n entries in its row, even if it has only a few neighbors. Since reachable may visit all n nodes, the total worst case work is O(n * n) = O(n^2).
