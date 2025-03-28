import os
import sys

# Добавляем путь к текущей директории в sys.path
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

# Импортируем main из venv/botnew.py
sys.path.append(os.path.join(dir_path, 'venv'))
from botnew import main

if __name__ == "__main__":
    main()
