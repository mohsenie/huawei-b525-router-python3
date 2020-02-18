import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huawei-lte-python3",
    version="1.0.0",
    author="Hamish McNeish",
    author_email="https://github.com/jinxo13",
    description="This package allows programmatic access to the Huawei LTE B525 router",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohsenie/HuaweiB525Router",
    packages=setuptools.find_packages(),
    install_requires=[
        'pycryptodome>=3.9.6',
        'IPy>=1.0.0',
        'requests>=2.22.0',
        'six>=1.14.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
    ],
    python_requires='>=3.6',
)