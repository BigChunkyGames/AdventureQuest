from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='A quest for adventure!',
      url='https://github.com/DreamTeamXtreme/Adventure',
      author='DreamTeamXtreme',
      author_email='jacksonbbush@gmail.com',
      license='None', #TODO
      packages=['AdventureQuest'],
      zip_safe=False,
      #TODO add to below each time a package is used https://python-packaging.readthedocs.io/en/latest/dependencies.html
      dependency_links=["https://github.com/prompt-toolkit/python-prompt-toolkit.git"] 
      # npyscreen
      # curses
      # wheel
      )