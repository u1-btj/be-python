def luas_segitiga(a, t):
    return round((a * t) / 2, 2)

def param_segitiga():
    inp_a = round(float(input('Masukkan luas alas: ')), 2)
    inp_t = round(float(input('Masukkan tinggi: ')), 2)
    return [inp_a, inp_t]