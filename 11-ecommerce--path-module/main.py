from pathlib import Path

# Absolute path - c:\Program Files\Microsoft
# Relative path - curr folder

path = Path("ecommerce")
email = Path("email")

print(path.exists())
print(email.mkdir())
print(email.rmdir())

print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)