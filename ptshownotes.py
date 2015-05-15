def get_notes(file):
    with open(file,'r') as f:
        new_file = ''
        for line in f:
            if line.strip() and not line.startswith('#'):
                new_line = line.split('-', 1)
                new_file += ('* [{}]({})\n'.format(new_line[0],new_line[1].strip()))
            else:
                new_file += line
        return(new_file)
filename = input('Name of File: ')+'.txt'
with open('submission-{}'.format(filename), 'w') as f:
    f.write(get_notes(filename))
