from setuptools import setup, find_packages

requires = ['hanziconv', 'snownlp']

setup(
        name='bei',
        version='0.0.1',
        description='Gather sentiment analysis on bei',
        author='Sophia Anderson',
        author_email='sophieanderson80@gmail.com',
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python:: 3.5',
        ],
        packages=find_packages(),
        package_data={},
        py_modules=['bei'],
        install_requires=requires,
)
