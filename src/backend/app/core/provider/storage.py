from app.core.interface.service import Service

class StorageService(Service):
    def set_ready(self):
        print("StorageService is ready")

    def teardown(self):
        print("StorageService is being torn down")

    def execute(self):
        print("Executing StorageService logic")