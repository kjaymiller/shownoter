from distutils.core import setup

setup(name='data_py',
    version='1.0',
    py_modules=['data_py'],
    install_requires = [
        "beautifulsoup4",
        "Flask",
        "Flask-WTF",
        "itsdangerous",
        "Jinja2",
        "Markdown",
        "MarkupSafe",
        "py",
        "pymongo",
        "requests",
        "six",
        "Werkzeug",
        "wheel",
        "WTForms"
    ]
)
