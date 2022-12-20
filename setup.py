from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mat_addon/__init__.py
from mat_addon import __version__ as version

setup(
	name="mat_addon",
	version=version,
	description="Mat Addon",
	author="Hidayatali",
	author_email="hidayatmanusiya1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)