from tkinter import *
from tkinter.ttk import Combobox
filename = 'arquivo.txt'

def write(albumNameWrite, singerNameWrite, yearAlbum, isRelease):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(albumNameWrite + '|' + singerNameWrite + '|' + yearAlbum + '|' + isRelease + '\n')
    
def processData(albumName, singerName, yearAlbum, isRelease):
    write(albumName, singerName, yearAlbum, isRelease)

def showAlbums(event):

    windowInfo = Toplevel()
    windowInfo.title('Registered albums')
    windowInfo.geometry('600x400')

    scrollbar = Scrollbar(windowInfo, orient=VERTICAL)
    scrollbar.grid(row=0, column=1, rowspan=4, sticky=N+S)

    text_box = Text(windowInfo, yscrollcommand=scrollbar.set, wrap=WORD)
    text_box.grid(row=0, column=0, rowspan=4)

    scrollbar.config(command=text_box.yview)

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) == 0:
            windowAlert = Toplevel()
            windowAlert.title('Warning')
            windowAlert.geometry('250x200')
            labelWarning = Label(windowAlert, text='NO ALBUMS TO SHOW!')
            labelWarning.pack(expand=True, fill='both')
            windowInfo.destroy()
            windowAlert.mainloop()  

        foundAlbums = set() 
        count = 1
        for line in lines:
            if line.strip(): # Evitar que linha em branco seja lida
                album, name, year, is_release = line.split('|')
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

    windowInfo.mainloop()

def numberValidation():
    try:
        float(yearAlbum)
        return True
    except: 
        return False
def clickedButton(event):
    albumName = entryAlbumName.get().upper().strip()
    global singerName, yearAlbum
    singerName = entrySingerName.get().upper().strip()
    yearAlbum = entryYearAlbum.get().upper().strip()
    isRelease = v0.get().upper().strip()
    if albumName == '' or singerName == '' or yearAlbum == '' or isRelease != 'YES' and isRelease != 'NO':
        windowNoEntryDetected = Toplevel()
        windowNoEntryDetected.title('ADVICE')
        windowNoEntryDetected.geometry('250x200')
        labelWarning = Label(windowNoEntryDetected, text='MISSING ENTRY!')
        labelWarning.pack(expand=True, fill='both')
        windowNoEntryDetected.mainloop() 
    else:
        if numberValidation():
            processData(albumName, singerName, yearAlbum, isRelease)
            windowSuccessfulSegistration = Toplevel()
            windowSuccessfulSegistration.title('SUCCESSFUL REGISTRATION')
            windowSuccessfulSegistration.geometry('250x200')
            labelSuccessfulSegistration = Label(windowSuccessfulSegistration, text='ALBUM REGISTERED SUCCESSFULLY!')        
            labelSuccessfulSegistration.configure(fg='green', font=('Helvetica', 9))
            labelSuccessfulSegistration.pack(expand=True, fill='both')
            windowSuccessfulSegistration.mainloop()
        else:
            windowNoNumberEntry = Toplevel()
            windowNoNumberEntry.title('ADVICE')
            windowNoNumberEntry.geometry('250x200')
            labelWarning = Label(windowNoNumberEntry, text='ALBUM YEAR NEEDS TO BE A NUMBER!')
            labelWarning.pack(expand=True, fill='both')
            windowNoNumberEntry.mainloop()
        
def showWindowRadionAndComboOption(event):
    global windowShowResultsRadionAndCombo
    windowShowResultsRadionAndCombo = Toplevel()
    windowShowResultsRadionAndCombo.title('Results by Radio and Combo')

    scrollbar = Scrollbar(windowShowResultsRadionAndCombo, orient=VERTICAL)
    scrollbar.grid(row=0, column=1, rowspan=4, sticky=N+S)

    text_box = Text(windowShowResultsRadionAndCombo, yscrollcommand=scrollbar.set, wrap=WORD)
    text_box.grid(row=0, column=0, rowspan=4)

    scrollbar.config(command=text_box.yview)

    radioSelected = varRadioOption.get()
    comboSelected = varComboOption.get()
    foundAlbums = set()
    

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                album, name, year, isrelease = line.split('|')

                if album not in foundAlbums:                         
                    if radioSelected == "Option 1" and int(year) <= int(comboSelected):
                        showByRadionAndCombo(text_box, album, name, year, isrelease)
                    elif radioSelected == "Option 2" and int(year) >= int(comboSelected):
                        showByRadionAndCombo(text_box, album, name, year, isrelease)
                    elif radioSelected == "Option 3" and int(year) == int(comboSelected):
                        showByRadionAndCombo(text_box, album, name, year, isrelease)
                    foundAlbums.add(album)

def showByRadionAndCombo(text_box, album, name, year, isrelease):
    text_box.insert(END, f'Name of the album: {album}\n')
    text_box.insert(END, f'Name of the singer: {name}\n')
    text_box.insert(END, f'Year of the album: {year}\n')
    text_box.insert(END, f'Is Release? {isrelease}\n')
    text_box.insert(END, '\n')

