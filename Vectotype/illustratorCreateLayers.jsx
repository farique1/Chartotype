// Ilustrator script add named layers
// Author unknown

var line,lay,myLayers = [];  
var layersList = File(File.openDialog("Open layers name list"));
layersList.open( 'r' );   
while(!layersList.eof){  
    line = layersList.readln();  
    myLayers.push(line);  
}  
layersList.close();   
var doc = app.activeDocument;  
for(var i = myLayers.length - 1; i > 0; i--){  
    lay = doc.layers.add();  
    lay.name = myLayers[i];  
}