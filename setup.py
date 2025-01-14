from setuptools import find_packages, setup

setup(
    name="Video Tools",
    version="0.1",
    packages=find_packages(),
    install_requires=["Click", 'colorama;sys_platform=="win32"'],
    classifiers=["Programming Language :: Python :: 3"],
    license="MIT",
    entry_points={"console_scripts": ["video_tools=video_tools.__main__:cli"]},
)
