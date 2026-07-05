from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str = "general"
    time_window: Optional[str] = None

    def is_urgent(self) -> bool:
        return self.priority.lower() == "high"


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks_for_day(self) -> List[Task]:
        return list(self.tasks)


@dataclass
class Owner:
    name: str
    preferences: List[str] = field(default_factory=list)
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def update_preferences(self, preferences: List[str]) -> None:
        self.preferences = preferences


class Scheduler:
    def generate_plan(self, pet: Pet) -> List[Task]:
        return list(pet.get_tasks_for_day())

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.priority.lower(), reverse=True)

    def apply_constraints(self, tasks: List[Task]) -> List[Task]:
        return [task for task in tasks if task.duration_minutes > 0]
