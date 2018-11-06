# ------- Журналирование (логгирование) с использованием модуля logging -------
#            Вынесение настройки логгирования в отдельный модуль


import logging

import log_config

# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
log = logging.getLogger('app.main')

def main():
    ''' Тестовая главная функция
    '''
    # logger.debug('Старт приложения')
    log.debug('There will be debug information')
    log.info('Hello, World!')
    log.warning('It seems to be a bug...')
    log.critical('Critical bug in app! Hello, World!')

if __name__ == '__main__':
    main()    