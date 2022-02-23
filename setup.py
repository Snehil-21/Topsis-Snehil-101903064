from distutils.core import setup
setup(
  name = 'Topsis-Snehil-101903064',         # How you named your package folder (MyLib)
  packages = ['Topsis-Snehil-101903064'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implements Topsis for the given datafile and returns topsis score and rank.',   # Give a short description about your library
  author = 'Snehil Gupta',                   # Type in your name
  author_email = 'sgupta2_be19@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/Snehil-21/Topsis-Snehil-101903064',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Snehil-21/Topsis-Snehil-101903064/archive/refs/tags/v_02.tar.gz',    # I explain this later on
  keywords = ['Topsis', 'Rank Ordering', 'Data Science'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
