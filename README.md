# 🧠 Constraint Satisfaction Problems (CSP) Projects Collection

This repository contains multiple implementations of classic Artificial Intelligence problems using **Constraint Satisfaction Problem (CSP)** techniques in Python.

---

## 📁 Project Structure

- q1 → Map Coloring (Australia)
- q2 → Telangana Map Coloring (GeoPandas + CSP + kml)
- q3 → Sudoku Solver (Backtracking)
- q4 → Cryptarithmetic Solver (TWO + TWO = FOUR)

---

# 🔹 Q1: Map Coloring using CSP (Australia)

## Overview
This project solves the Map Coloring Problem using CSP techniques. The goal is to assign colors to regions such that no two adjacent regions share the same color.

## Problem Description
States considered:
- WA (Western Australia)
- NT (Northern Territory)
- Queensland
- SA (South Australia)
- NSW (New South Wales)
- V (Victoria)
- T (Tasmania)

Colors used:
- Red
- Green
- Blue

## Adjacency Constraints
- WA → NT, SA  
- NT → WA, SA, Queensland  
- SA → WA, NT, Queensland, NSW, V  
- Queensland → NT, SA, NSW  
- NSW → Queensland, SA, V  
- V → SA, NSW  
- T → (no neighbors)

## Approach
- Uses **Backtracking Algorithm**
- Ensures no adjacent regions share the same color
- Recursive solution with constraint checking

---

# 🔹 Q2: Telangana Map Coloring using CSP (Automated Border Detection)

## Overview
This project extends the map coloring problem using real-world geospatial data. It automatically detects neighboring districts from a KML file and colors them using CSP.

## Key Features
- Automatic adjacency detection using GeoPandas
- CSP-based backtracking solution
- Degree heuristic (most constrained district first)
- Randomized color selection
- Visualization using Matplotlib

## Concepts Used
- Constraint Satisfaction Problem (CSP)
- Backtracking Algorithm
- Graph Coloring
- Degree Heuristic
- Geospatial Data Processing

## Input
- `telangana.kml` (district boundary file)

## How It Works
1. Load map using GeoPandas  
2. Detect neighbors using `.touches()`  
3. Build adjacency graph  
4. Apply CSP with heuristics  
5. Assign valid colors  
6. Visualize the colored map  

## Colors Used
- Red  
- Green  
- Blue  
- Yellow  

## Output
- Colored Telangana map
- No adjacent districts share the same color
- District labels and borders displayed

---

# 🔹 Q3: Sudoku Solver using CSP (Backtracking)

## Overview
This project solves a 9×9 Sudoku puzzle using CSP and backtracking.

## Problem Description
Rules:
- Each row → numbers 1–9 (no repetition)
- Each column → numbers 1–9
- Each 3×3 grid → numbers 1–9

Empty cells are represented by `0`.

## Approach
1. Find an empty cell  
2. Try numbers from 1–9  
3. Check validity:
   - Row constraint  
   - Column constraint  
   - 3×3 grid constraint  
4. Place number if valid  
5. Recursively solve  
6. Backtrack if needed  

## Functions Used
- `print_board()` → Displays Sudoku board  
- `find_empty()` → Finds empty cell  
- `is_valid()` → Validity check  
- `solve_sudoku()` → Main solver  

---

# 🔹 Q4: Cryptarithmetic Problem Solver (TWO + TWO = FOUR)

## Overview
This project solves a cryptarithmetic puzzle where each letter represents a unique digit.

## Problem Description

TWO + TWO = FOUR

Constraints:
- Unique digit for each letter  
- Leading digits (T, F) ≠ 0  
- Equation must be valid  

## Approach
- Uses **Brute Force with Permutations**

Steps:
1. Generate all permutations of digits  
2. Assign digits to letters (T, W, O, F, U, R)  
3. Skip invalid cases (leading zeros)  
4. Convert words into numbers:
   - TWO = 100*T + 10*W + O  
   - FOUR = 1000*F + 100*O + 10*U + R  
5. Check equation validity  
6. Stop when solution is found  

## Concepts Used
- Brute Force Search  
- Permutations (`itertools`)  
- Constraint Satisfaction  

---

# 🧩 Technologies Used

- Python 🐍  
- GeoPandas 🌍  
- Matplotlib 📊  
- itertools 🔢  

---

# 🚀 How to Run

```bash
# Clone the repository
git clone <your-repo-link>

# Navigate into project
cd CSP-Projects

# Run individual files
python q1.py
python q2.py
python q3.py
python q4.py
```

---

# 📌 Summary

This repository demonstrates how CSP techniques can be applied to:
- Graph coloring problems
- Real-world geospatial datasets
- Puzzle solving (Sudoku)
- Cryptarithmetic challenges

---

# 👨‍💻 Author

**Your Name**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!
