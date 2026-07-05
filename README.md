# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Sample output from running the CLI demo script:

```text
Today's Schedule for Jordan:
• 08:00 - Morning walk (daily)
• 09:00 - Feeding (daily)
• 10:30 - Play session (daily)
```

## 🧪 Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The current test suite covers:
- task completion status
- adding tasks to a pet
- sorting tasks by time
- recurring task creation for daily tasks
- conflict detection for duplicate times

Sample test output:

```text
.....                                                                    [100%]
5 passed in 0.03s
```

Confidence level: ⭐⭐⭐⭐☆

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

This project includes a set of simple scheduling features implemented in the logic layer. Methods and behaviors:

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time`, `Scheduler.sort_tasks` | Sorts tasks by `HH:MM` time and optionally by priority.
| Filtering | `Scheduler.filter_tasks`, `Scheduler.tasks_for_pet`, `Scheduler.sort_and_filter` | Filter by completion status or pet name; can combine with sorting.
| Conflict detection | `Scheduler.find_conflicts` | Lightweight exact-time conflict detection. Returns readable warnings when two or more tasks share the same `HH:MM` time.
| Recurring tasks | `Scheduler.mark_task_complete` | When a `daily` or `weekly` task is completed, a new task instance for the next occurrence is created (uses task `date` if present, otherwise today).

These features are intentionally simple to keep the code easy to reason about. See `pawpal_system.py` for the method implementations and `main.py` for simple CLI demos.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
