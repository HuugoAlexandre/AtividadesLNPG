filename = 'arquivo.txt'

def write(albumNameWrite, singerNameWrite, yearAlbum, isRelease):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(albumNameWrite + '|' + singerNameWrite + '|' + yearAlbum + '|' + isRelease + '\n')
    
def processData(albumName, singerName, yearAlbum, isRelease):
    write(albumName, singerName, yearAlbum, isRelease)

def isBDEmpty():
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) == 0:
            return True
        else:
            return False

def readBD(): 
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        dictBD = {'album':[], 'name':[], 'year':[], 'is_release':[]}      
        for line in lines:
            if line.strip():  
                arrBD = line.split('|')
                dictBD['album'].append(arrBD[0])
                dictBD['name'].append(arrBD[1])
                dictBD['year'].append(arrBD[2])
                dictBD['is_release'].append(arrBD[3])
                
    return dictBD
