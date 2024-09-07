import pytest
import os
import time

if __name__ == '__main__':
    pytest.main()
    time.sleep(5)
    os.system("allure generate report/ -o report/html --clean")