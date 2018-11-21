'''
mplement a group_by_owners function that:

    Accepts a dictionary containing the file owner name for each file name.
    Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
'''


class FileOwners:

    @staticmethod
    def group_by_owners(files):
        res = {}
        for file, owner in files.items():
            if owner not in res:
                res[owner] = [file]
            else:
                res[owner].append(file)
            # As a try/except clause
            #try:
            #   res[owner].append(file)
            #except KeyError:
            #   res[owner] = [file]
        return res

# Dunno if this solution is any better than the other two up there but its different
# Either way a defaultdict seems appropriate for this problem too
def group_by_owners(files):
    res = {owner: [] for owner in set(files.values())}
    for file in files:
        res[files.get(file)].append(file)

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
