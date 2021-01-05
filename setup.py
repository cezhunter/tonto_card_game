from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tonto",
    version="1.0.0",
    author="Cezanne Vahid",
    author_email="cezannevahid@gmail.com",
    description="Tonto's Card Game package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cezhunter/tonto_card_game",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'tonto = tonto.run:entry',
        ],
    },
    python_requires='>=3.6')