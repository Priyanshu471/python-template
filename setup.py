from setuptools import find_packages,setup

setup(
    name='GLbot',
    version='0.0.1',
    author='Priyanshu Mishra',
    author_email='cs20169@glbitm.ac.in',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)