# **Augmenting Path Matching -- Python Learning Project**

This project is a simple, educational implementation of the
**augmenting-path algorithm** for bipartite matching.\
The goal is to understand how matchings, BFS exploration, and
alternating paths work under the hood.

------------------------------------------------------------------------

## **What the Code Does**

-   Builds a bipartite graph with two groups: **X** (top) and **Y**
    (bottom)\
-   Sets up an initial *partial matching*\
-   Adds all remaining edges\
-   Runs a BFS-style search to find an **augmenting path**, using:
    -   alternating matched/unmatched edges\
    -   predecessor pointers\
    -   visited flags\
    -   a processing queue\
-   When an unmatched vertex is reached on the opposite side, the code
    reconstructs and prints the **augmenting path**

------------------------------------------------------------------------

## **Why This Exists**

This is a hands-on, write-it-from-scratch project meant to teach:

-   representing bipartite graphs\
-   tracking matchings\
-   exploring alternating paths\
-   detecting augmenting paths via BFS

------------------------------------------------------------------------

## **How to Run**

``` bash
python3 main.py
```

You'll see queue updates and, if one exists, the printed augmenting
path.

------------------------------------------------------------------------

## **Future Extensions**

-   Repeat BFS to compute **maximum matching**\
-   Add graph visualization\
-   Implement **Hopcroft--Karp** for efficiency
