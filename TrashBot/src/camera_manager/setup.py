from setuptools import find_packages, setup

package_name = 'camera_manager'

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
            'cam_stream_node = camera_manager.cam_stream_node:main',
            'picam_stream_publisher = camera_manager.cam_publisher_compressed:main'
        ],
    },
)
