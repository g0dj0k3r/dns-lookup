from setuptools import setup, find_packages

setup(
    name='dnslookup',
    version='v3.0',
    author='Godjoker',
    url='github.com/g0dj0k3r',
    packages=find_packages(),
    py_modules=['guilookup','dns_lookup','whoiscan','perform','enumerator', 'user_manuel','guienumerator'],
    install_requires=[
        'dnspython',
        'python-whois',
        'colorama',
        'requests',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'dnslookup=dns_lookup:dlookup',
            'dnslookup-gui=guilookup:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        
        'Operating System :: OS Independent',
    ],
    python_requires='>=3'
)
