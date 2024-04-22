seg = input("Número de segundos que deseja converter: ")
total_seg = int(seg)

horas = total_seg // 3600
seg_rest = total_seg % 3600
min = seg_rest // 60
seg_rest_f = seg_rest % 60

print(horas, "horas, ", min, "minutos e", seg_rest_f, "segundos.")