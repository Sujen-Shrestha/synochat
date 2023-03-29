from distutils.core import setup
setup(
  name = 'chatsyno',
  packages = ['chatsyno'],
  version = '1.0.0',
  license='MIT',
  description = 'Automating synology using selenium',
  author = 'knightmare',
  author_email = 'kneel.stha@gmail.com',
  url = 'https://github.com/knightmare-sujen/synochat',
  download_url = 'https://github.com/knightmare-sujen/synochat',
  install_requires=[
          'selenium',
          'webdriver_manager'
      ],
  classifiers=[ 
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
