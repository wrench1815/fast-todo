from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..db import operations as op
from ..dependencies import get_db
from ..db import schemas

router = APIRouter(
    prefix='/todo',
    tags=['todo'],
)


@router.get('/',
            response_model=list[schemas.TaskFull],
            status_code=status.HTTP_200_OK)
def task_list(*,
              db: Session = Depends(get_db),
              completed: bool | None = False,
              pending: bool | None = False):
    '''
        lists all todo tasks
    '''
    task_list = op.task_get_list(db, completed, pending)
    return task_list


@router.get('/{task_id}',
            response_model=schemas.TaskFull,
            status_code=status.HTTP_200_OK)
def task_single(*, db: Session = Depends(get_db), task_id: int):
    '''
        returns single task for id passed
    '''
    fetched_task = op.task_get_single(db, task_id)
    if fetched_task is None:
        raise HTTPException(status_code=404, detail='task does not exist')

    return fetched_task


@router.post('/',
             response_model=schemas.TaskFull,
             status_code=status.HTTP_201_CREATED)
def task_add(*, db: Session = Depends(get_db), task: schemas.TaskCreate):
    '''
        adds a new task
    '''
    new_task = op.task_create(db, task)
    if new_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='failed to add task')
    return new_task


@router.delete('/{task_id}', status_code=status.HTTP_200_OK)
def task_delete(*, db: Session = Depends(get_db), task_id: int):
    '''
        delete a task of id passed
    '''
    delete_resp = op.task_delete(db, task_id)
    if not delete_resp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='unable to delete task, check if it exist or not')
    return JSONResponse(content={'detail': 'task deleted'},
                        status_code=status.HTTP_200_OK)


@router.get('/{task_id}/complete', status_code=status.HTTP_200_OK)
def task_manage(*, db: Session = Depends(get_db), task_id: int):
    '''
        mark a task complete of passed id if it exist
    '''
    task = op.task_status_update(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='unable to mark task complete, check if it exist or not')

    return task
