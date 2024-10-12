import graphviz
import os
import tempfile

# Define your AI client here
client = None  # Assuming this would be an AI/ML API client

def extract_text(file):
    # Dummy function to extract text from files
    return "Extracted text from file"

def get_workload_distribution(client, project_description, team_members):
    # Simulate task assignments based on team members' expertise
    return "Workload distribution response (dummy)"

def get_project_workflow(client, project_description):
    # Simulate project workflow generation
    return "Project workflow response (dummy)"

def generate_flowchart(assignment_response, workflow_response):
    try:
        # Create a new graph object
        dot = graphviz.Digraph()

        # Add nodes and edges based on assignment_response and workflow_response
        dot.node('A', 'Start')
        dot.node('B', 'Task Assignment')
        dot.node('C', 'Project Workflow')
        dot.node('D', 'End')

        # Add edges (define relationships)
        dot.edge('A', 'B')
        dot.edge('B', 'C')
        dot.edge('C', 'D')

        # Generate a temporary file for the flowchart image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            flowchart_path = tmp_file.name
            dot.render(flowchart_path, format='png')

        return flowchart_path
    except Exception as e:
        print(f"Error generating flowchart: {str(e)}")
        return None

def generate_project_structure(assignment_response):
    # Dummy function to simulate project structure generation
    return None

def suggest_project_names(client, project_description):
    # Simulate project name suggestions
    return "Project name suggestions (dummy)"












# # functions/flowchart_generation.py

# import graphviz
# import tempfile  # Add this import
# from typing import Dict
# import streamlit as st

# def generate_flowchart(workload_distribution: str, project_workflow: str) -> str:
#     try:
#         # Parse the workload_distribution and project_workflow to extract tasks and assignments
#         # For simplicity, assume that workload_distribution contains lines like "Member: Task"
#         tasks = {}
#         for line in workload_distribution.split('\n'):
#             if ':' in line:
#                 member, task = line.split(':', 1)
#                 tasks[member.strip()] = task.strip()
        
#         if not tasks:
#             st.error("No tasks found to generate a flowchart.")
#             return ""
        
#         # Create a flowchart
#         dot = graphviz.Digraph(comment='Project Flowchart', format='png')
        
#         dot.node('Start', 'Project Start')
#         dot.node('End', 'Project End')
        
#         prev = 'Start'
#         for member, task in tasks.items():
#             # Sanitize member name to create a valid node name
#             node_name = ''.join(e for e in member if e.isalnum() or e == '_')
#             if not node_name:
#                 node_name = f"Member_{list(tasks.keys()).index(member)+1}"
#             dot.node(node_name, f"{member}\n{task}")
#             dot.edge(prev, node_name)
#             prev = node_name
#         dot.edge(prev, 'End')
        
#         # Render the flowchart to a temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
#             dot.render(filename=tmpfile.name, cleanup=True)
#             flowchart_path = tmpfile.name + '.png'
        
#         return flowchart_path

#     except Exception as e:
#         st.error(f"Flowchart generation failed: {str(e)}")
#         return ""
