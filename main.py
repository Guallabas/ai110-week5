from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(name="Jordan")

    mocha = Pet(name="Mochi", species="dog")
    luna = Pet(name="Luna", species="cat")

    owner.add_pet(mocha)
    owner.add_pet(luna)

    # add tasks out of chronological order to test sorting
    mocha.add_task(Task(description="Feeding", time="09:00", frequency="daily", priority="high"))
    mocha.add_task(Task(description="Morning walk", time="08:00", frequency="daily", priority="high"))
    mocha.add_task(Task(description="Grooming", time="12:00", frequency="weekly", priority="low"))
    luna.add_task(Task(description="Play session", time="10:30", frequency="daily", priority="medium"))
    luna.add_task(Task(description="Feeding", time="09:00", frequency="daily", priority="high"))

    scheduler = Scheduler()
    print("Unsorted tasks:")
    for t in owner.get_all_tasks():
        print(f"- {t}")

    print("\nSorted tasks (all):")
    for t in scheduler.sort_by_time(owner.get_all_tasks()):
        print(f"- {t}")

    print("\nFiltered tasks (pending only):")
    # mark one task complete using scheduler to create next occurrence
    completed_task = owner.pets[0].tasks[0]
    new_occurrence = scheduler.mark_task_complete(owner, "Mochi", completed_task)
    print(f"Marked complete: {completed_task}")
    if new_occurrence:
        print(f"Created next occurrence: {new_occurrence}")

    for t in scheduler.filter_tasks(owner.get_all_tasks(), completed=False):
        print(f"- {t}")


if __name__ == "__main__":
    main()
