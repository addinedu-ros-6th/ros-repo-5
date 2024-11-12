from setuptools import find_packages, setup

package_name = 'deeplearning_manager'

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
    maintainer='jeback',
    maintainer_email='wpqordlek@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dl_manager_node = deeplearning_manager.dl_manager_node:main',
            'picam_stream_processor = deeplearning_manager.cam_subscriber_and_process:main',
            'picam_yolo_processor = deeplearning_manager.cam_subscriber_and_yolo:main', 
        ],
    },
)