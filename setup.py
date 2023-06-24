from setuptools import setup, find_packages

setup(
    name='vulmonsahil',
    version='1.0.0',
    description='A Python library for scraping vulnerability information from Vulmon',
    author='Sahil Gaikwad',
    author_email='sahil.gaikwad@zerothreat.in',
    License='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=[
    "vulmon",
    "vulnerability",
    "security",
    "scraper",
    "CVE",
    "common vulnerabilities and exposures",
    "vulnerability analysis",
    "exploits",
    "GitHub links",
    "reference links",
    "security researchers",
    "information retrieval",
    "web scraping",
    "data scraping",
    "vulnerability assessment",
    "CVSSv3",
    ]
)
