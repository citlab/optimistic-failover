import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_mako',
    'python-novaclient'
    ]

setup(name='service-dashboard',
      version='0.0',
      description='service-dashboard',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Tim Jungnickel',
      author_email='tim.jungnickel@gmail.com',
      url='',
      keywords='web dashboard openstack',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="servicedashboard",
      entry_points="""\
      [paste.app_factory]
      main = servicedashboard:main
      """,
      )
