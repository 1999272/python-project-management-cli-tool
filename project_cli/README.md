# python-project-management-cli-tool
Here’s a ready‑to‑paste **README.md** written in Markdown for your project. It’s simple, clear, and matches the level you’ve learned so far:

```markdown
# Project Management CLI Tool

A simple Python command‑line interface (CLI) application for managing users, projects, and tasks.  
This project was built as a lab assessment to practice object‑oriented programming, file I/O, and basic CLI design.

---

## Project Structure
```
project_cli/
│── main.py              
│── models/
│   ├── user.py
│   ├── project.py
│   └── task.py
│── utils/
│   └── helpers.py
│── data/
│   └── datastore.json   
│── tests/
│   └── test_models.py   
│── requirements.txt
│── README.md
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-cli-tool.git
   cd project-cli-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the CLI:
   ```bash
   python main.py --help
   ```

---

## CLI Commands

### Add a User
```bash
python main.py add-user --name "Alex" --email "alex@example.com"
```

### Add a Project
```bash
python main.py add-project --user "Alex" --title "CLI Tool" --description "Build CLI system" --due_date "2026-03-10"
```

### List Projects
```bash
python main.py list-projects --user "Alex"
```
Example output (using `tabulate`):
```
Title      Description       Due Date
---------  ----------------  ----------
CLI Tool   Build CLI system  2026-03-10
```

### Complete a Task
```bash
python main.py complete-task --user "Alex" --project "CLI Tool" --task "Implement add-task"
```

## External Package
This project uses:
- **tabulate** → for clean table output in the CLI.

---

## Testing
Run tests with:
```bash
pytest
```

Example test file: `tests/test_models.py` checks that a User can have Projects and Projects can have Tasks.

---

## Features
- Manage users with name and email.
- Assign projects to users with title, description, and due date.
- Add tasks to projects and mark them complete.
- View projects in a neat table format.
- Data saved and loaded via JSON.


## Author
Lab assessment project by Mark.
```



