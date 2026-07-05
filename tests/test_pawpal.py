from pawpal_system import Pet, Task


def test_task_completion_marks_task_complete():
    task = Task(description="Morning walk", time="08:00", frequency="daily")

    task.mark_complete()

    assert task.is_completed() is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    initial_count = pet.task_count()

    pet.add_task(Task(description="Feeding", time="09:00", frequency="daily"))

    assert pet.task_count() == initial_count + 1
