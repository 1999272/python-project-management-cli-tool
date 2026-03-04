class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"