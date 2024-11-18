from setuptools import find_packages, setup

package_name = 'trashbot_manager'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='minibot',
    maintainer_email='minibot@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pushbutton_publisher = trashbot_manager.pushbutton_publisher:main',
            'detectedSensor_server = trashbot_manager.detectedSensor_server:main',
            'trashbot_device = trashbot_manager.trashbot_device:main'
        ],
    },
)
