from setuptools import setup
import os
from glob import glob

package_name = 'turtlebot_autonomous_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rafa',
    maintainer_email='rafa@example.com',
    description='Pacote para navegação autônoma com TurtleBot3',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'autonomous_nav_node = turtlebot_autonomous_nav.autonomous_nav_node:main',
        ],
    },
)
