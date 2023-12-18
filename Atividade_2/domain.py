from tkinter import *
from gui import *
from bd import *

def fillTextBoxShowAlbumsWithBD(bd, text_box, window_main):
    foundAlbums = set() 
    count = 1
    if isBDEmpty():
        warningWindow(window_main, 'NO ALBUMS TO SHOW!')
    else:
        for(album, name, year, is_release) in zip(bd['album'], bd['name'],bd['year'],bd['is_release']):
            if album not in foundAlbums:
                if count == 1:
                    text_box.insert(END, f'Albums list: \n\n')
                    text_box.insert(END, f'=================================================\n\n')
                    count+=1
                text_box.insert(END, f'Name of the album: {album}\n')
                text_box.insert(END, f'Name of the singer: {name}\n')
                text_box.insert(END, f'Year of the album: {year}\n')
                text_box.insert(END, f'Is Release? {is_release}\n')
                text_box.insert(END, '=================================================\n') 

                foundAlbums.add(album)

def lookByPeriods(event):
    global windowByDetails
    windowByDetails = Toplevel()
    
    global varRadioAndCombo
    
    varRadioAndCombo = byDetails(event, windowByDetails, showByDetails)
    
    windowByDetails.mainloop()

def filterByDetails(bd, window_main, text_box):
    entryPeriod = varRadioAndCombo[0].get()
    entryYear = varRadioAndCombo[1].get()
    entryYear = int(entryYear)
    found_albums_by_period = {} 
    current_period = None

    for (album, name, year, is_release) in zip(bd['album'], bd['name'], bd['year'], bd['is_release']):
        year = int(year)
        
        if entryPeriod == 'Option 1':
            if year < entryYear:
                if year not in found_albums_by_period:
                    found_albums_by_period[year] = set()

                if album not in found_albums_by_period[year]:
                    if current_period != year:
                        if current_period is not None:
                            text_box.insert(END, '\n')
                        text_box.insert(END, f'Albums released before {year}\n\n')
                        current_period = year

                    text_box.insert(END, f'Name of the album: {album}\n')
                    text_box.insert(END, f'Name of the singer: {name}\n')
                    text_box.insert(END, f'Year of the album: {year}\n')
                    text_box.insert(END, f'Is Release? {is_release}\n')

                    found_albums_by_period[year].add(album)

        elif entryPeriod == 'Option 2':
            if year > entryYear:
                if year not in found_albums_by_period:
                    found_albums_by_period[year] = set()

                if album not in found_albums_by_period[year]:
                    if current_period != year:
                        if current_period is not None:
                            text_box.insert(END, '\n')
                        text_box.insert(END, f'Albums released after {year}\n\n')
                        current_period = year

                    text_box.insert(END, f'Name of the album: {album}\n')
                    text_box.insert(END, f'Name of the singer: {name}\n')
                    text_box.insert(END, f'Year of the album: {year}\n')
                    text_box.insert(END, f'Is Release? {is_release}\n')

                    found_albums_by_period[year].add(album)

        elif entryPeriod == 'Option 3':
            if year == entryYear:
                if year not in found_albums_by_period:
                    found_albums_by_period[year] = set()

                if album not in found_albums_by_period[year]:
                    if current_period != year:
                        if current_period is not None:
                            text_box.insert(END, '\n')
                        text_box.insert(END, f'Albums released in {year}\n\n')
                        current_period = year

                    text_box.insert(END, f'Name of the album: {album}\n')
                    text_box.insert(END, f'Name of the singer: {name}\n')
                    text_box.insert(END, f'Year of the album: {year}\n')
                    text_box.insert(END, f'Is Release? {is_release}\n')

                    found_albums_by_period[year].add(album)

def showAlbums(event):
    window_main, text = windowAlbums()

    infos = readBD()

    fillTextBoxShowAlbumsWithBD(infos, text, window_main)

    window_main.mainloop()

def filterByArtist(bd, window_main, text_box):
    entry_artist = entryByArtist.get().upper()
    found_albums_by_artist = {}
    current_artist = None

    for (album, name, year, is_release) in zip(bd['album'], bd['name'],bd['year'],bd['is_release']):
        if entry_artist == '':
            warningWindow('YOU DIDN\'T WRITE ANY NAME!', window_main)
        if entry_artist in name.upper():
            if name not in found_albums_by_artist:
                found_albums_by_artist[name] = set()

            if album not in found_albums_by_artist[name]:
                if current_artist != name:
                    if current_artist is not None:
                        text_box.insert(END, '\n')  # Adiciona uma quebra de linha antes da próxima mensagem
                    text_box.insert(END, f'{name}\'s found album(s)\n\n')
                    current_artist = name

                text_box.insert(END, f'Name of the album: {album}\n')
                text_box.insert(END, f'Year of the album: {year}\n')
                text_box.insert(END, f'Is Release? {is_release}\n')

                found_albums_by_artist[name].add(album)

def showByDetails(event):
    window_show_by_details, text_box = windowShowByDetails()

    infos = readBD()

    if isBDEmpty():
        warningWindow('NO ALBUMS TO SHOW!', window_show_by_details)
    else:
        filterByDetails(infos, window_show_by_details, text_box)

    window_show_by_details.mainloop()

def showByArtist(event):
    window_show_by_artist, text_box = windowShowByArtist()

    infos = readBD()
    
    if isBDEmpty():
        warningWindow('YOU DIDN\'T WRITE ANY NAME!', window_show_by_artist)
    else:
        filterByArtist(infos, window_show_by_artist, text_box)

    window_show_by_artist.mainloop()

def sendInfo():
    processData(entries[0], entries[1], entries[2], entries[3])

def isEntriesAllTyped(event):
    entryName, entryYear = entries[1], entries[2]
    if not entryYear.isdigit():
        return False
    if entryName.isdigit():
        return False 
    return True
         
def getInfo(event):
    global entries
    entries = collectInfo(event) 
    if entries:
        if isEntriesAllTyped(entries):
            sendInfo()
            sucessWindow(event)
        else:
            warningWindow('INCORRECT ENTRY!')
    else:
        windowNoEntryDetected()

def SearchByArtist(event):
    global entryByArtist
    entryByArtist = byArtist(event, showByArtist)

if __name__ == '__main__':
    windowMain = Tk()
    dictFunctions = {
        'sendFunction':getInfo,
        'showAlbums':showAlbums,
        'SearchByArtist':SearchByArtist,
        'look':lookByPeriods,
        'clear':clear, 
    }

    buildMainScreen(windowMain, dictFunctions)
    windowMain.mainloop()
