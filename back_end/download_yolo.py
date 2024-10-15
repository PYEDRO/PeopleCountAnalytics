import urllib.request

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)
    print(f"{filename} downloaded.")

# URLs dos arquivos de configuração e pesos
cfg_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg"
weights_url = "https://pjreddie.com/media/files/yolov3.weights"

# Nomes dos arquivos
cfg_file = "yolov3.cfg"
weights_file = "yolov3.weights"

# Baixar os arquivos
download_file(cfg_url, cfg_file)
download_file(weights_url, weights_file)
