import requests
if __name__ == '__name__':
    url='http://httpbin.org/get'
    response = requests.get(url)
    #print(response)

    if response.status_code == 200:
        #print(response.content)
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
   

'''if __name__ == '__name__':
    url='http://httpbin.org/get'
    response= requests.get(url)
    if response.status_code == 200:
        content=response.content
        print(content) '''
    

        
        