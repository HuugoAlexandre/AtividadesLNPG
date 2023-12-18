from tkinter import *
from tkinter.ttk import Combobox

# Warning Window
def warningWindow(text, windowInfo=None):
    windowAlert = Toplevel()
    windowAlert.title('Warning')
    windowAlert.geometry('250x200')
    labelWarning = Label(windowAlert, text=text)
    labelWarning.pack(expand=True, fill='both')
    if windowInfo is not None:
        windowInfo.destroy()
    windowAlert.mainloop()

def windowNoEntryDetected():
    warning_no_entry = Toplevel()
    warning_no_entry.title('Warning')
    warning_no_entry.geometry('250x200')
    labelWarning = Label(warning_no_entry, text='NO ENTRY!')
    labelWarning.pack(expand=True, fill='both')
    warning_no_entry.mainloop()

def windowInvalidEntryDetected(): 
    warning_no_entry = Toplevel()
    warning_no_entry.title('Warning')
    warning_no_entry.geometry('250x200')
    labelWarning = Label(warning_no_entry, text='INCORRECT ENTRY!')
    labelWarning.pack(expand=True, fill='both')
    warning_no_entry.mainloop()

# Construtor de Show Artist
def windowShowByArtist():
    windows_show_by_artist = Toplevel()
    windows_show_by_artist.title('Albums by artist')
    windows_show_by_artist.geometry('600x400')

    text_box = Text(windows_show_by_artist)
    text_box.pack()

    return (windows_show_by_artist, text_box)


def isEntryInfo():
    if entryAlbumName.get() == '' or entrySingerName.get() == '' or entryYearAlbum.get() == '' or v0.get() != 'YES' and v0.get() != 'NO':
        return False
    else:
        return True

def collectInfo(event):
    if isEntryInfo():
        entryAlbum = entryAlbumName.get().upper()
        entrySinger = entrySingerName.get().upper()
        entryYear = entryYearAlbum.get().upper()
        entryOption = v0.get().upper()
        
        return (entryAlbum, entrySinger, entryYear, entryOption)
     
def byArtist(event, showByArtist):
    windowTest = Toplevel()
    windowTest.title('Albums by artist')
    labelInfo = Label(windowTest, text='Enter the artist name:')
    labelInfo.grid(row=1, padx=20, pady=20, column=0, sticky='nswe', columnspan=3)

    entryByArtist = Entry(windowTest)
    entryByArtist.grid(row=2, padx=20, pady=20, column=0, sticky='nswe', columnspan=3)

    btnTestArtist = Button(windowTest ,text='Look for artist')
    btnTestArtist.grid(row=3, padx=20, pady=20, column=0, sticky='nswe', columnspan=3)
    btnTestArtist.bind('<Button-1>', showByArtist)

    return entryByArtist

def windowShowByDetails():
    window_show_by_details = Toplevel()
    window_show_by_details.title('Albums by period and year')
    window_show_by_details.geometry('600x400')

    text_box = Text(window_show_by_details)
    text_box.pack()

    return (window_show_by_details, text_box)

# Construtor de Show Albuns
def windowAlbums():
    windowInfo = Toplevel()
    windowInfo.title('Registered albums')
    windowInfo.geometry('600x400')

    scrollbar = Scrollbar(windowInfo, orient=VERTICAL)
    scrollbar.grid(row=0, column=1, rowspan=4, sticky=N+S)

    text_box = Text(windowInfo, yscrollcommand=scrollbar.set, wrap=WORD)
    text_box.grid(row=0, column=0, rowspan=4)

    scrollbar.config(command=text_box.yview)
    
    return (windowInfo, text_box)

def byDetails(event, windowByDetails, showByDetails):
    windowByDetails.title('Search by Selection')

    global varRadioOption, varComboOption
    varRadioOption = StringVar()
    varComboOption = StringVar()

    r3 = Radiobutton(windowByDetails, text="Anterior a", variable=varRadioOption, value='Option 1')
    r4 = Radiobutton(windowByDetails, text="Posterior a", variable=varRadioOption, value='Option 2')
    r5 = Radiobutton(windowByDetails, text="Igual a", variable=varRadioOption, value='Option 3')
    r3.grid(row=1, padx=10, pady=3, column=0, sticky='nswe', columnspan=1)
    r4.grid(row=2, padx=10, pady=3, column=0, sticky='nswe', columnspan=1)
    r5.grid(row=3, padx=10, pady=3, column=0, sticky='nswe', columnspan=1)

    data = ("2010", "2015", "2020", "2023")
    cb = Combobox(windowByDetails, values=data, textvariable=varComboOption)
    cb.grid(row=1, padx=10, pady=3, column=1, sticky='nswe', columnspan=2)
    cb.set("Selecione uma opção")

    btnByRadionAndCombo = Button(windowByDetails, text='Search')
    btnByRadionAndCombo.grid(row=4, padx=10, pady=10, column=0, sticky='nswe', columnspan=4)
    btnByRadionAndCombo.bind('<Button-1>', showByDetails)
    
    varRadioAndCombo = (varRadioOption, varComboOption)
    
    return varRadioAndCombo

def clear(event):
    entryAlbumName.delete(0, END)
    entrySingerName.delete(0, END)
    entryYearAlbum.delete(0, END)
    v0.set(None)

def buildMainScreen(windowMain, buttonsFunctions):
    
    windowMain.title('Register album')
    global entryAlbumName, entrySingerName, entryYearAlbum, v0
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
    mainBtn.bind('<Button-1>', buttonsFunctions['sendFunction'])

    btnShowAlbums = Button(text='Show Albums')
    btnShowAlbums.grid(row=9, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
    btnShowAlbums.bind('<Button-1>', buttonsFunctions['showAlbums'])

    btnShowByArtist = Button(text='Search by Artist')
    btnShowByArtist.grid(row=10, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
    btnShowByArtist.bind('<Button-1>', buttonsFunctions['SearchByArtist'])

    btnSearchByRadionAndCombo = Button(text='Look for details by period and year')
    btnSearchByRadionAndCombo.grid(row=11, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
    btnSearchByRadionAndCombo.bind('<Button-1>', buttonsFunctions['look'])

    btnClear = Button(text='Clear')
    btnClear.grid(row=12, padx=10, pady=10, column=0, sticky='nswe', columnspan=3)
    btnClear.bind('<Button-1>', buttonsFunctions['clear'])



    

