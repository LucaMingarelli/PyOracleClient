import setuptools, pyoracleclient

with open("README.md", "r") as f:
    long_description = f.read()

package_data = ['../pyoracleclient/res/*',
                '../pyoracleclient/instantclient/*',
                '../pyoracleclient/instantclient/instantclient/*',
                '../pyoracleclient/instantclient/instantclient/network/*',
                '../pyoracleclient/instantclient/instantclient/network/admin/*']

setuptools.setup(
    name="PyOracleClient",
    version=pyoracleclient.__version__,
    author=pyoracleclient.__author__,
    author_email=pyoracleclient.__email__,
    description=pyoracleclient.__about__,
    url=pyoracleclient.__url__,
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'': package_data},
    # install_requires=['cx_oracle'],
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    python_requires='>=3.6',
)