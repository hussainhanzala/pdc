Python Multiprocessing — Practical Demonstrations

This repository contains Python scripts demonstrating the multiprocessing module.
Each example uses a CPU-bound function do_something() (from do_something.py) to simulate computational work and illustrate various multiprocessing concepts, including:

Process creation and naming

Lifecycle management (start, join, terminate)

Synchronization (Lock, Barrier)

Daemon vs non-daemon behavior

Process pools

⚙️ 1. naming_processes.py

Purpose:
Show how to name processes and observe concurrent execution.

Core Example:

process_with_name = multiprocessing.Process(
    name='do_something process 1',
    target=do_something,
    args=(1000, out_list1)
)
process_with_default_name = multiprocessing.Process(
    target=do_something,
    args=(1000, out_list2)
)


Sample Output:

Process 1 output list length: 1000
Process 2 output list length: 1000
Total execution time: 0.43 seconds


Key Insight:
Named and unnamed processes execute concurrently, reducing overall execution time.

⚙️ 2. spawning_processes.py

Purpose:
Demonstrates spawning multiple processes dynamically in a loop.

Core Example:

for i in range(6):
    process = multiprocessing.Process(target=myFunc, args=(i,))
    process.start()
    process.join()


Sample Output:

calling do_something from process no: 0
Process 0 finished with 0 results.
calling do_something from process no: 1
Process 1 finished with 1000 results.
...


Key Insight:
Processes can handle independent workloads efficiently and scale tasks dynamically.

⚙️ 3. killing_processes.py

Purpose:
Shows process lifecycle control: start, terminate, and join.

Core Example:

p.start()
print('Process running:', p.is_alive())
p.terminate()
print('Process terminated:', p.is_alive())
p.join()


Sample Output:

Process running: True
Process terminated: False
Process joined: False
Exit code: 0


Key Insight:
Processes can be safely terminated and joined, with exit codes confirming proper shutdown.

⚙️ 4. run_background_processes_no_daemons.py

Purpose:
Compare daemon and non-daemon process behavior.

Core Example:

background_process.daemon = True
NO_background_process.daemon = False


Sample Output:

Starting background_process
---> 0
---> 1
---> 2
Starting NO_background_process
Results from do_something(): [0.0, 1.0, 2.0]
Exiting background_process
Exiting NO_background_process


Key Insight:
Daemon processes terminate with the main program; non-daemon processes complete independently.

⚙️ 5. processes_barrier.py

Purpose:
Demonstrates process synchronization using Barrier and Lock.

Core Example:

synchronizer = Barrier(2)
serializer = Lock()
Process(name='p1 - test_with_barrier',
        target=test_with_barrier,
        args=(synchronizer, serializer)).start()


Sample Output:

process p3 - test_without_barrier ----> 2025-11-01 00:27:31
p3 results: [0.0, 1.0]
process p1 - test_with_barrier ----> 2025-11-01 00:27:31
p1 results: [0.0, 1.0]


Key Insight:
Processes using barriers wait for each other before continuing, ensuring synchronized execution.

⚙️ 6. process_pool.py

Purpose:
Demonstrates parallel execution using a process pool.

Core Example:

inputs = list(range(0, 10))
pool = multiprocessing.Pool(processes=4)
pool_outputs = pool.map(do_something, inputs)


Sample Output:

Pool: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


Key Insight:
Process pools distribute workloads across cores efficiently, enabling concurrent task execution.

🧮 Summary Table
Script	Purpose	Result	Key Observation
naming_processes.py	Naming & parallel execution		Reduced total execution time
spawning_processes.py	Spawning processes via loop		Scalable independent workloads
killing_processes.py	Lifecycle management		Safe start, terminate, join
run_background_processes_no_daemons.py	Daemon vs Non-Daemon comparison		Daemon stops early; non-daemon completes
processes_barrier.py	Barrier & Lock synchronization		Ordered execution and controlled output
process_pool.py	Parallel execution with Pool		Efficient workload distribution
 Conclusion

Multiprocessing enables true parallelism for CPU-bound tasks.

Process naming, barriers, and locks make management predictable.

Lifecycle methods (start(), terminate(), join()) ensure control.

Daemon vs non-daemon processes behave differently.

Pools and barriers are essential for structured concurrency.

🧠 Key Takeaways

Python’s multiprocessing module allows scalable, parallel computation.

Proper synchronization prevents race conditions and ensures data consistency.

Understanding process control and coordination is crucial for high-performance Python applications.