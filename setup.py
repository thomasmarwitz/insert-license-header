from setuptools import find_packages, setup

setup(
    name="pre-commit-hooks",
    description="Some out-of-the-box hooks for pre-commit",
    url="https://github.com/Lucas-C/pre-commit-hooks",
    use_scm_version=True,
    platforms="linux",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages("."),
    install_requires=[
        "rapidfuzz",
    ],
    entry_points={
        "console_scripts": [
            "insert_license = pre_commit_insert_qc_license.insert_license:main",
        ],
    },
)
