class CubeProvider:
    _instance = None

    @classmethod
    def set_instance(cls, instance):
        cls._instance = instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise ValueError("Instance not set in Cube.")
        return cls._instance