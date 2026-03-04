import pytest
from models.user import User
from models.project import Project
from models.task import Task

def test_user_project_task():
    u = User("Alex", "alex@example.com")
    p = Project("CLI Tool", "Build CLI", "2026-03-10")
    t = Task("Implement add-task", u)

    u.add_project(p)
    p.add_task(t)

    assert u.projects[0].title == "CLI Tool"
    assert p.tasks[0].status == "pending"
    assert t.assigned_to == u