import configparser

def create_configfile(path):
    """
    create confgi file for the logger
    """

    config = configparser.ConfigParser()
    
    #loggers section
    config.add_section("loggers")
    config.set('loggers', 'keys', value='root')

    #handlers section
    config.add_section("handlers")
    config.set('handlers', 'keys', value='fileHandler')


    #formatter section
    config.add_section("formatters")
    config.set('formatters', 'keys', value='myFormatter')

    #logger_root
    config.add_section("logger_root")
    config.set('logger_root', 'level', value='CRITICAL')
    config.set('logger_root', 'handlers', value='consoleHandler')

    #logger_exampleApp section
    config.add_section("logger_exampleApp")
    config.set('logger_exampleApp', 'level', value='INFO')
    config.set('logger_exampleApp', 'handlers', value='fileHandler')
    config.set('logger_exampleApp', 'qualname', value='exampleApp')

    #handler_consoleHandler section
    config.add_section("handler_consoleHandler")
    config.set('handler_consoleHandler', 'class', value='StreamHandler')
    config.set('handler_consoleHandler', 'level', value='DEBUG')
    config.set('handler_consoleHandler', 'formatter', value='myFormatter')
    config.set('handler_consoleHandler', 'args', value='(sys.stdout,)')

    #handler_fileHandler section
    config.add_section("handler_fileHandler")
    config.set('handler_fileHandler', 'class', value='FileHandler')
    config.set('handler_fileHandler', 'formatter', value='myFormatter')
    config.set('handler_fileHandler', 'args', value='("config.log",)')

    #formatter_myFormatter section
    config.add_section("formatter_myFormatter")
    config.set('formatter_myFormatter', 'format', value='root')
    #config.set('formatter_myFormatter', 'format', value='root')