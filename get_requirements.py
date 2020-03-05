def get_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f]
