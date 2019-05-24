def get_requirements():
    with open('lint.txt') as f:
        return [line.strip() for line in f]
