from setuptools import setup, find_packages

# Lire le contenu de README.md pour la longue description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='EducTools',
    version='0.1',
    packages=find_packages(),
    description='Outils d\'apprentissage pour étudiants.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='éducation apprentissage mathématiques outils',
    author='Nom de l\'Auteur',
    author_email='auteur@example.com',
    url='https://github.com/auteur/packagev2',
    license='MIT',
    install_requires=[
    'numpy'],
    entry_points={
        'console_scripts': [
            'math=eductools.math_tools_cli:calcul_cli',
        ],
    },
)
