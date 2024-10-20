import logger
import re
import requests;
from bs4 import BeautifulSoup
import tools
import xbmc

host = "zonevipz.com";
urlNovelasActuales = "https://"+host+"/?op=categories_all&per_page=60&page=";

capitulosVistos = list(tools.getCapitulosVistos());


def getNovelas(pagina):
    if pagina == None or pagina == "0":
        pagina = 1;
    try:
        pagina = int(pagina);
    except:
        pagina = 1;
    with requests.Session() as s:
        response = s.get(urlNovelasActuales+str(pagina));
        #logger.debug(response.text);
        # with open(__file__.replace("actions.py", "test.html").replace("\\", "/"), "w", encoding="utf-8") as out:
        #     out.write(response.text);
        #     out.close();
        for novela in BeautifulSoup(response.content, "html.parser").find_all("div",attrs={"class":"video-post clearfix"}):
            titulo = novela.find("a").find("p").text;
            url = str(novela.find("a")["href"]);
            portada = str(novela.find("a").find("div", attrs={"class":"thumb"})["style"]).replace(")", "").replace("background-image:url(","");
            tools.addItemMenu(titulo, portada, tools.build_url({"action":"verNovela", "url":url}), isFolder=True);
        tools.addItemMenu("Página "+str(pagina+1), None, tools.build_url({"action":"listaNovelas", "pagina": str(pagina+1)}), isFolder=True);
        s.close();

def getEnlaces():
    



def verCapitulo(url):
    with requests.Session() as s:
        response = s.get(url);
        urlVideo = re.findall("sources: \[{src: \".*v.mp4", response.text)[0].replace("sources: [{src: \"", "")
        #tools.play_video("Ver online", urlVideo);
        tools.addItemMenu("Ver online", "", urlVideo, "true", isVideo=True)
        tools.marcarVisto(url);
        s.close();
