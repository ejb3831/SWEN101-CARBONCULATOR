
function readFile(key){
    
    var doc1;
    var out = {};
    fs.readFile('DB.txt', 'utf-8', (err, data) => { 
        if (err) throw err; 
        doc1+=data;
    })
    var lineSplt = doc1.split("\n");
    for(x in lineSplt){
        var up = x.split(",");
        out[atob(bytes.toString(CryptoJS.AES.decrypt(up[0],key)))] = atob(bytes.toString(CryptoJS.AES.decrypt(up[1],key)));
    }
    return(out);
}
function writeFile(text,key){
    var bs = "";
    for(k in text){
        bs.concat(CryptoJS.AES.encrypt(btoa(k)), key);
        bs.concat(",");
        bs.concat(CryptoJS.AES.encrypt(btoa(text[k])), key);
        bs.concat("\n");
    }
    fs.writeFile('DB.txt', bs);

}