# pip install GitPython
import os
from git import Repo
os.system('cls')

base_dir = os.path.dirname(__file__)+'\\.git'
repo = Repo(base_dir)
assert not repo.bare