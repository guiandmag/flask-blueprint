from distutils.core import setup
from flask_blueprint import __version__

setup(
    name='flask-blueprint',
    version=__version__,
    description='Flask blueprint generator',
    author='Jeffrey Marvin Forones',
    author_email='aiscenblue@gmail.com',
    url='https://github.com/aiscenblue/flask-blueprint',
    packages=['flask_blueprint'],
    keywords=['flask', 'blueprint', 'flask-blueprint', 'flask_blueprint'],  # arbitrary keywords
    install_requires=[
        # list of this package dependencies
    ],
    entry_points=None
)
