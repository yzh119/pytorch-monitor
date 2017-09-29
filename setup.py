from distutils.core import setup

setup(
    name='training_monitor',
    version='0.1.1',
    packages=[''],
    package_dir={'': 'training_monitor'},
    package_data={'': ['template/index.html', 'template/plot.html']},
    url='https://github.com/yzh119/training_monitor',
    license='GNU General Public License v3.0',
    author='expye',
    author_email='expye@outlook.com',
    description='Visualize training process'
)
