import json

json_inventario="C:\Users\heprado\Documents\Github\Cisco\Studies\heprado\inventario.json"

def open_json(arquivo):

    with open(arquivo,'+') as arquivo_aberto:
        
        parseado=json.dumps(arquivo_aberto)
        
return parseado


        



