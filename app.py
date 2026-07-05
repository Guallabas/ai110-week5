import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

owner = st.session_state.owner
scheduler = Scheduler()

st.title("🐾 PawPal+")

st.markdown(
    """
This app now uses the backend logic layer to manage pets, tasks, and a simple daily schedule.
"""
)

st.divider()

st.subheader("Owner")
owner_name = st.text_input("Owner name", value=owner.name)
if owner_name != owner.name:
    owner.name = owner_name
    st.session_state.owner = owner

st.subheader("Add a pet")
pet_name = st.text_input("Pet name", value="Mochi", key="pet_name")
species = st.selectbox("Species", ["dog", "cat", "other"], key="pet_species")

if st.button("Add pet"):
    owner.add_pet(Pet(name=pet_name, species=species))
    st.session_state.owner = owner
    st.success(f"Added {pet_name} to {owner.name}'s profile.")

if owner.pets:
    st.write("Current pets:")
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Add a task")
if owner.pets:
    pet_names = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Choose pet", pet_names, key="selected_pet")
    selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)

    task_title = st.text_input("Task title", value="Morning walk", key="task_title")
    task_time = st.text_input("Time", value="08:00", key="task_time")
    frequency = st.selectbox("Frequency", ["daily", "weekly"], key="task_frequency")
    priority = st.selectbox("Priority", ["low", "medium", "high"], key="task_priority")

    if st.button("Add task"):
        selected_pet.add_task(
            Task(
                description=task_title,
                time=task_time,
                frequency=frequency,
                priority=priority,
            )
        )
        st.session_state.owner = owner
        st.success(f"Added task to {selected_pet.name}.")

    st.write(f"Pending tasks for {selected_pet.name}:")
    pending_tasks = scheduler.filter_tasks(selected_pet.get_tasks(), completed=False)
    sorted_tasks = scheduler.sort_by_time(pending_tasks)
    if sorted_tasks:
        task_rows = [
            {
                "Time": task.time,
                "Task": task.description,
                "Frequency": task.frequency,
                "Priority": task.priority,
            }
            for task in sorted_tasks
        ]
        st.table(task_rows)
    else:
        st.info("No pending tasks for this pet.")

    conflicts = scheduler.find_conflicts(owner)
    if conflicts:
        st.warning("Potential scheduling conflicts:")
        for conflict in conflicts:
            st.warning(conflict)
    else:
        st.success("No scheduling conflicts detected.")
else:
    st.info("Add a pet first to create tasks.")

st.divider()

st.subheader("Build Schedule")
if st.button("Generate schedule"):
    st.code(scheduler.format_schedule(owner), language="text")
