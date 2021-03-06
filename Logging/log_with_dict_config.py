import logging
import logging.config




def main():

    dictLogConfig = {
        'version':1,
        'handlers': {
            'fileHandler':{
                'class': 'logging.FileHandler',
                'formatter':'myFormatter',
                'filename': 'config2.log'
            }
        },
        'loggers': {
            'exampleApp':{
                'handlers': ['fileHandler'],
                'level':'INFO',
            }
        },
        'formatters': {
            'myFormatter': {
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }   
        }
    }

    logging.config.dictConfig(dictLogConfig)

    logger = logging.getLogger('exampleApp')
    logger.info('Program Started')
    logger.info('DONE!')


if __name__ == '__main__':
    main()