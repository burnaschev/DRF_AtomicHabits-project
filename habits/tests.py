from datetime import datetime

from django.test import TestCase


def test():
    return datetime.now().time()

if __name__ == "__main__":
    print(test())