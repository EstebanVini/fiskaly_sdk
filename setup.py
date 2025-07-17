from setuptools import setup, find_packages
import os

# Path seguro para README
readme_path = "README.md" if os.path.exists("README.md") else "docs/README.md"

setup(
    name='fiskaly-sdk-sign-es',
    version='0.1.0',
    description='SDK oficial para la integración con la API Fiskaly SIGN ES',
    author='Esteban Viniegra Pérez Olagaray',
    author_email='esteban@eviniegra.software',
    url='https://github.com/tuusuario/fiskaly-sdk-sign-es',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'pydantic>=2.0.0'
    ],
    python_requires='>=3.7',
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
    ],
    long_description=open(readme_path, encoding="utf-8").read(),
    long_description_content_type="text/markdown"
)
