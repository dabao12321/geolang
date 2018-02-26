from distutils.core import setup

with open('docs/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='geolang',
      version='1.0',
      description='Language and Geographic Origin',
      author='Amanda Li',
      author_email='ali2@andover.edu',
      url="https://github.com/dabao12321/geolang",
      license="MIT",
      packages=['geolang',
    	      "geolang.src",
              "geolang.src.classifiers",
              "geolang.src.cleaners",],
      install_requires=requirements
     )
