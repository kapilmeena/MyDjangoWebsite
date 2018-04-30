# class MyCustomRouter(object):
#     """
#     A router to control all database operations on models in
#     the server_data application
#     """
#
#     def db_for_read(self, model, **hints):
#         """
#         Point all operations on server_data models to 'server'
#         """
#         if model._meta.app_label == 'server_data':
#             return 'sever'
<<<<<<< HEAD
#         elif model._meta.app_label == 'client_data':
=======
#         return None
#
#         else
#         if model._meta.app_label == 'client_data':
>>>>>>> refs/remotes/origin/master
#             return 'client'
#         return None
#
#     def db_for_write(self, model, **hints):
#         """
#         Point all operations on myapp models to 'other'
#         """
#         if model._meta.app_label == 'server_data':
#             return 'server'
<<<<<<< HEAD
#         elif model._meta.app_label == 'client_data':
#             return 'client'
=======
>>>>>>> refs/remotes/origin/master
#         return None
#
#     def allow_syncdb(self, db, model):
#         """
#         Make sure the 'server' app only appears on the 'other' db
#         """
#         if db == 'server':
#             return model._meta.app_label == 'server_data'
<<<<<<< HEAD
#         elif db == 'client':
#             return model._meta.app_label == 'client_data'
=======
>>>>>>> refs/remotes/origin/master
#         elif model._meta.app_label == 'server':
#             return False
#         return None