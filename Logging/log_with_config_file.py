import logging
import logging.config


def main():

    logging.config.fileConfig('loggersettings.conf')
    logger = logging.getLogger('exampleApp')

    logger.info('Program started')
    logger.info('Done!')


if __name__ == '__main__':
    main()