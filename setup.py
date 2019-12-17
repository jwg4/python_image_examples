from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Image-Examples',
    version='0.1.0',
    url='http://github.com/jwg4/python_image_examples',
    author='Jack Grahl',
    maintainer='Jack Grahl',
    maintainer_email='jack.grahl@gmail.com',
    description='Image processing examples',
    long_description=readme(),
    packages=['image_examples'],
    package_data={'image_examples': ['data/usc_misc']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite='tests',
)