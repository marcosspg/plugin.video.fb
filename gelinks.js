var lndata = "Última actualización: "+new Date().toLocaleString("es")+"\n"


var added = []
document.querySelectorAll("div[class='b-c'] a").forEach(
    (link)=>{
        if (link.href.includes("acestream://") && !link.innerHTML.includes("<") && !added.includes(link.innerHTML)) {
            lndata+= multiBTOA(link.innerHTML)+"|"+multiBTOA(link.href)+"\n"
            added.push(link.innerHTML)
        }
    }
)


function multiBTOA(text) {
    for (let i = 0; i < 10; i++) {
        text = btoa(text)
    }
    return text
}



function downloadFile(data, filename) {
    var file = new Blob([data], {type: "text/plain"});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);  
        }, 0); 
    }
}




downloadFile(lndata, "lndata.txt")