from setuptools import setup, find_packages


setup(name='Grid2Kpi',
      version='0.1.0-rc3',
      description='Grid2Kpi',
      long_description='Grid2Kpi',
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
      license='MPL',
      packages=['grid2kpi', 'grid2kpi.episode'],
      include_package_data=True,
      install_requires=["numpy", "pandas", "pandapower", "Grid2Op", "plotly"],
      zip_safe=False)
