from volume.bola import param_bola, volume_bola
from volume.kubik import param_kubik, volume_kubik
from volume.silinder import param_silinder, volume_silinder
from luas.segitiga import param_segitiga, luas_segitiga
from luas.lingkaran import param_lingkaran, luas_lingkaran
from luas.persegi import param_persegi, luas_persegi

class Output:
    def __init__(self, tipe, bentuk, param, result):
        self.tipe = tipe
        self.bentuk = bentuk
        self.param = param
        self.result = result
    
    def display(self):
        print(f'{self.tipe.capitalize()} {self.bentuk.capitalize()} dengan {self.make_param_to_text()} adalah {self.result}')
    
    # convert param into unique text based on bentuk
    def make_param_to_text(self):
        if self.bentuk == 'lingkaran' or self.bentuk == 'bola':
            return f'panjang jari - jari {self.param}'
        elif self.bentuk == 'kubus' or self.bentuk == 'persegi':
            return f'panjang sisi {self.param}'
        elif self.bentuk == 'segitiga':
            return f'luas alas {self.param[0]} dan tinggi {self.param[1]}'
        elif self.bentuk == 'silinder':
            return f'panjang jari - jari {self.param[0]} dan tinggi {self.param[1]}'

# decorator to handle error tipe
def handle_error_tipe(func):
    def check_tipe(*tipe):
        if tipe[0] not in ['luas', 'volume']:
            print('Jenis perhitungan tidak tersedia!')
            return
        else:
            return func(*tipe)
    return check_tipe

# decorator to handle error bentuk
def handle_error_bentuk(func):
    def check_bentuk(**data_bentuk):
        if data_bentuk['bentuk'] not in data_bentuk['opsi']:
            print('Bentuk tidak tersedia pada opsi bentuk')
            return 0, 0
        else:
            return func(**data_bentuk)
    return check_bentuk

@handle_error_tipe
def pilih_tipe(tipe):
    if tipe == 'luas':
        bentuk = ['lingkaran', 'persegi', 'segitiga']
    elif tipe == 'volume':
        bentuk = ['bola', 'silinder', 'kubus']
    return bentuk

@handle_error_bentuk
def pilih_bentuk(**data_bentuk):
    param = 0
    result = 0
    if data_bentuk['bentuk'] == 'bola':
        param = param_bola()
        result = volume_bola(param)
    elif data_bentuk['bentuk'] == 'kubus':
        param = param_kubik()
        result = volume_kubik(param)
    elif data_bentuk['bentuk'] == 'silinder':
        param = param_silinder()
        result = volume_silinder(param[0], param[1])
    elif data_bentuk['bentuk'] == 'segitiga':
        param = param_segitiga()
        result = luas_segitiga(param[0], param[1])
    elif data_bentuk['bentuk'] == 'lingkaran':
        param = param_lingkaran()
        result = luas_lingkaran(param)
    elif data_bentuk['bentuk'] == 'persegi':
        param = param_persegi()
        result = luas_persegi(param)
    return param, result

if __name__ == "__main__":
    inp_tipe = str(input('Pilihlah Jenis Perhitungan (luas, volume): ')).lower()
    opsi_bentuk = pilih_tipe(inp_tipe)
    if opsi_bentuk:
        print('Opsi Bentuk >>', str(opsi_bentuk))
        bentuk = str(input('Pilihlah Jenis Bentuk: ')).lower()
        param, result = pilih_bentuk(opsi=opsi_bentuk, bentuk=bentuk)
        if param != 0 and result != 0:
            output = Output(inp_tipe, bentuk, param, result)
            output.display()