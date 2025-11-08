Matrix Multiplication: Multiprocessing vs. Multithreading
🔍 Project Overview

This project showcases how matrix multiplication performs under two parallelism approaches in Python — multiprocessing and multithreading — using NumPy for numerical operations.

The main objective is to analyze performance differences and understand how Python’s execution model affects CPU-bound workloads.

⚙️ How It Works

Matrix Creation

Two random square matrices of size 500 × 500 are generated using numpy.random.rand().

These serve as input for multiple independent computations.

Computation

Each operation performs matrix multiplication using numpy.dot().

The resulting matrix is then summarized (e.g., by summing all elements) to simulate realistic output handling.

Parallel Execution

Multiprocessing — Each task runs in a separate process with its own memory space, bypassing the Global Interpreter Lock (GIL). Ideal for CPU-heavy operations but has higher startup cost.

Multithreading — Multiple threads share memory and execute concurrently but are limited by the GIL, meaning only one thread executes Python bytecode at a time for CPU-bound workloads.

▶️ How to Run
python main.py


You can change the number of processes or threads by modifying the variable procs inside the script.
Try testing with different values like 1, 5, 10, 15, 20 to see how performance scales.

🧪 Experimental Results
Processes / Threads	Multiprocessing Time (s)	Multithreading Time (s)
1	0.569	0.073
5	0.835	0.119
10	1.333	0.287
15	1.919	0.586
20	4.032	0.431
📊 Performance Breakdown
🧠 1. Single Process / Thread

Multiprocessing (0.569s) is slower due to process creation overhead.

Threads (0.073s) reuse the same memory and start faster.

⚡ 2. 5 Units of Parallelism

Multiprocessing rises slightly to 0.835s.

Multithreading increases to 0.119s — still faster.

Overhead begins to appear but is manageable at this scale.

💻 3. 10–15 Parallel Units

Multiprocessing times grow (1.3s–1.9s).

Threads also slow down (0.28s–0.58s) but remain quicker.

The workload is too small for multiprocessing to benefit; overhead dominates.

🚀 4. 20 Parallel Units

Multiprocessing spikes to 4.03s due to context switching and memory copying.

Threads maintain 0.43s — small fluctuations due to scheduling but generally stable.

🧭 Key Insights

Multiprocessing

Best for large-scale, CPU-intensive computations.

Avoid exceeding your number of physical CPU cores.

Overhead can negate benefits for small workloads.

Multithreading

Suffers from Python’s GIL on CPU-bound tasks.

Still faster for lightweight or I/O-bound work because threads are cheaper to create and manage.

Recommended Strategy

For heavy numeric tasks → use multiprocessing with limited processes (equal to CPU cores).

For smaller jobs or I/O-heavy workloads → multithreading is more efficient.

🧩 Dependencies

Requirements:

Python 3.x

NumPy

Installation:

pip install numpy

💡 Conclusion

This experiment highlights that more parallel units ≠ faster execution — the nature of the task matters.
Python’s GIL restricts true parallel CPU execution for threads, while multiprocessing overcomes that at the cost of higher overhead.

For optimal performance:

Match process count ≈ CPU core count.

Use threads for small or mixed workloads.