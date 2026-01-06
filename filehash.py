from pathlib import Path

p = Path('.')
dirs = [x for x in p.iterdir() if x.is_dir()]
listed =list(p.glob('**/*.py'))
print(listed)