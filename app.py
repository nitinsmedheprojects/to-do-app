from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# In-memory task list
tasks = []

# Optional AI-powered task suggestion (bonus)
suggested_tasks = [
    "Read 30 mins",
    "Practice Python",
    "Exercise",
    "Write Journal",
    "Plan your day"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task and 0 <= task_id < len(tasks):
            tasks[task_id] = new_task
        return redirect(url_for("index"))
    return render_template("edit.html", task=tasks[task_id], task_id=task_id)

# Bonus route: auto-generate a random task
@app.route("/generate")
def generate():
    task = random.choice(suggested_tasks)
    tasks.append(task)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
