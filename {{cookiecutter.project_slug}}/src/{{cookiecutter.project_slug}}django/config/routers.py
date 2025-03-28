from django.apps import apps


class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {"auth", "contenttypes", "admin"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth_db"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "auth_db"
        return None


class DatabaseRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    intranet_tables = {"tbl_user"}
    {{cookiecutter.project_slug}}_tables = {"old_wip_steerer_projects", "old_wip_steerer_metha_project"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.db_table in self.intranet_tables:
            return "intranet"
        else:
            return "{{cookiecutter.project_slug}}"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.db_table in self.intranet_tables:
            return "intranet"
        else:
            return "{{cookiecutter.project_slug}}"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.db_table in self.intranet_tables
            or obj2._meta.db_table in self.intranet_tables
        ):
            return True
        elif (
            obj1._meta.db_table in self.{{cookiecutter.project_slug}}_tables
            or obj2._meta.db_table in self.{{cookiecutter.project_slug}}_tables
        ):
            return True
        return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     db_table = apps.get_model(app_label,model_name)._meta.db_table
    #     if db_table in self.{{cookiecutter.project_slug}}_tables:
    #         return db == "{{cookiecutter.project_slug}}"
    #     elif db_table in self.intranet_tables:
    #         return db == "intranet"
    #
    #     return None
