# from functools import wraps
# from uuid import uuid1
# from datetime import datetime
#
# from sql_app import crud, schemas
#
# from sqlalchemy.orm.session import Session
# from fastapi import Request
#
#
# def _get_request(kwargs: dict) -> Request:
#     for value in kwargs.values():
#         if type(value) is Request:
#             return value
#     raise ValueError('There is not Request params in arguments of function')
#
#
# def _get_db(kwargs: dict) -> Session:
#     for value in kwargs.values():
#         if str(type(value)) == "<class 'sqlalchemy.orm.session.Session'>":
#             return value
#     raise ValueError('There is not Session params in arguments of function')
#
#
# def session_counter(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'{func(args, **kwargs)}!!!')
#         db = _get_db(kwargs)
#         request = _get_request(kwargs)
#
#         user_session = schemas.CreateUserSession(
#             id=str(uuid1()),
#             ip=request.client.host,
#             datetime=datetime.now(),
#             path=request.url.path
#         )
#
#         crud.create_user_session(
#             db,
#             user_session
#         )
#
#         return func(*args, **kwargs)
#
#     return wrapper()
