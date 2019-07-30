"""
Translation rules
Copyright 2019
"""
def translateName(rawname):
    '''
    A general purpose name expander.
    '''
    suffixlookup = {
    'Ave':'Avenue',
    'Rd':'Road',
    'St':'Street',
    'Pl':'Place',
    'Cres':'Crescent',
    'Blvd':'Boulevard',
    'Dr':'Drive',
    'Lane':'Lane',
    'Crt':'Court',
    'Gr':'Grove',
    'Cl':'Close',
    'Rwy':'Railway',
    'Div':'Diversion',
    'Hwy':'Highway',
    'Hwy':'Highway',
    'Conn': 'Connector',
    'E':'East',
    'S':'South',
    'N':'North',
    'W':'West',
    'SE':'Southeast',
    'NE':'Northeast',
    'SW':'Southwest',
    'NW':'Northwest'}

    newName = ''
    for partName in rawname.split():
        newName = newName + ' ' + suffixlookup.get(partName,partName)
    
    return newName

def filterTags(attrs):
    if not attrs:
        return

    tags = {}
    if 'ADDR_NUM' in attrs and attrs['ADDR_NUM'] != '':
        tags['addr:housenumber'] = attrs['ADDR_NUM']
    if 'UNIT' in attrs and attrs['UNIT'] != '':
        tags['addr:unit'] = attrs['UNIT']
    if 'FULLNAME' in attrs and attrs['FULLNAME'] != '':
        tags['addr:street'] = attrs['FULLNAME']
    if 'CTYNAME' in attrs and attrs['CTYNAME'] != '':
        tags['addr:city'] = attrs['CTYNAME']
    if 'ZIP5' in attrs and attrs['ZIP5'] != '':
        tags['addr:postcode'] = attrs['ZIP5']

    return tags
