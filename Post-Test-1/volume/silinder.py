def volume_silinder(r, t):
    return round(3.14 * r * r * t, 2)

def param_silinder():
    inp_r = round(float(input('Masukkan jari - jari: ')), 2)
    inp_t = round(float(input('Masukkan tinggi: ')), 2)
    return [inp_r, inp_t]