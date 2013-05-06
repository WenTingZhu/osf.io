import os, random, string

def moduleDirs(modules_dir):
    modules_dir = modules_dir.replace('/', '')
    return [f for f in os.listdir(modules_dir) if os.path.isdir(os.path.join(modules_dir, f))]

def getDirectories(directory):
    if not isinstance(directory, list):
        directory = [directory]
    res = []
    for i in directory:
        for root, dirs, files in os.walk(i):
            res.append(os.path.join(os.getcwd(), str(root)))
    return res

def randomString(length=8, chars=string.letters+string.digits):
    return ''.join([chars[random.randint(0, len(chars)-1)] for i in range(length)])

def importFiles(modules_dir, required_file):
    module_dirs = moduleDirs(modules_dir)
    entryModules = {}
    for d in module_dirs:
        file_to_import = os.path.join(modules_dir, d, required_file)
        if os.path.exists(file_to_import):
            entryModules[d] = __import__(modules_dir + '.' + d + '.' + string.replace(required_file, '.py', ''))
    return entryModules
