# MaxHeap with Priority Queue Project

## Overview

This project implements a MaxHeap and PriorityQueue, demonstrating the application of heap operations for task prioritization. The heap structure is used to efficiently handle the insertion, extraction, and prioritization of tasks based on their priority values. This project provides an insight into the use of heap data structures and their application in real-world scenarios like task scheduling.

## Table of Contents

1. Project Structure
2. Features
3. Installation
4. Usage
5. Testing
6. Contributors
7. License

## Project Structure

```
heap_project/
│
├── main.py                # Main application logic (Member 4)
├── heap/
│   ├── __init__.py        # Initializes the heap package
│   ├── heap_base.py       # Base structure for the heap (Member 1)
│   ├── heap_operations.py # Heapify, Insert, Extract (Member 2)
├── priority_queue.py      # PriorityQueue implementation (Member 3)
├── tests/
│   ├── test_heap.py       # Unit tests for MaxHeap (Member 5)
│   ├── test_priority_queue.py  # Unit tests for PriorityQueue (Member 5)
├── demo.py                # Demonstration of heap operations (Member 6)
└── README.md              # Documentation and ADT specification (Member 6)
```

### Folder Breakdown:

- **heap_project/**: Root directory containing all project files.
- **main.py**: Contains the main logic where the PriorityQueue is demonstrated.
- **heap/**:
  - **heap_base.py**: Contains the MaxHeap base class, responsible for defining the basic heap structure.
  - **heap_operations.py**: Contains the heap operations like insert, extract, and heapify logic.
- **priority_queue.py**: Implements the PriorityQueue class using the MaxHeap for task prioritization.
- **tests/**:
  - **test_heap.py**: Unit tests for validating the functionality of the MaxHeap class.
  - **test_priority_queue.py**: Unit tests for validating the functionality of the PriorityQueue class.
- **demo.py**: Demonstrates heap operations in a user-friendly manner.
- **README.md**: Documentation and ADT specifications.

## Features

- **MaxHeap Implementation**: Core heap data structure with insert and extract operations.
- **Heapify Logic**: Ensures the heap property is maintained during insertions and deletions.
- **PriorityQueue**: Real-world application of the MaxHeap for task prioritization.
- **Unit Testing**: Ensures reliability of the implementation.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:veenjenga/AP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd heap_project
   ```
3. Install dependencies (if any).

## Usage

1. Run the main application:
   ```bash
   python main.py
   ```
2. Demonstrate the PriorityQueue using the demo script:
   ```bash
   python demo.py
   ```

## Testing

Run unit tests to validate the functionality of the MaxHeap and PriorityQueue:

```bash
python -m unittest discover tests
```

## Contributors

- **Joe (Member 1)**: Implemented the base structure of the MaxHeap.
- **Mutisya (Member 2)**: Developed core heap operations (heapify, insert, extract).
- **Vanessa (Member 3)**: Implemented the PriorityQueue using the MaxHeap.
- **Viona (Member 4)**: Developed the main application logic.
- **Tess (Member 5)**: Wrote unit tests for the heap and priority queue.
- **Richard (Member 6)**: Created the demo script and wrote the documentation.

## License

This project is licensed under the MIT License.
