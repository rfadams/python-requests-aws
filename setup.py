from distutils.core import setup

version = '0.1'

setup(name='awsrequests',
      version=version,
      description='A port of reqests.py that includes AWS Authentication.',
      author='Robert Adams',
      author_email='rfadams@gmail.com',
      url='https://github.com/rfadams/python-requests-aws',
      packages=['awsrequests'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
