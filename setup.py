from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1.0",
    author="",
    author_email="",
    description="Python Framework.",
    license="MIT",
    url="",
    packages=find_packages(),
    entry_points={
    },
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: NLP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
            'pandas',
            'numpy',
            'Flask==1.0.2',
            'flask_restplus==0.11.0',
            'xgboost',
            'flask-cors',
            'pymysql',
            'tqdm',
            'pytest',
            'scikit-learn==0.20.1'
    ],
    zip_safe=True,
)
