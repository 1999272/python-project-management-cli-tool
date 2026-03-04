import argparse
from utils.helpers import load_data
from tabulate import tabulate

DATA_FILE = "data/datastore.json"

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)

    # add-project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("--user", required=True)
    project_parser.add_argument("--title", required=True)
    project_parser.add_argument("--description", required=True)
    project_parser.add_argument("--due_date", required=True)

    # list-projects
    list_parser = subparsers.add_parser("list-projects")
    list_parser.add_argument("--user", required=True)

    args = parser.parse_args()
    data = load_data(DATA_FILE)

    if args.command == "add-user":
        data["users"].append({"name": args.name, "email": args.email, "projects": []})
        from utils.helpers import save_data
        save_data(DATA_FILE, data)
        print(f"User {args.name} added.")

    elif args.command == "add-project":
        for user in data["users"]:
            if user["name"] == args.user:
                user["projects"].append({
                    "title": args.title,
                    "description": args.description,
                    "due_date": args.due_date,
                    "tasks": []
                })
                from utils.helpers import save_data
                save_data(DATA_FILE, data)
                print(f"Project {args.title} added to {args.user}.")
                return
        print(f"User {args.user} not found.")

    elif args.command == "list-projects":
        for user in data["users"]:
            if user["name"] == args.user:
                projects = [[proj["title"], proj["description"], proj["due_date"]] 
                            for proj in user["projects"]]
                if projects:
                    print(tabulate(projects, headers=["Title", "Description", "Due Date"]))
                else:
                    print(f"No projects found for {args.user}.")