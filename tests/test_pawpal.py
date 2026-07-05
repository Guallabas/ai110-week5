from datetime import date, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_completion_marks_task_complete():
    task = Task(description="Morning walk", time="08:00", frequency="daily")

    task.mark_complete()

    assert task.is_completed() is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    initial_count = pet.task_count()

    pet.add_task(Task(description="Feeding", time="09:00", frequency="daily"))

    assert pet.task_count() == initial_count + 1


def test_scheduler_sorts_tasks_by_time():
    scheduler = Scheduler()
    tasks = [
        Task(description="Late task", time="10:00", frequency="daily"),
        Task(description="Early task", time="08:00", frequency="daily"),
        Task(description="Mid task", time="09:00", frequency="daily"),
    ]

    ordered = scheduler.sort_by_time(tasks)

    assert [task.description for task in ordered] == ["Early task", "Mid task", "Late task"]


def test_scheduler_marks_daily_task_complete_and_creates_next_occurrence():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)
    scheduler = Scheduler()
    task = Task(description="Feeding", time="09:00", frequency="daily", date=date.today().isoformat())
    pet.add_task(task)

    new_task = scheduler.mark_task_complete(owner, "Mochi", task)

    assert task.is_completed() is True
    assert new_task is not None
    assert new_task.frequency == "daily"
    assert new_task.date == (date.today() + timedelta(days=1)).isoformat()


def test_scheduler_detects_conflicts_for_duplicate_times():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    other_pet = Pet(name="Luna", species="cat")
    owner.add_pet(pet)
    owner.add_pet(other_pet)
    scheduler = Scheduler()

    pet.add_task(Task(description="Walk", time="08:00", frequency="daily"))
    other_pet.add_task(Task(description="Feeding", time="08:00", frequency="daily"))

    conflicts = scheduler.find_conflicts(owner)

    assert len(conflicts) == 1
    assert "Conflict at 08:00" in conflicts[0]
