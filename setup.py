from setuptools import setup

setup(name='pdfmerge',
      version='0.1',
      packages=['pdfmerge'],
      entry_points={
          'console_scripts': ['pdfmerge = pdfmerge.__main__:main']
      },
      install_requires=['PyPDF2']
      )