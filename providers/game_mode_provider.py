class GameModeProvider:
    _instance = None
    _main_window = None

    @classmethod
    def set_instance(cls, instance, main_window=None):
        cls._instance = instance
        if main_window:
            cls._main_window = main_window

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise ValueError("Instance not set in GameModeProvider.")
        return cls._instance

    @classmethod
    def get_main_window(cls):
        if cls._main_window is None:
            raise ValueError("MainWindow not set in GameModeProvider.")
        return cls._main_window
