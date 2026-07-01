from setuptools import setup

package_name = 'talker_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fishfarm',
    maintainer_email='fishfarm@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_node = talker_listener.talker_node:main',
            'listener_node = talker_listener.listener_node:main'

            # '노드_이름 = 패키지.노드_파일:main'  # 예: 'talker = my_package.talker_node:main'
        ],
    },
)
