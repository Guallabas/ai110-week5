# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- The initial design centered on four main classes: Owner, Pet, Task, and Scheduler.
- Owner stores the pet owner’s name, preferences, and the pets they manage.
- Pet represents an individual animal and holds the animal’s name, species, and related tasks.
- Task captures a single care activity, including its description, time, frequency, priority, completion status, and optional date.
- Scheduler converts the stored tasks into a useful daily plan by sorting, filtering, and warning about conflicts.

**b. Design changes**

- The design stayed mostly intact, but it became more concrete during implementation.
- I used Python dataclasses for Task, Pet, and Owner because they made the object model simple to define and extend.
- The Scheduler grew from a simple placeholder into a small utility layer that handles sorting, completion filtering, recurrence, and conflict detection.
- I also chose to keep the logic separate from the UI so the Streamlit app could use the same backend behavior as the console demo.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- The scheduler currently considers task time, completion state, frequency, and priority.
- Time is the primary constraint because the app is meant to present a daily plan in chronological order.
- Priority influences ordering when two tasks have similar timing, and completion status helps the UI show only pending tasks.
- Frequency and date support recurring-task behavior when a task is marked complete.

**b. Tradeoffs**

- One tradeoff is that conflict detection is intentionally simple. It checks for exact matches in task times, rather than trying to reason about overlapping intervals or task duration.
- This is reasonable because the current app is focused on a lightweight pet-care planner. Exact-time checks are easy to understand, fast to compute, and sufficient for many common scheduling mistakes such as assigning the same time to two tasks.

---

## 3. AI Collaboration

**a. How I used AI**

- I used AI assistance to help structure the project, turn the UML design into Python classes, and refine the Streamlit integration.
- It was especially helpful for stepping through the implementation in smaller phases and for suggesting test cases around scheduling behavior.

**b. Judgment and verification**

- I did not accept every suggestion automatically. For example, I verified the scheduler behavior directly in the code and through pytest rather than trusting an implementation that looked plausible but was not yet tested.
- I used the test suite and manual inspection of the app flow to confirm that the logic worked as intended.

---

## 4. Testing and Verification

**a. What I tested**

- I tested task completion, task addition, sorting by time, recurring task creation for daily tasks, and conflict detection for duplicate times.
- These checks cover the core behaviors needed for the scheduler to be useful in a simple pet-care scenario.

**b. Confidence**

- I am confident that the current implementation works well for the core scenarios covered by the tests.
- If I had more time, I would add more edge-case tests for invalid times, empty task lists, and more complex overlap handling.

---

## 5. Reflection

**a. What went well**

- The strongest part of this project was connecting the backend logic to the UI without losing the clarity of the core object model.
- The scheduler and tests became a reliable foundation for the app.

**b. What I would improve**

- I would improve the scheduler next by supporting more realistic conflict detection, such as overlapping tasks based on duration and start/end times.
- I would also expand the UI to show more explanation for why a plan was generated.

**c. Key takeaway**

- A good system design becomes much easier to build and verify when the core classes are simple, the responsibilities are clear, and the behavior is tested early.

