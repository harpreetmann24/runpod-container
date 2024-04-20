import importlib.metadata

# List of packages you want to include in your requirements.txt
packages = [
    "transformers", "evaluate", "wandb", "datasets", "accelerate", "peft",
    "bitsandbytes", "trl", "huggingface_hub", "lm-eval", "deepspeed",
    "sentencepiece", "scipy", "scikit-learn", "protobuf", "python-dotenv",
    "numpy", "pandas", "seaborn", "matplotlib", "pathlib"
]

# Create a requirements.txt file with package versions
with open("requirements.txt", "w") as f:
    for package in packages:
        try:
            # Use importlib.metadata to get the version of the package
            version = importlib.metadata.version(package)
            f.write(f"{package}=={version}\n")
        except importlib.metadata.PackageNotFoundError:
            # If a package is not found, write a warning to the output
            print(f"Warning: {package} not found in the installed packages.")

