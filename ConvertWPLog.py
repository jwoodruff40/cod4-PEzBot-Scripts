import os, zipfile
#from contextlib import contextmanager

mapName =input('\nEnter map name (omitting the mp_ prefix): ').lower()
fullMapName ='mp_'+mapName

def main():
    #Converts latest set of waypoint coordinates for the given map in the games_mp.log file to a properly formatted mapname.gsc waypoint file
    print('\nReading games_mp.log...')
    log =open('games_mp.log','r')
    wpLines =log.readlines()
    log.close()
    lineNum =0
    lineNum2 =0
    for i,j in enumerate(wpLines):
        if fullMapName+'()' in j:
            lineNum =i+1
        if '}' in j:
            lineNum2 =i+1
    if lineNum !=0:
        print('\nGenerating new %s.gsc waypoint file...' % mapName.capitalize())
        wpLines =wpLines[lineNum:lineNum2]
        wpLinesNew =[]
        for i,line in enumerate(wpLines):
            if i ==0 or i ==(len(wpLines)-1):
                wpLinesNew.append(line)
            elif '*/' in line:
                pos =line.find('*/')
                wpLinesNew.append('    '+line[(pos+2):])
            else:
                wpLinesNew.append('    '+line)
        newMapName =mapName.capitalize()+'.gsc'
        if not os.path.exists('bots/waypoints'):
            os.makedirs('bots/waypoints')
        newWPFile =open('bots/waypoints/%s' % newMapName,'w')
        newWPFile.write(mapName.capitalize()+'()\n')
        for i in wpLinesNew:
            newWPFile.write(i)
        newWPFile.close()
        input('New waypoint file successfully generated!\nPress [Enter] to continue...')    
    else:
        print('\n%s not found in games_mp.log!' % mapName)    
    if checkPresenceFuncs():
        convertFuncs()
    else:
        input('\nbots_funcs.gsc not found in current directory.\nPress [Enter] to attempt to extract from archive...')
        with zipfile.ZipFile('z_svr_bots.iwd') as botsZip:
            botsZip.extractall()
        if checkPresenceFuncs():
            print('\nbots_funcs.gsc successfully extracted from z_svr_bots.iwd\nChecking for map case...')
            convertFuncs()
        else:
            print('Failed to extract bots_funcs.gsc from z_svr_bots.iwd. Please make sure the script is being run from the main mod directory.\nPress [Enter] to close...')
    zipGSCs(newMapName)
def generateFuncs(lines,check,pos):
    #writes a new bots_funcs.gsc if necessary to add a load case for the given map
    newFuncs =open('bots/bots_funcs.gsc','w')
    for i,line in enumerate(lines):
        if check !=1 and i ==pos+2:
            newFuncs.write('        case "'+fullMapName+'":\n            level.waypoints = bots\waypoints\\'+mapName.capitalize()+'::'+mapName.capitalize()+'();\n        break;\n    }')
        else:
            newFuncs.write(line)
    newFuncs.close()
    return
def checkPresenceFuncs():
    #checks for the presence of the bots_funcs.gsc file in uncompressed form
    if os.path.isfile('bots/bots_funcs.gsc') ==True:
        return(True)
    else:
        return(False)
def convertFuncs():
    #checks for a load case in the bots_funcs.gsc for the given map and calls the script generation function if necessary
    funcs =open('bots/bots_funcs.gsc','r')
    mapLines =funcs.readlines()
    funcs.close()
    for i,line in enumerate(mapLines):
        if mapName.capitalize()+'();' in line:
            lineNum =1
        elif 'level.waypoints = bots\waypoints\\' in line:
            lineNum2 =i
    if lineNum ==1:
        input('\n%s is already present in bots_funcs.gsc!\nAborting operation...\nPress [Enter] to continue...' % fullMapName)
    else:
        os.remove('bots/bots_funcs.gsc')    
        print('Adding '+fullMapName+' to bots_funcs.gsc...')
        generateFuncs(mapLines,lineNum,lineNum2)
        input('\n'+fullMapName+' successfully added to bots_funcs.gsc\nPress [Enter] to close')
def zipGSCs(wpFilename):
    botsZip =zipfile.ZipFile('z_svr_bots.iwd', mode='r')
    files =botsZip.namelist()
    print('\nZipping files into z_svr_bots.iwd...')
    with zipfile.ZipFile('z_svr_bots.iwd', mode='w') as botsZip:
        for path in files:
            botsZip.write(path)
    input('New z_svr_bots.iwd archive successfully created!\nPress [Enter] to close.')
main()