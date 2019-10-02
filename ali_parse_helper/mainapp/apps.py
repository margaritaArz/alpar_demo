from django.apps import AppConfig
from parser_tools import test_print


class MainappConfig(AppConfig):
    name = 'mainapp'

    def ready(self):
        test_print.test()
