import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt')) as f:
    requires = filter(None, f.readlines())


setup(name='unicore-cms-ebola',
      version='0.2',
      description='Ebola Pyramid Frontend Site for Universal Core ',
      long_description='Ebola Pyramid Frontend Site for Universal Core ',
      classifiers=[
      "Programming Language :: Python",
      "Framework :: Pyramid",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Praekelt Foundation',
      author_email='dev@praekelt.com',
      url='http://github.com/universalcore/unicore-cms-ebola',
      license='BSD',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="unicorecmsebola",
      entry_points="""\
      [paste.app_factory]
      main = unicorecmsebola:main
      """,
      message_extractors={'.': [
      ('**.py', 'python', None),
      ('**.pt', 'chameleon', None),
      ]},
      )
