import os
import json
import logging
from pathlib import Path

logger = logging.getLogger(__file__)

class FileManager(object):

    @classmethod
    def read_json(cls, file_path):
        logger.info("Reading file: %s" % file_path)
        file_data = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content:
                    file_data = json.loads(content)
                    logger.info("File read done with contents: %s" % str(file_data))
                else:
                    logger.warning("No file data")
        except Exception as exp:
            logger.warning("Exception: %s" % str(exp))
        return file_data