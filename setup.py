from setuptools import setup, find_packages

setup(
    name='qmds',
    version="0.0.1",
    description="Qommands: execute shell pipelines against multiple inputs, diff/compare/join results",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=open("requirements.txt").read(),
    entry_points={
        'console_scripts': [
            'diff-x = qmds.diff_x:main',
            'comm-x = qmds.comm_x:main',
            'git-diff-x = qmds.git_diff_x:main',
        ],
    },
    license="MIT",
    author="Ryan Williams",
    author_email="ryan@runsascoded.com",
    author_url="https://github.com/ryan-williams",
    url="https://github.com/runsascoded/qmds",
)
