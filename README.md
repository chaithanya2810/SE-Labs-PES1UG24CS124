# Software Engineering Labs

**Name:** Chaithanya N
**SRN:** PES1UG24CS124
**Section:** B
**University:** PES University, Bengaluru
**Course:** Software Engineering Lab

This repo has all 7 of my SE lab submissions. Labs 1 to 3 are for one project, the **Digital Parking Reservation Gateway**. Labs 4 to 7 are separate hands-on labs (vibe coding, static analysis, coverage, fuzzing). Every lab folder has its own README with the details, linked below.

---

## Labs at a Glance

| Lab | Topic | Folder |
|-----|-------|--------|
| **Lab 1** | Requirements Engineering & UML Use-Case Modelling | [Lab1](Lab1/README.md) |
| **Lab 2** | Agile Backlog Creation & Sprint Simulation in Jira | [Lab2](Lab2/README.md) |
| **Lab 3** | Component Modelling & Architectural Pattern Selection | [Lab3](Lab3/README.md) |
| **Lab 4** | Vibe Coding (High-Low Card Predictor) | [Lab4](Lab4/README.md) |
| **Lab 5** | Static Code Analysis (Pylint, Bandit, Flake8) | [Lab5](Lab5/README.md) |
| **Lab 6** | Code and Branch Coverage Analysis | [Lab6](Lab6/README.md) |
| **Lab 7** | Fuzz Testing with Hypothesis | [Lab7](Lab7/README.md) |

---

## Repository Structure

```
SE-Labs-PES1UG24CS124/
├── Lab1/                                  # Lab 1 README
├── Lab2/                                  # Lab 2 README
├── Lab3/                                  # Lab 3 README
├── Lab4/                                  # High-Low Card Predictor
│   ├── README.md
│   ├── Lab_4_Details.pdf
│   └── chat_history.pdf
├── Lab5/                                  # Static code analysis
├── Lab6/                                  # Code and branch coverage
├── Lab7/                                  # Fuzz testing
├── digital-parking-reservation-gateway/   # Project files for Labs 1, 2 and 3
│   ├── requirements/
│   ├── uml/
│   ├── use-case-flow/
│   ├── Lab2.pdf
│   ├── Lab3_Architectural_Justification.pdf
│   ├── Lab3_Component_Diagram.png
│   └── README.md
└── README.md
```

---

## Labs 1 to 3: Digital Parking Reservation Gateway

A campus parking reservation system built around three actors: **Student**, **Security Staff** and **Parking Administrator**. The project files for all three labs are in [`digital-parking-reservation-gateway/`](digital-parking-reservation-gateway/README.md), and each lab folder has its own README.

| Lab | What I did | Links |
|-----|------------|-------|
| **Lab 1** | Wrote 5 functional and 2 non-functional requirements with acceptance criteria, drew the UML use-case diagram (`«include»` / `«extend»`), and wrote the flow for *Reserve Parking Slot* | [Lab 1 README](Lab1/README.md) · [Requirements Table](digital-parking-reservation-gateway/requirements/requirements-table.md) · [Use-Case Flow](digital-parking-reservation-gateway/use-case-flow/reserve-parking-slot.md) |
| **Lab 2** | Planned the project in Jira Scrum: Epics, User Stories, Story Points, split into two sprints | [Lab 2 README](Lab2/README.md) · [Lab 2 PDF](digital-parking-reservation-gateway/Lab2.pdf) |
| **Lab 3** | UML component diagram with 5 components, and chose Client-Server architecture with a written justification | [Lab 3 README](Lab3/README.md) · [Architectural Justification](digital-parking-reservation-gateway/Lab3_Architectural_Justification.pdf) · [Component Diagram](digital-parking-reservation-gateway/Lab3_Component_Diagram.png) |

---

## Lab 4: Vibe Coding (High-Low Card Predictor)

Fixed the existing bug in the High-Low Card Predictor and added the features from the assignment README, using ChatGPT as the vibe coding tool.

- Fixed card rank comparison (string to numeric)
- Added win streak multipliers
- Added tie / PUSH handling
- Added side-by-side card reveal

Each task was committed separately and tested before and after the changes.

- [Lab 4 README](Lab4/README.md)
- [Details PDF](Lab4/Lab_4_Details.pdf)
- [Chat history](Lab4/chat_history.pdf)
- [Individual game repo](https://github.com/chaithanya2810/55_card_predictor)

---

## Lab 5: Static Code Analysis

Ran Pylint, Bandit and Flake8 on a Python attendance tracker, then fixed the issues they reported (security, code quality and style) and re-ran all three to verify.

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.55 / 10 | 10.00 / 10 |
| Bandit | 8 issues (2 High, 3 Medium, 3 Low) | No issues |
| Flake8 | Multiple violations | No violations |

- [Lab 5 README](Lab5/README.md)
- [Fixed code](Lab5/attendance_tracker.py) · [Issues table](Lab5/issues.md) · [Reflection](Lab5/reflection.md)

---

## Lab 6: Code and Branch Coverage

Wrote test cases for a credit card rewards module and measured them with `coverage` and `pytest`, reaching 100% line coverage and 100% branch coverage.

| Type | Tests | Result |
|------|-------|--------|
| Code (line) coverage | 24 | 35 statements, 0 missed, 100% |
| Branch coverage | 28 | 26 branches, 0 partial, 100% |

- [Lab 6 README](Lab6/README.md)

---

## Lab 7: Fuzz Testing

Used Hypothesis to fuzz three input-parsing functions in a credit card rewards parser. It found crashes in all three (`None`, empty string and malformed inputs). I added input validation and re-ran the tests, and all 6 now pass.

- [Lab 7 README](Lab7/README.md)

---

## Author
**Chaithanya N** (PES1UG24CS124) · [@chaithanya2810](https://github.com/chaithanya2810)
