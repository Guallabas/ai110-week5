from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(name="Jordan")

    mocha = Pet(name="Mochi", species="dog")
    luna = Pet(name="Luna", species="cat")

    owner.add_pet(mocha)
    owner.add_pet(luna)

    mocha.add_task(Task(description="Morning walk", time="08:00", frequency="daily", priority="high"))
    mocha.add_task(Task(description="Feeding", time="09:00", frequency="daily", priority="high"))
    luna.add_task(Task(description="Play session", time="10:30", frequency="daily", priority="medium"))

    scheduler = Scheduler()
    print(scheduler.format_schedule(owner))


if __name__ == "__main__":
    main()
