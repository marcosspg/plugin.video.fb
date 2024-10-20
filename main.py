import os
import xbmcaddon
import sys
from urllib.parse import urlparse, parse_qs
import xbmcgui
import xbmcplugin
import actions
import tools
import logger 

__url__ = sys.argv[0]
__handle__ = int(sys.argv[1])

args = parse_qs(sys.argv[2][1:]);

action = args.get('action', None);

if action != None:
    action = action[0];

#Acciones    
if action == None:
    tools.addItemMenu("Enlaces", os.path.join(tools.get_runtime_path(),"resources","buttons","list.png"), tools.build_url({"action":"listaEnlaces"}),isFolder=True);
elif action == "listaEnlaces":
    actions.getEnlaces();
# elif action == "verNovela":
#     url = args.get('url', None)[0];
#     actions.getCapitulos(url);
# elif action == "verCapitulo":
#     url = args.get('url', None)[0];
#     actions.verCapitulo(url);
# elif action=="buscar":
#     actions.buscar();
xbmcplugin.endOfDirectory(__handle__)
