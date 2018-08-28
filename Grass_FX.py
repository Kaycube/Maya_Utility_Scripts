import maya.cmds as cmds

cmds.turbulence(n='Grass_wind_FX', m=20, pos=(0,0,0), att=0.0, f=1, mxd=0, nsl=8)
x = 1
lat = 1

for i in range(109):
    cmds.select('grass_grass'+str(i)) #select object
    cmds.polyUnite(muv=1, n='grass'+str(i)) #Combine and rename
    cmds.delete(ch=True)
    cmds.select('grass'+str(i)) #slect new shape
    
    ################################ Create FX ########################### 
    cmds.lattice(dv=(7,7,7), oc=True)
    cmds.select("ffd" +str(x)+"Lattice")
    cmds.duplicate(n="ffd" +str(x)+"Lattice_goal")
    cmds.select("ffd" +str(x)+"Base")
    cmds.duplicate(n="ffd" +str(x)+"Base_goal")
    
    cmds.select("ffd" +str(x)+"Lattice")
    cmds.soft("ffd" +str(x)+"Lattice", c=True)
    cmds.goal("ffd"+str(x)+"LatticeParticle", g="ffd" +str(x)+"Lattice_goal", w=0.5)
    cmds.connectDynamic("ffd"+str(x)+"LatticeParticle", f='Grass_wind_FX')
    cmds.select('grass'+str(i), "ffd" +str(x)+"Lattice", "ffd" +str(x)+"Base", "ffd" +str(x)+"Lattice_goal", "ffd" +str(x)+"Base1", "ffd" +str(x)+"Base_goal")
    cmds.group(n='Dynamic_grass'+str(i))
    
    x += 2 #increment

l = 1
for i in range(109):
    cmds.select("ffd" +str(l)+"Lattice", "ffd" +str(l)+"Lattice_goal", "ffd" +str(l)+"Base1", "ffd" +str(l)+"Base_goal")
    cmds.hide(cs = True)
    l += 2
print "DONE!!!"    