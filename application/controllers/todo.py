# -*- coding: utf-8 -*-

import flask
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app, request, redirect, flash, render_template, url_for
from application.extensions import db
from application.models import Todo

todo_bp = flask.Blueprint(
    'todo',
    __name__,
    template_folder='../templates'
)


@todo_bp.route('/', methods=['GET', 'POST'])
def index():
    _form = request.form

    if request.method == 'POST':
        title = _form["title"]
        td = Todo(title=title)
        try:
            td.store_to_db()
            flash("add task successfully!")
            return redirect(url_for('todo.index'))
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Could not add task")
            flash("fail to add task!")

    return render_template('index.html', todo=Todo.query.order_by(Todo.id.desc()).all())


@todo_bp.route('/<int:todo_id>/del')
def del_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.delete_todo()
    flash("delete task successfully")
    return redirect(url_for('todo.index'))


@todo_bp.route('/<int:todo_id>/edit', methods=['GET', 'POST'])
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    if request.method == 'POST':
        Todo.query.filter_by(
            id=todo_id
        ).update({
            Todo.title: request.form['title']
        })
        db.session.commit()
        flash("update successfully!")
        return redirect(url_for('todo.index'))

    return render_template('edit.html', todo=todo)


@todo_bp.route('/<int:todo_id>/done')
def done(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        Todo.query.filter_by(id=todo_id).update({Todo.status: True})
        db.session.commit()
        flash("task is completed!")

    return redirect(url_for('todo.index'))


@todo_bp.route('/<int:todo_id>/redo')
def redo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        Todo.query.filter_by(id=todo_id).update({Todo.status: False})
        flash("redo successfully!")
        db.session.commit()

    return redirect(url_for('todo.index'))


@todo_bp.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
