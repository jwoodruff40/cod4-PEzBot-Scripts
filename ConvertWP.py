mapName = input("Enter mapname\n(do not include the 'mp_' or '_waypoints' prefix/suffix)\n:")
fullMapName ='mp_'+mapName+'_waypoints.gsc'

#Converts mapname_waypoints.gsc file (old style PEzBot format) to newer mapname.gsc file (new style Bot Warfare format)
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
newWPFile.close()