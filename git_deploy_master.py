# pip install GitPython
import os
from git import Repo
os.system('cls')

base_dir = os.path.dirname(__file__)+'\\.git'
repo = Repo(base_dir)
assert not repo.bare

git = repo.git
git.checkout('HEAD', "my_new_branch")         # create a new branch
git.checkout('HEAD', b="my_new_branch2")         # create a new branch
git.branch('another-new-one')
git.branch('-D', 'another-new-one')             # pass strings for full control over argument order
git.for_each_ref()                              # '-' becomes '_' when calling it