class Task:
    def __init__(self, title, assigned_to, status="pending"):
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    def mark_complete(self):
        self.status = "complete"

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"