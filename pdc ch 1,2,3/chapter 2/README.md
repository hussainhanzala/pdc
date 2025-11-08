 Thread Synchronization Techniques in Python
(Using Lock, RLock, Semaphore & Condition)

This project demonstrates how various thread synchronization primitives from Python’s threading module manage concurrent access to a shared list via a common computation function: do_something.py.

It compares how Lock, RLock, Semaphore, and Condition coordinate multiple threads and ensure data safety in a multi-threaded environment.

 Synchronization Methods Overview
1️ Lock

Purpose:
Ensures that only one thread modifies the shared resource (out_list) at a time.

Observed Output:

Thread 0 started.
Thread 0 finished.
Thread 1 started.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Lock): 21


Conclusion:
Threads executed sequentially with no overlap.
All threads safely updated the shared list, producing the expected total of 21 items.
Ideal for basic mutual exclusion where only one thread should operate at once.

2️⃣ RLock (Reentrant Lock)

Purpose:
Allows the same thread to acquire the same lock multiple times safely (useful in nested functions).

Observed Behavior:
Execution order mirrored the Lock version — each thread executed sequentially and safely.

Conclusion:
RLock ensured thread-safe access while supporting recursive locking.
Best suited for scenarios where a single thread may re-enter critical sections multiple times.

3️⃣ Semaphore

Purpose:
Restricts how many threads can access a resource concurrently.

Observed Output:

Thread 0 waiting for permit...
Thread 0 started.
Thread 1 waiting for permit...
Thread 2 waiting for permit...
Thread 1 started.
Thread 0 finished.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Semaphore): 21


Conclusion:
The semaphore controlled how many threads could work simultaneously.
It allowed controlled parallel execution, preventing race conditions while maintaining correct results.
Useful for resource-limited systems (e.g., limited I/O channels or API connections).

4️⃣ Condition

Purpose:
Facilitates coordination and signaling between threads — one thread can wait while another sends a notification.

Observed Output:

Thread 0 notifying condition.
Thread 1 notifying condition.
Thread 2 notifying condition.
Monitor: Current length = 7
Monitor: Current length = 14
Monitor: Current length = 21


Conclusion:
Condition variables enabled smooth coordination between worker threads and a monitor thread.
This mechanism is perfect for event-driven workflows such as producer-consumer models or progress tracking.

📊 Comparison Table
Synchronization Type	Core Function	Behavior Description	Data Safety	Ideal Use Case
Lock	Prevents simultaneous modification	Sequential thread execution	 Safe	Basic mutual exclusion
RLock	Lock can be re-acquired by same thread	Similar to Lock (reentrant)	 Safe	Nested locking situations
Semaphore	Limits concurrent threads	Controlled parallel access	 Safe	Shared resource management
Condition	Wait/notify signaling mechanism	Event-driven coordination	 Safe	Producer-consumer / signaling tasks
🧠 Summary

All four synchronization methods — Lock, RLock, Semaphore, and Condition — successfully prevented data corruption during concurrent thread execution.

Each approach maintained consistent results (21 total items) and prevented race conditions:

Lock / RLock → Basic mutual exclusion (RLock adds recursive safety).

Semaphore → Allows controlled concurrency.

Condition → Enables signaling between threads.

 Key takeaway:
Choose your synchronization primitive based on your concurrency requirements — simplicity (Lock), recursion (RLock), resource control (Semaphore), or coordination (Condition).

▶️ Running the Examples

Run each synchronization example individually to observe its behavior:

python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py


Each script demonstrates a unique synchronization technique using the same shared computation logic from do_something.py.

 Dependencies

Python 3.x

No external libraries required (threading is built-in)

 Final Thoughts

Thread synchronization is critical in multi-threaded applications to prevent data inconsistency and unexpected behavior.
Python’s threading module offers versatile primitives — use them wisely based on task structure and concurrency goals.