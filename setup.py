import setuptools


setuptools.setup(
    name='django-pariah',
    version='0.1',
    packages=['pariah',],
    install_requires=[
        'django>1.2',
        'PIL'
    ],
    author='Paul Hummer @ Amelia, LLC',
    author_email='paul@ameliaknows.com',
    url='https://github.com/rockstar/django-pariah',
    license='http://www.opensource.org/licenses/mit-license.php',
    description='A Django app for creating web comics',
    keywords='django comics webcomics',
    include_package_data=True,
)
