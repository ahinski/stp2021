from pyowm import OWM
from pyowm.commons.enums import SubscriptionTypeEnum
from pyowm.utils.config import get_default_config

config = {
    'subscription_type': SubscriptionTypeEnum.FREE,
    'language': 'ru',
    'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
    },
    'proxies': {
        'http': 'http://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
}
owm = OWM('be079bb2c4d5e135ab9e60710f217c1b',config)

place = input('В каком городе ты сейчас??? ')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')['temp']

print('В городе ', place, ' сейчас ', w.detailed_status)

if temp < 10:
    print('Меньше десяти градусов, очень холодно!')
elif temp < 25:
    print('Температура норм')
else:
    print('Жара')