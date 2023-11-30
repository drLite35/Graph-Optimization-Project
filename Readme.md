# An Application of Graph Optimization


## Contributors
- [Anurag Singh 2021B5A72874]
- [Vandit Kharod 2022A7PS0564G]
- [Mitta Manish Gupta 2022A7PS0292G]


## Problem Statement

The research problem focuses on optimizing the University Course Assignment System, where faculty members are categorized into three groups: "x1," "x2," and "x3," each with different course load capacities. The challenge involves developing an assignment scheme that maximizes the number of courses assigned to faculty while considering their preferences and category-based constraints. Faculty members can take multiple courses in a semester, and a course can be assigned to multiple professors, with each assignment contributing to their course load. The unique aspect of this problem lies in the flexibility of course assignments, deviating from traditional Assignment problems, and the need to align with individual preferences within category constraints.


## Problem Constraints

1. **Faculty Categories:** The faculty members are divided into three categories: "x1," "x2," and "x3," each with distinct course loads. "x1" handles 0.5 courses, "x2" manages 1 course, and "x3" takes on 1.5 courses per semester.

2. **Course Load Flexibility:** Faculty members can handle multiple courses in a semester, and a single course can be assigned to multiple professors..

3. **Preference Lists:** Each faculty member maintains a preference list of at least 12 courses, ordered by personal preference.

4. **Full Assignment Requirement:** Faculty members must be fully assigned or not assigned at all to courses.

5. **Total Faculty Constraint:** The total number of faculty members across all categories ("x1," "x2," "x3") must be less than 30.


## Table of Contents

1. [Bipartite Graphs]
2. [Maximum Bipartite Matching]
3. [Graph Optimization]
4. [NetworkX Library]



## Bipartite Graphs

A bipartite graph is a type of graph where the set of vertices can be partitioned into two disjoint sets, and all edges connect vertices from different sets. In the context of university course assignment, the faculty members and the courses form the two sets, and edges represent preferences or possible assignments.

### Code Snippet

```python
# Function to create the bipartite graph
def create_bipartite_graph(faculty_categories, course_loads, preferences, all_courses):
    G = nx.Graph()

    # Add faculty nodes
    G.add_nodes_from(faculty_categories, bipartite=0)

    # Add course nodes
    G.add_nodes_from(all_courses, bipartite=1)

    # Add edges based on preferences
    for faculty, pref_list in preferences.items():
        for course in pref_list:
            G.add_edge(faculty, course)

    # Ensure that each faculty member is fully assigned or not assigned at all
    for faculty in faculty_categories:
        G.add_edge(faculty, f"Unassigned_{faculty}", weight=0)

    return G 
```


## Maximum Bipartite Matching 

## Code Snippet

```python
# Function to perform maximum bipartite matching and calculate total load
def perform_matching(G, faculty_categories, course_loads):
    all_matchings = list(nx.bipartite.maximum_matching(G))

    if not all_matchings:
        print("No valid assignment found.")
    else:
        # Code for processing and displaying matchings
        # ...

        # Code for calculating and displaying total course load
        # ...
```
 ## Graph Optimization

Graph optimization involves finding the best solution from all feasible solutions in a graph. In the university course assignment system, optimization aims to maximize the number of courses assigned to faculty members while adhering to constraints.

```python
# Main function to orchestrate the entire process
def optimize_course_assignment():
    try:
        # Code for user input and initialization
        # ...

        # Code for creating bipartite graph
        G = create_bipartite_graph(faculty_categories, course_loads, preferences, all_courses)

        # Code for drawing the bipartite graph
        # ...

        # Code for performing maximum bipartite matching
        perform_matching(G, faculty_categories, course_loads)

    except ValueError as e:
        print(f"Error: {e}")
```


## Code Overview

The provided Python code uses the NetworkX library for graph representation and bipartite matching. The program takes user input for faculty preferences, creates a bipartite graph, performs maximum bipartite matching, and calculates the total course load assigned to each faculty member. The results are displayed in the form of matchings and a course assignment matrix.


## Usage

1. Run the `optimize_course_assignment` function in the provided Python script.
2. Enter the number of professors in each category, along with their preference lists.
3. View the generated bipartite graph and the results of the course assignment.


## Directory Structure

```plaintext
- Disco_Final.py   # Main.tex
- README.md                        # Project documentation

