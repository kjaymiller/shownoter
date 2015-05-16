notes = {}

def get_notes(file):
    with open(file,'r') as f:
        key = ''
        for line in f:
            if line.startswith('>'):                
                if '#' in line:
                    val = line[1:line.find(' #')].strip()
                    key = line[line.find('#'):].strip()
                    print(key, val)
                    notes[key] = notes.get(key, [val])
                    if not val in notes[key]:
                        notes[key].append(val) 
                else:
                    val = line[1:line.find(' #')].strip()
                    notes[key] = notes.get(key, [val])
                    if not val in notes[key]:
                        notes[key].append(val)

filename = input('Name of File: ') + '.txt'
get_notes(filename)
print(notes)
                
        
