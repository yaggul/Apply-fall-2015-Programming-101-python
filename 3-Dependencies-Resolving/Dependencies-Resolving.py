

'''
dep={'dependencies': ['backbone'], 'projectName': 'Test0000'}
'''

'''
pack={'backbone': ['jQuery', 'underscore'],
 'jQuery': ['queryJ'],
 'lodash': [],
 'queryJ': [],
 'underscore': ['lodash']}
'''


'''
Installing backbone.
In order to install backbone, we need jQuery and underscore.
Installing jQuery.
In order to install jQuery, we need queryJ.
Installing queryJ.
Installing underscore.
In order to install underscore, we need lodash. Lodash is already installed.
All done.
'''

import os
import json
import platform


try:
    os.chdir('packages')
except:
    os.mkdir('./packages')
    os.chdir('./packages')

try:
    for i in os.listdir('./installed_modules'):
        os.removedirs('./installed_modules/{}'.format(i))
except:
    pass

try:
    os.mkdir('./installed_modules')
except:
    pass


try:
    os.mkdir('./installed_modules/lodash')
except:
    pass

dep={'dependencies': ['backbone'], 'projectName': 'Test0000'}
pack={'backbone': ['jQuery', 'underscore'],
 'jQuery': ['queryJ'],
 'lodash': [],
 'queryJ': [],
 'underscore': ['lodash']}

try:
    with open('dependencies.json','w') as f:
        json.dump(dep, f)
except:
    pass

try:
    with open('all_packages.json','w') as f1:
        json.dump(pack, f1)
except:
    pass

del dep
del pack

with open('./all_packages.json','r') as f1:
    pack=json.load(f1)

with open('./dependencies.json','r') as f2:
    dep=json.load(f2)

inModules=[]
inModules+=os.listdir('./installed_modules')

def installing(app,deptree,inModules):
    #Debugging statements
    '''
    print('\n')
    print('app: ',app)
    print('deptree[app]: ',deptree[app])
    print('x in modules: ', [x in inModules for x in deptree[app]])
    print('inModules: ', inModules)
    print('\n')
    '''
    if deptree[app]==[]:
        print('Installing {}.'.format(app))
        inModules.append(app)
        os.mkdir('./installed_modules/{}'.format(app))
    elif deptree[app]!=[]:
        if {x in inModules for x in deptree[app]}=={True}:
            print('In order to install {} we need to install {}. {} is already installed.'.format(app,' and '.join(deptree[app][:]),' and '.join(deptree[app][:]).capitalize()))
            inModules.append(app)
            os.mkdir('./installed_modules/{}'.format(app))
        else:
            print('Installing {}.'.format(app))
            print('In order to install {}, we need {}.'.format(app,' and '.join(deptree[app][:])))
            for i in deptree[app]:
                installing(i,deptree,inModules)
    else:
        print('ERROR')
    if app not in inModules:
        inModules.append(app)
        os.mkdir('./installed_modules/{}'.format(app))



for app in dep['dependencies']:
   installing(app, pack,inModules)
print('All done.')
if platform.system()=='Windows':
    os.system('tree /F')
elif platform.system()=='Linux':
    try:
        os.system('tree')
    except:
        print('"tree" not installed')
else:
    print('Platform not supported for tree command')
#installing('backbone', pack, inModules)

