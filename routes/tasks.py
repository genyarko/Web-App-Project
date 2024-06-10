from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
@login_required
def view_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/tasks/new', methods=['GET', 'POST'])
@login_required
def new_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task(title=title, description=description, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully.')
        return redirect(url_for('tasks.view_tasks'))
    return render_template('new_task.html')

@tasks_bp.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        return redirect(url_for('tasks.view_tasks'))
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        db.session.commit()
        flash('Task updated successfully.')
        return redirect(url_for('tasks.view_tasks'))
    return render_template('edit_task.html', task=task)

@tasks_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        return redirect(url_for('tasks.view_tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully.')
    return redirect(url_for('tasks.view_tasks'))
