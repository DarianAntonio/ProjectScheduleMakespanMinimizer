# ProjectScheduleMakespanMinimizer
## Overview
This project solves a complex variant of the Job Shop Scheduling Problem using a genetic algorithm. It focuses on scheduling tasks with non-trivial precedence constraints and worker-task assignments, aiming to minimize the makespan (the total time required to complete all tasks).

Unlike traditional job-shop problems, this version supports:

- Arbitrary precedence between tasks (across jobs)

- Fixed worker-task assignments

- Multi-worker tasks (optional feature)

## Why Genetic Algorithm?
Genetic algorithms provide flexibility in tackling NP-hard problems like this. The core GA structure remains adaptable across many problem variations, with tunable components such as:
- Chromosome representation
- Mutation function
- Crossover function
- Fitness function
- Selection function
  
This makes the solution robust against constraint changes that would break standard schedulers.

## Problem Description
Given:

- A set of tasks with arbitrary precedence constraints

- A set of workers with pre-defined task assignments

- Fixed task durations

- A defined order in which each worker handles their tasks

The goal is to compute a schedule that minimizes the makespan, while respecting precedence and resource constraints.

## How It Works
Chromosome Representation
A chromosome consists of:

- A list of (worker, job) pairs

- A job priority list (defines task execution order)

- A cached fitness value

To ensure valid schedules:

- The job priority list is generated by traversing a directed acyclic graph of tasks, starting from a dummy "Start" node.

- Invalid individuals (e.g., those violating precedence) are repaired during mutation/crossover.

## Genetic Algorithm Components
- Fitness Function: Calculates the makespan by simulating the execution of tasks using worker availability and precedence constraints.

- Selection: Rank-based selection is used to preserve diversity.

- Crossover: Single-point crossover on both the worker/job list and the job priority list. Invalid priority lists are repaired post-crossover.

- Mutation: Swaps elements in the worker/job list and job priority list. Validation and repair are applied as needed.

## Core Data Structures
- A custom directed acyclic graph structure is used to represent and traverse task dependencies efficiently.
- The input of problem was stored in hashmaps/dictionaries optimized for fast access.
- The chromosome representation is a dictionary with a list of pairs, job priority list and cached fitness function result.

## How to Use
- Option 1: Run the program using the executable inside the dist/main folder.

- Option 2: From Source python main.py

### Input
Available input examples are stored in dist/main
- Projects are defined via CSV files.
- The tool includes a basic CSV editor for modifying tasks, workers, durations, and constraints.
### Output
The resulting schedule is visualized using a Gantt chart.
## About This Project
This project was developed as my individual final-year project in a BSc Artificial Intelligence and Computer Science degree. It was designed and implemented from scratch and only used Python and PySide6(for gui) as tech stack, focusing on solving a real-world variant of an NP-hard scheduling problem using evolutionary computing principles. I chose a genetic algorithm to solve the scheduling problem because I did not choose it as part of my modules, providing an opportunity to learn and explore evolutionary algorithms. This allowed me to expand my knowledge in optimization techniques and problem-solving.
