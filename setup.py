import os
from setuptools import setup, find_packages


#Functions to create the folder structure
def create_project_structure():
    
    #Defining the folder structures
    structure = {
        'app' : {
            '__init__.py': '',
            'main.py': '#Fastapi app entry point',
            'api': {
                '__init__.py':'',
                'routes': {
                    '__init__.py':'',
                    'auth.py': '# authentication routes (login, logout)',
                    'trades.py': '#Trading-related routes',
                    'users.py': '# User management routes',
                },
                'dependencies.py': '# Dependency injection and resuable dependencies',
            },
            'data': {
                '__init__.py':'',
                'data_loader.py': '#Load data from sources (eg ., APIs CSVs)',
                'preprocessing.py': '# Data Processing functions',
                'features.py': '# Features engineering functions',
            },
            'models': {
                '__init__.py': '',
                'trading_model.py': '#Trading stretegy/model definitions',
                'user_model.py':'#user model for authentication and management',
                'model_training.py':'#Model training and evalution scripts',
            },
            'services': {
                '__init__.py': '',
                'trading_service.py':'#Business logic for trading operations',
                'user_service.py':'#Business logic for user management',
            },
            'schemas': {
                '__init__.py':'',
                'trading_schema.py': '# Schemas for trading-related data',
                'user_schema.py': '#shemas for user data',
            },
            'tasks': {
                '__init__.py': '',
                'trading_tasks.py': '#scheduled trading tasks',
            },
            'config.py': '#configuration settings',
            'utils': {
                '__init__.py': '',
                'utils.py': '# Utility functions',
            },
        },
        'tests': {
            '__init__.py': '',
            'test_main.py': '# Tests for FastAPI app',
            'test_routes.py':'# Tests for API routes',
            'test_services.py':'# Tests for service layers',
            'test_models.py':'#Tests for models and database interactions',
            'test_utils.py':'#Tests for utility functions',
        },
        'requirements.txt': '# Python dependencies',
        'ReadME.md': '# project documentation',
        '.env': '#enviorment varibles',
        'Dockerfile': '#Dockerfile for containerization',
        'docker-compose.yml': '#Docker compose file for local development',
        '.gitignore':'#files to ignore in git',
    }
    
    # Function to create directories and files
    def create_structure(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict): # if it's directory
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, 'w') as f:
                    f.write(content)
    
    create_structure(os.getcwd(), structure)
    
# call the function
create_project_structure()

setup(
    name='entropy-trade-bot',
    version='0.1.0',
    description='A crypto trading bot SaaS project built with FastAPI and data science techniques.',
    author='Harshal Honde',
    author_email='Harshalhonde50@gmail.com',
    url='https://github.com/Harry262000/entropy-trade-bot',  # Update with your repository URL
    packages=find_packages(where='app'),  # This will find packages in the app directory
    package_dir={'': 'app'},  # Tells setuptools to look for packages in the app folder
    install_requires=[
        'fastapi',
        'uvicorn',
        'pandas',
        'numpy',
        'scikit-learn',
        'requests',
        'pydantic',
        
    ],
    entry_points={
        'console_scripts': [
            'run-app=main:app.run',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  
)