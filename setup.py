from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.rst').read()

setup(name="dtool-cli",
      packages=["dtool_cli"],
      version=version,
      description="Data management command line interface: dtool.",
      long_description=readme,
      include_package_data=True,
      author="Tjelvar Olsson",
      author_email="tjelvar.olsson@jic.ac.uk",
      url=url,
      install_requires=[],
      download_url="{}/tarball/{}".format(url, version),
      license="MIT")