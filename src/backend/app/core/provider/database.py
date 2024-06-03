from app.core.interface.service import Service

class DatabaseService(Service):
    def set_ready(self):
        print("DatabaseService is ready")

    def teardown(self):
        print("DatabaseService is being torn down")

    def execute(self):
        print("Executing DatabaseService logic")
