from setuptools import setup

setup(
    name='1password2lastpass',
    version='0.1',
    py_modules=['1password2lastpass'],
    install_requires=[
        'Click',
    ],
    extras_require={
        'dev': [
            'flake8'
        ]
    },
    entry_points='''
        [console_scripts]
        1password2lastpass=1password2lastpass:main
    ''',
)
