from setuptools import setup


setup(
        name='dotman', 
        version='0.1.0', 
        packages=['dotman'], 
        entry_points= {
            'console-scripts': [ 
                'dotman = dotman.__main__:main'
            ]
    })