def searchAlbumByOption(event):
    global windowRadionAndCombo
    windowRadionAndCombo = Toplevel()
    windowRadionAndCombo.title('Search by Selection')

    global varRadioOption, varComboOption
    varRadioOption = StringVar()
    varComboOption = StringVar()

    r3 = Radiobutton(windowRadionAndCombo, text="Anterior a", variable=varRadioOption, value='Option 1')
    r4 = Radiobutton(windowRadionAndCombo, text="Posterior a", variable=varRadioOption, value='Option 2')
    r5 = Radiobutton(windowRadionAndCombo, text="Igual a", variable=varRadioOption, value='Option 3')
    r3.grid(row=1, padx=10, pady=3, column=0, sticky='nswe', columnspan=1)
    r4.grid(row=2, padx=10, pady=3, column=0, sticky='nswe', columnspan=1)
    r5.grid(row=3, padx=10, pady=3, column=0, sticky='nswe', columnspan=1)

    data = ("2010", "2015", "2020", "2023")
    cb = Combobox(windowRadionAndCombo, values=data, textvariable=varComboOption)
    cb.grid(row=1, padx=10, pady=3, column=1, sticky='nswe', columnspan=2)
    cb.set("Selecione uma opção")

    btnByRadionAndCombo = Button(windowRadionAndCombo, text='Search')
    btnByRadionAndCombo.grid(row=4, padx=10, pady=10, column=0, sticky='nswe', columnspan=4)
    btnByRadionAndCombo.bind('<Button-1>', showWindowRadionAndComboOption)


def byArtist(event):
    windowTest = Toplevel()
    windowTest.title('Albums by artist')
    labelInfo = Label(windowTest, text='Enter the artist name:')
    labelInfo.grid(row=1, padx=20, pady=20, column=0, sticky='nswe', columnspan=3)
    global entryByArtist
    entryByArtist = Entry(windowTest)
    entryByArtist.grid(row=2, padx=20, pady=20, column=0, sticky='nswe', columnspan=3)

    btnTestArtist = Button(windowTest ,text='Look for artist')
    btnTestArtist.grid(row=3, padx=20, pady=20, column=0, sticky='nswe', columnspan=3)
    btnTestArtist.bind('<Button-1>', showByArtist)

def clear(event):
    entryAlbumName.delete(0, END)
    entrySingerName.delete(0, END)
    entryYearAlbum.delete(0, END)

def showByArtist(event):
    windowShowByArtist = Toplevel()
    windowShowByArtist.title('Albums by artist')
    windowShowByArtist.geometry('600x400')

    text_box = Text(windowShowByArtist)
    text_box.pack()

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) == 0:
            windowWarning = Toplevel()
            windowWarning.title('WARNING')
            windowWarning.geometry('250x200')
            labelWarning = Label(windowWarning, text='NO ALBUMS TO SHOW!')
            labelWarning.pack(expand=True, fill='both')
            windowShowByArtist.destroy()
            windowWarning.mainloop()

        entry_artist = entryByArtist.get().upper()
        found_albums_by_artist = {}
        current_artist = None

        for line in lines:
            if line.strip():
                album, name, year, is_release = line.split('|')
                if entry_artist == '':
                    windowWarning = Toplevel()
                    windowWarning.title('Warning')
                    windowWarning.geometry('250x200')
                    labelWarning = Label(windowWarning, text='YOU DIDN\'T WRITE ANY NAME!')
                    labelWarning.pack(expand=True, fill='both')
                    windowShowByArtist.destroy()
                    windowWarning.mainloop()

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

    windowShowByArtist.mainloop()

windowMain = Tk()
windowMain.title('Register album')

labelMainRegisterAlbum = Label(text='ALBUM RECORDER')
labelMainRegisterAlbum.grid(row=0, column=0, padx=10, pady=10, sticky='nswe',  columnspan=3)

labelAlbumName = Label(text='Album name: ')
labelAlbumName.grid(row=1, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
entryAlbumName = Entry(windowMain)
entryAlbumName.grid(row=1, padx=10, pady=10, column=1, sticky='nswe', columnspan=3)

labelSingerName = Label(text='Singer\'s name: ')
labelSingerName.grid(row=2, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
entrySingerName = Entry(windowMain)
entrySingerName.grid(row=2, padx=10, pady=10, column=1, sticky='nswe', columnspan=2)

labelYearAlbum = Label(text='Album year: ')
labelYearAlbum.grid(row=3, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
entryYearAlbum = Entry(windowMain)
entryYearAlbum.grid(row=3, padx=10, pady=10, column=1, sticky='nswe', columnspan=2)

v0=StringVar()
v0.set('1')
labelNewAlbum = Label(windowMain,text='Album release? ' )
labelNewAlbum.grid(row=4, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
labelNewAlbum.configure(font=("Helvetica", 9))
r1=Radiobutton(windowMain, text="Yes", variable=v0, value='YES')
r2=Radiobutton(windowMain, text="No", variable=v0, value='NO')
r1.grid(row=4, padx=10, pady=10, column=2, sticky='nswe', columnspan=1)
r2.grid(row=4, padx=10, pady=10, column=1, sticky='nswe', columnspan=1)

mainBtn = Button(text='Send')
mainBtn.grid(row=8, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
mainBtn.bind('<Button-1>', clickedButton)

btnShowAlbums = Button(text='Show Albums')
btnShowAlbums.grid(row=9, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
btnShowAlbums.bind('<Button-1>', showAlbums)

btnShowByArtist = Button(text='Search by Artist')
btnShowByArtist.grid(row=10, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
btnShowByArtist.bind('<Button-1>', byArtist)

btnSearchByRadionAndCombo = Button(text='Look for details by period and year')
btnSearchByRadionAndCombo.grid(row=11, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
btnSearchByRadionAndCombo.bind('<Button-1>', searchAlbumByOption)

btnClear = Button(text='Clear')
btnClear.grid(row=12, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
btnClear.bind('<Button-1>', clear)

windowMain.mainloop()
