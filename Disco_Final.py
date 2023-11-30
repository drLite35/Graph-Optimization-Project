import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def validate_preferences(preferences, courses):
    for faculty, pref_list in preferences.items():
        if len(pref_list) != 12 or not set(pref_list).issubset(set(courses)):
            raise ValueError(f"Invalid preference list for {faculty}")

# Function to create the bipartite graph
def create_bipartite_graph(faculty_categories, course_loads, preferences, all_courses):
    G = nx.Graph()

    # Add faculty nodes
    G.add_nodes_from(faculty_categories, bipartite=0)

    # Add course nodes
    G.add_nodes_from(all_courses, bipartite=1)

    # Ensure that each faculty member has exactly 12 preferences
    validate_preferences(preferences, all_courses)

    # Add edges based on preferences
    for faculty, pref_list in preferences.items():
        for course in pref_list:
            G.add_edge(faculty, course)

    # Ensure that each faculty member is fully assigned or not assigned at all
    for faculty in faculty_categories:
        G.add_edge(faculty, f"Unassigned_{faculty}", weight=0)

    return G

# Function to perform maximum bipartite matching and calculate total load
def perform_matching(G, faculty_categories, course_loads):
    all_matchings = list(nx.bipartite.maximum_matching(G))

    if not all_matchings:
        print("No valid assignment found.")
    else:
        # Create an empty matrix for course assignments
        course_assignment_matrix = np.full((len(faculty_categories), len(all_courses)), "Unassigned", dtype='<U10')

        for idx, matching in enumerate(all_matchings, start=1):
            print(f"\nMatching {idx}:")
            assignments = {faculty: course for faculty, course in (edge.split("_") for edge in matching) if not course.startswith("Unassigned")}
            for faculty, course in assignments.items():
                print(f"Course {course.split('Course')[1]} assigned to Prof {faculty}")

                # Fill the matrix with course assignments
                faculty_index = faculty_categories.index(faculty)
                course_index = int(course.split('Course')[1]) - 1  # Adjust index to start from 0
                course_assignment_matrix[faculty_index, course_index] = faculty

            # Calculate total course load assigned to each faculty
            total_load = {faculty: sum(course_loads[course]) for faculty, course in assignments.items()}
            print("\nTotal Course Load:")
            for faculty, load in total_load.items():
                print(f"Prof {faculty}: {load} courses")

        # Print the course assignment matrix
        print("\nCourse Assignment Matrix:")
        print("   ", end="")
        for course in all_courses:
            print(f" Course{course.split('Course')[1]}", end="")
        print()
        for i, row in enumerate(course_assignment_matrix):
            print(f"Prof {faculty_categories[i]}", end="")
            for assignment in row:
                print(f"    {assignment}", end="")
            print()

# Main function to orchestrate the entire process
def optimize_course_assignment():
    try:
        # Define faculty categories and their corresponding course loads
        faculty_categories = []
        num_professors = {}

        # User input for faculty categories and number of professors
        while True:
            faculty_category = input("Enter faculty category (or type 'done' to finish): ")
            if faculty_category.lower() == 'done':
                break
            num_professors[faculty_category] = int(input(f"Enter the number of professors in {faculty_category}: "))
            faculty_categories.append(faculty_category)

        # Validate that the total number of professors matches the specified total
        if sum(num_professors.values()) > 30 or sum(num_professors.values())==0:  # Adjust the total as needed
            raise ValueError("The total number of professors should be 30.")

        # Define course loads
        course_loads = {'x1': 0.5, 'x2': 1, 'x3': 1.5}

        # Predefined course names
        all_courses = [f"Course{i+1}" for i in range(12)]  # Adjust the number of courses as needed

        # User input for faculty preferences
        preferences = {}
        for faculty in faculty_categories:
            print(f"Enter preference list for {faculty} (exactly 12 courses):")
            pref_list = input().split()  # Read space-separated course names
            preferences[faculty] = pref_list

        # Create bipartite graph
        G = create_bipartite_graph(faculty_categories, course_loads, preferences, all_courses)

        # Draw the bipartite graph
        pos = nx.bipartite_layout(G, faculty_categories)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=800)
        plt.show()

        # Perform maximum bipartite matching and calculate total load
        perform_matching(G, faculty_categories, course_loads)

    except ValueError as e:
        print(f"Error: {e}")

# Run the optimization
optimize_course_assignment()