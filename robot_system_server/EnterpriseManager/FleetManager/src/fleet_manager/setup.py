from setuptools import find_packages, setup

package_name = 'fleet_manager'

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
            'fleet_manager_node = fleet_manager.fleet_manager_node:main',
            'minibot_pos_calibrator = fleet_manager.minibot_pos_calibrate:main',
            'fleetmanager_control_ver1 = fleetmanager.fleetmanager_control_ver1:main',
            'fleetmanager_control_ver2 = fleetmanager.fleetmanager_control_ver2:main',
            'fleetmanager_control_ver3 = fleetmanager.fleetmanager_control_ver3:main',
            'fleetmanager_comunication = fleetmanager.fleetmanager_comunication:main',
            'fleetmanager_control_ver4 = fleetmanager.fleetmanager_control_ver4:main',  
            'fleetmanager_control_bridge_r0 = fleetmanager.fleetmanager_control_bridge_r0:main',
            'fleetmanager_control_bridge_r1 = fleetmanager.fleetmanager_control_bridge_r1:main',
        ],
    },
)
