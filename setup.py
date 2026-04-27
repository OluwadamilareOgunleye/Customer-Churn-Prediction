import os

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models",
    "app"
]

files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "notebooks/churn_analysis.ipynb",
    "src/data_preprocessing.py",
    "src/train_model.py",
    "src/evaluate_model.py",
    "app/app.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, 'w') as f:
        pass

print("Project structure created successfully!")