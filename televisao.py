class Televisao:
    def __init__(obj, min=2, max=14):
        obj.ligada = False
        obj.canal = min
        obj.canal_minimo = min
        obj.canal_maximo = max

    def muda_canal_para_baixo(obj):
        if (obj.canal - 1 >= obj.canal_minimo):
            obj.canal -= 1
        else:
            obj.canal = obj.canal_maximo

    def muda_canal_para_cima(obj):
        if (obj.canal + 1 <= obj.canal_maximo):
            obj.canal += 1
        else:
            obj.canal = obj.canal_minimo


tv1 = Televisao(min=1, max=50)  # <--
tv1.muda_canal_para_baixo()
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)

tv2 = Televisao(min=2, max=20)  # <--
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_cima()
print(tv2.canal)
