mapName =input('\nEnter map name(s) (omitting the mp_ prefix)\nSeparate map names with comma\n:').lower()
mapNameList =mapName.split(',')

def convertWPFile(mapName):
    #Converts mapname_waypoints.gsc file (old style PEzBot format) to newer mapname.gsc file (new style Bot Warfare format)
    fullMapName ='mp_'+mapName+'_waypoints.gsc'
    waypoints = open(fullMapName,'r')
    wpLines =waypoints.readlines()
    waypoints.close()
    wpLinesNew =[]
    temp =0
    for i,j in enumerate(wpLines):
        if i >31:
            if 'level.' in j:
                #if ('waypoints['+str(temp+1)+']') in j and 'size' not in j:
                #wpLinesNew.append('waypoints['+str(temp)+'].use = true;')
                #temp +=1
                wpLinesNew.append('    '+j[10:])
    wpLinesNew.append('return waypoints;\n}')
    newMapName =mapName.capitalize()+'.gsc'
    newWPFile =open(newMapName,'w')
    newWPFile.write(mapName.capitalize()+'()\n{\n    waypoints = [];\n')
    for i in wpLinesNew:
        if 'waypointCount' not in i:
            newWPFile.write('    '+i.strip()+'\n')
    print('\n%s.gsc successfully converted' %mapName)
    newWPFile.close()
    
for name in mapNameList:
    convertWPFile(name.strip())
