from setuptools import setup

with open("README") as f:
      long_description = f.read()

setup(name='Adventure Quest',
      version='0.1',
      description='A quest for adventure!',
      long_description = long_description,
      url='https://github.com/DreamTeamXtreme/Adventure',
      author='DreamTeamXtreme',
      author_email='jacksonbbush@gmail.com',
      license='None', #TODO
      packages=['AdventureQuest'],
      #TODO add to below each time a package is used https://python-packaging.readthedocs.io/en/latest/dependencies.html
      dependency_links=[      "https://github.com/prompt-toolkit/python-prompt-toolkit.git" ], 
      install_requires=[
            'prompt_toolkit'
      ]
      # npyscreen
      # curses
      # wheel
      )