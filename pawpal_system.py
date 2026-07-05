from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "daily"
    completed: bool = False
    priority: str = "medium"

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True

    def is_completed(self) -> bool:
        """Return whether the task has been completed."""
        return self.completed

    def __str__(self) -> str:
        """Return a readable summary of the task."""
        status = "✓" if self.completed else "•"
        return f"{status} {self.time} - {self.description} ({self.frequency})"


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return list(self.tasks)

    def get_pending_tasks(self) -> List[Task]:
        """Return tasks that are still incomplete."""
        return [task for task in self.tasks if not task.completed]

    def task_count(self) -> int:
        """Return the number of tasks assigned to this pet."""
        return len(self.tasks)


@dataclass
class Owner:
    name: str
    preferences: List[str] = field(default_factory=list)
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's account."""
        self.pets.append(pet)

    def update_preferences(self, preferences: List[str]) -> None:
        """Replace the owner's current preferences."""
        self.preferences = preferences

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from every pet owned by this person."""
        tasks: List[Task] = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks from all owned pets."""
        return [task for task in self.get_all_tasks() if not task.completed]


class Scheduler:
    def retrieve_tasks(self, owner: Owner) -> List[Task]:
        """Collect tasks from all of the owner's pets."""
        return owner.get_all_tasks()

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time and then by priority."""
        return sorted(
            tasks,
            key=lambda task: (self._time_to_minutes(task.time), task.priority.lower()),
        )

    def build_daily_schedule(self, owner: Owner) -> List[Task]:
        """Build a sorted daily schedule from the owner's pets."""
        tasks = self.retrieve_tasks(owner)
        return self.sort_tasks(tasks)

    def format_schedule(self, owner: Owner) -> str:
        """Create a readable text schedule for the terminal."""
        lines = [f"Today's Schedule for {owner.name}:"]
        for task in self.build_daily_schedule(owner):
            lines.append(str(task))
        return "\n".join(lines)

    def _time_to_minutes(self, time_value: str) -> int:
        """Convert a HH:MM string to minutes for sorting."""
        hour_text, minute_text = time_value.split(":")
        return int(hour_text) * 60 + int(minute_text)
