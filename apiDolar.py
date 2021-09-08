import requests

url='https://api.apis.net.pe/v1/tipo-cambio-sunat'
precio=requests.get(url)
datos=precio.json()
precio_dolar_compra=float(datos['compra'])
precio_dolar_venta=float(datos['venta'])
print("precios compra: {} venta: {}".format(precio_dolar_compra,precio_dolar_venta))
print("precio compra: ",precio_dolar_compra,"precio venta:  ",precio_dolar_venta)