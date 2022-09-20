import os
import wifi_credentials
import ip


# Class which is describes name, state of device (on or off) and if the traffic transmission is active. This class also
# contains functions for google_dns and host ping.
class NetworkInterface:
    def __init__(self, name, isactive, traffic_transmission):
        self.name = name
        self.isactive = isactive
        self.traffic_transmission = traffic_transmission

    @classmethod
    def google_response(cls):
        return os.system("ping -c 60 " + ip.google_dns)

    @classmethod
    def host_response(cls):
        return os.system("ping -c 60 " + ip.host)


# objects of the class (wi-fi and lte) and its initial state
wifi = NetworkInterface("wlan1", True, True)
lte = NetworkInterface("eth3", False, False)

# if host is available
if wifi.host_response() == 0:
    wifi.traffic_transmission = True
elif wifi.host_response() != 0:
    if lte.google_response() == 0 and wifi.host_response() != 0:
        lte.isactive = True
        lte.traffic_transmission = True
        wifi.traffic_transmission = False
    else:
        lte.traffic_transmission = False
        lte.isactive = False
        wifi.traffic_transmission = True

# Система автоматически определеяет доступные каналы передачи данных lte | wifi по критериям:
#
#    1) if wifi.host_response() == 0, то - wifi.traffic_transmission = True
#    (если хост пингуется через wifi, то на интерфейсе включается передача трафика)
#    2) if wifi.host_response() != 0, то lte.isactive = True, lte.traffic_transmission = True,
#    while lte.google_response() == 0 and wifi.host_response() != 0 (если хост не пингуется через wifi, то включается
#    lte, начинается передача трафика через lte до тех пор, пока пингуется google_dns через lte или пока пингуется host
#    через wifi)
#    3) если нет доступа к ресурсам host | google_dns по одному из покдлючений соответственно в течение минуты,
#    то происходят попеременные попытки переключения по кругу между каналами
#
# Ограничения и допущения в задании:
# - место хранения настроек беспроводного сетевого подключения (логина\пароля к сети wi-fi) - в файловой системе
# на модуле, может быть определено в любом месте исполнителем тестового задания
# - считать, что SIM-карта всегда есть в устройстве и не требуется ввод пин кода
# - допустима ситуация, когда подняты одновременно оба сетевых интерфейса, когда поднят только один из них
# - ситуацию, когда оба интерфейса недоступны, считать неверным поведением системы
# - приоритетным для передачи данных из двух активных каналов является wi-fi
# Задание:
# Написать тест дизайн для проверки данной функциональности в виде шагов и ожидаемых результатов.
# Автоматизировать наиболее критичные описанные тесты с использованием pytest.
