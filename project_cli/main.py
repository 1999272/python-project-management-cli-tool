import argparse
from utils.helpers import load_data, save_data
from rich.console import Console

console = Console()
DATA_FILE = "data/datastore.json"

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)

    # list-projects
    list_parser = subparsers.add_parser("list-projects")
    list_parser.add_argument("--user", required=True)

    # complete-task
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--user", required=True)
    complete_parser.add_argument("--project", required=True)
    complete_parser.add_argument("--task", required=True)

    args = parser.parse_args()
    data = load_data(DATA_FILE)

    if args.command == "add-user":
        data["users"].append({"name": args.name, "email": args.email, "projects": []})
        save_data(DATA_FILE, data)
        console.print(f"[green]User {args.name} added successfully![/]")

    elif args.command == "list-projects":
        for user in data["users"]:
            if user["name"] == args.user:
                console.print(f"[bold cyan]Projects for {user['name']}:[/]")
                for proj in user["projects"]:
                    console.print(f"- {proj['title']} (Due: {proj['due_date']})")

    elif args.command == "complete-task":
        for user in data["users"]:
            if user["name"] == args.user:
                for proj in user["projects"]:
                    if proj["title"] == args.project:
                        for task in proj["tasks"]:
                            if task["title"] == args.task:
                                task["status"] = "complete"
                                save_data(DATA_FILE, data)
                                console.print(f"[yellow]Task {task['title']} marked complete.[/]")
                                return

if __name__ == "__main__":
    main()