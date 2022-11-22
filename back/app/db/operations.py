from sqlalchemy.orm import Session

from . import schemas, models


def task_get_single(db: Session, task_id: int):
    '''
        return first task for the id passed
    '''
    return db.query(models.Todo).filter(models.Todo.id == task_id).first()


def task_get_list(db: Session, completed: bool, pending: bool):
    '''
        return list of all tasks
    '''
    if completed and pending:
        return db.query(models.Todo).all()

    if completed:
        return db.query(
            models.Todo).filter(models.Todo.is_completed == True).all()

    if pending:
        return db.query(
            models.Todo).filter(models.Todo.is_completed == False).all()

    return db.query(models.Todo).all()


def task_get_list_completed(db: Session):
    '''
        return list of all tasks that are completed
    '''
    return db.query(models.Todo).filter(models.Todo.is_completed == True).all()


def task_get_list_not_completed(db: Session):
    '''
        return list of all tasks that are not completed
    '''
    return db.query(
        models.Todo).filter(models.Todo.is_completed == False).all()


def task_create(db: Session, task: schemas.TaskCreate):
    new_task = models.Todo(task=task.task)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def task_delete(db: Session, task_id: int):
    deleted_task = db.query(
        models.Todo).filter(models.Todo.id == task_id).delete()
    if deleted_task:
        db.commit()

    return deleted_task


def task_status_update(db: Session, task_id: int):
    update_task = db.query(
        models.Todo).filter(models.Todo.id == task_id).first()

    if update_task is None:
        return update_task

    update_task.is_completed = True
    db.commit()
    db.refresh(update_task)

    return update_task
