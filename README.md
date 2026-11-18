# Creature Battle Project (OOP + Git Branching Practice)

This project is designed to help me learn **object-oriented programming**
in Python — especially **inheritance** — while also practicing key **Git
concepts** like branching, merging, conflict resolution, and version history.

I will begin with a base class (`Creature`) and create additional subclasses
on separate Git branches to simulate a real development workflow.

---

## Learning Objectives

### Python / OOP
- Understand and implement **classes**
- Use **inheritance** to extend behaviors
- Override and extend methods (e.g., `attack()`)
- Practice writing simple test code in `main`

### Git / Version Control
- Create and switch branches
- Merge branches into `main`
- Resolve merge conflicts
- View commit history (`git log --graph --all`)

---

## Project Structure
oop_creature_code/
│
├── creature_simulation.py # Base class + subclasses
└── README.md

---

## How to Run

Make sure you have Python 3 installed. From inside the `oop_creature_code`
folder, run:

```bash
python creature_simulation.py
```

This will execute the test code in the `if __name__ == "__main__":` block,
which creates instances of `Creature`, `FlyingCreature`, `SwimmingCreature`,
and `FireCreature`, and prints out their stats and attack results so you can
see inheritance and method overriding in action.

## What to submit
- Put the link to the Github repository to Google Classroom for grading