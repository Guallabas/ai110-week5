# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- My initial UML design centered on four main classes: Owner, Pet, Task, and Scheduler.
- Owner is responsible for storing the owner’s name, preferences, and the pets they manage.
- Pet represents an individual animal and holds its name, species, and related tasks.
- Task captures a single care activity, including its duration, priority, category, and optional time window.
- Scheduler is responsible for turning the pet’s tasks into a daily plan based on the available information.
- Core user actions for the app:
  - Add a pet to the system
  - Add or edit care tasks for a pet
  - Generate a daily care plan for the pet
- Main building blocks for the system:
  - Owner: stores the owner name, pet care preferences, and a list of pets; methods may include adding a pet and updating preferences.
  - Pet: stores the pet name, species, and associated care tasks; methods may include adding or removing tasks and retrieving tasks for a day.
  - Task: stores the task title, duration, priority, category, and optional time constraints; methods may include marking a task complete or checking whether it is urgent.
  - Scheduler: uses the owner, pet, and task information to create a daily plan; methods may include sorting tasks, applying constraints, and generating a schedule.

**b. Design changes**

- I kept the original structure mostly intact, but I simplified the initial design so it would be easier to implement as a clean Python skeleton.
- I chose to use dataclasses for Task and Pet to make the objects easier to define and extend later.
- I also kept the Scheduler methods lightweight at this stage, since the focus for Phase 1 was on structure rather than full scheduling logic.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

- Tradeoff: The scheduler currently detects conflicts using an exact-time match (tasks with identical `HH:MM` times). It does not attempt to detect overlapping tasks based on duration or more complex calendar semantics.

- Why reasonable: Exact-time conflict detection is lightweight and easy to reason about; it gives immediate, actionable warnings without requiring task duration parsing, timezone handling, or a more complex interval-overlap algorithm. For many simple pet-care scenarios (fixed feeding/walk times), exact matches catch the most common problems while keeping the scheduler simple and predictable.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- I tested task completion, task addition, sorting by time, recurring task creation for daily tasks, and conflict detection for duplicate times.
- These behaviors were important because they cover the core scheduling logic and the most likely failure points in a simple pet-care planner.

**b. Confidence**

- I am fairly confident that the current scheduler works correctly for the core scenarios covered by the tests.
- If I had more time, I would test edge cases such as tasks with no time, pets with no tasks, and overlapping tasks with different durations.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
