from setuptools import setup


setup(name='Grid2Kpi',
      version='0.1.0',
      description='Toto',
      long_description='Tata',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Natural Language :: English"
      ],
    #   keywords='ML powergrid optmization RL power-systems',
    #   author='Benjamin DONNOT',
    #   author_email='benjamin.donnot@rte-france.com',
    #   url="https://github.com/rte-france/Grid2Op",
      license='MPL',
      packages=['grid2kpi'],
      include_package_data=True,
      install_requires=["numpy", "pandas", "pandapower", "Grid2Op", "plotly"],
      zip_safe=False)
