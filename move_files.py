"""Loop over generated .pyi (stub) files, get path to respective .py file,
then run merge-pyi to add type hints as comments."""
import os
import subprocess

for f in os.listdir('stubs'):
    print('merging:', f)
    split_filename = f.split('.')

    # create new path if necessary
    match_dir = split_filename[:-2]
    if match_dir:
        match_dir = os.path.join(*match_dir)
        os.makedirs(match_dir, exist_ok=True)

    py_path = split_filename[-2] + '.py'
    if match_dir:
        matching_file = os.path.join(match_dir, py_path)
    #print('to:', match_file_path)
    #os.rename(os.path.join('stubs', f), match_file_path)

    stub_file = os.path.join('stubs', f)
    commands = ["merge-pyi", "-i", "--as-comments", matching_file, stub_file]
    out = subprocess.run(commands, stdout=subprocess.PIPE).stdout
    print(out)
