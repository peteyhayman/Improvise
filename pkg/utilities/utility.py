import json


def OpenJson(path):
    file = open(path, 'r')
    txt = file.read()
    uniJsn = json.loads(txt)
    pyJsn = parseType(uniJsn)
    # print uniJsn
    # print pyJsn
    file.close()
    return pyJsn


def OpenTextLines(path):
    file = open(path, 'r')
    text = file.read()
    text.replace('\r', '')  # remove dos line endings
    lines = text.split('\n')
    return lines


def parseType(val):
    if isinstance(val, unicode):
        newVal = val.encode('ascii', 'ignore')
        return parseString(newVal)
    elif isinstance(val, str):
        return parseString(val)
    elif isinstance(val, dict):
        return parseUnicodeDict(val)
    elif isinstance(val, list):
        return parseUnicodeList(val)
    elif (val == None
            or isinstance(val, int)
            or isinstance(val, bool)
            or isinstance(val, float)):
        return val
    print '\n\n unknown type', '\n', type(val), '\n', val
    return val


def parseUnicodeDict(dict):
    res = {}
    for key, value in dict.iteritems():
        key = parseType(key)
        res[key] = parseType(value)
    return res


def parseUnicodeList(lst):
    res = []
    for item in lst:
        res.append(parseType(item))
    return res


def parseString(val):
    try:
        iVal = int(val)
        return iVal
    except ValueError:
        pass
    try:
        fVal = float(val)
        return fVal
    except ValueError:
        pass
    if val == 'true'or val == 'True':
        return True
    elif val == 'false' or val == 'False':
        return False
    else:
        return val


def GetMimeType(path):
    splitPath = path.split('.')
    lastIndex = len(splitPath)-1
    extension = splitPath[lastIndex]
    if extension == 'html':
        return 'text/html'
    elif extension == 'js':
        return 'text/javascript'
    elif extension == 'css':
        return 'text/css'
    elif extension == 'ico':
        return 'image/x-icon'
    else:
        print 'unknown extension', extension
        return 'text'
# 'r' = read, 'w' = write, 'a' = append, 'r+' = read and write
