from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="serp-intelligence",
    version="1.0.0",
    author="SERPChecker.fyi",
    author_email="info@serpchecker.fyi",
    description="SERP Intelligence is a research focused framework for analyzing search results, search intent, ranking patterns, competitor visibility, SERP features, and content opportunities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://serpchecker.fyi",
    project_urls={
        "Homepage": "https://serpchecker.fyi",
        "GitHub": "https://github.com/Serpchecker-fyi/serp-intelligence",
        "Documentation": "https://serp-intelligence.readthedocs.io",
        "PyPI": "https://pypi.org/project/serp-intelligence",
    },
    py_modules=["serp_intelligence"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    keywords=[
        "serp-intelligence",
        "serp-analysis",
        "search-intent",
        "ranking-patterns",
        "competitor-visibility",
        "serp-features",
        "content-opportunities",
        "seo-research",
        "organic-search",
        "serpchecker",
    ],
    entry_points={
        "console_scripts": [
            "serp-intel=serp_intelligence:main",
        ],
    },
)
