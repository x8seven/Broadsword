import os
import gc
import asyncio
import logging
import logging.config
import signal
import yaml
from logging.handlers import RotatingFileHandler
from datetime import datetime
from discord.ext import commands
from config import config
from lib.utils import BasicUtils
from lib.db import DBStart

gc.enable() # Not sure that this working..

main_modules = {
    "modules.admin",
    "modules.test",
    "modules.queues",
    "modules.userdb",
}

logging.config.dictConfig(yaml.load(open('config/logging.yaml', 'r')))
log = logging.getLogger("broadsword")

broadsword = commands.Bot(command_prefix=config.bot["prefix"])

def run_bot():
    try:
        cnx = DBStart()
        mysql_version = cnx.mysql_version()
        #stored_db_version = cnx.storage_get("db_version")
        #db_version = BasicUtils.db_version()
        #if stored_db_version is None:
        #    cnx.storage_add("db_version", db_version)
        #    stored_db_version = db_version
        #else:
            # There should be an update of the database
        #    if stored_db_version["storedValue"] < db_version:
        #        print("Database update required")
        #        return
    except Exception as e:
        log.info("MySQL DB is not available! BroadswordBot will not be started!")
        if config.bot["devMode"]:
            print(e)
            print("MySQL DB is not available! BroadswordBot will not be started!")
        return
    finally:
        del cnx
    
    try:
        cnx = DBStart()
        cnx.message_check()
        log.info("Message queue was checked.")
        if config.bot["devMode"]:
            print("Message queue was checked.")
    except Exception as e:
        log.exception("An exception has occurred in {}: ".format(__name__))
        print(e)
    finally:
        del cnx
    
    log.info("Connecting...")
    if config.bot["devMode"]:
        print("Connecting...")

    @broadsword.event
    async def on_ready():
        """A function that is called when the client is
        done preparing data received from Discord.
        """

        log.info("Broadsword is logged in..")
        log.info("Username: {}".format(broadsword.user.name))
        log.info("User ID: {}".format(broadsword.user.id))
        log.info("Version v.{}".format(BasicUtils.bot_version()))
        log.info("-----------------------")
        if config.bot["devMode"]:
            print("Broadsword is logged in..")
            print("Username: {}".format(broadsword.user.name))
            print("User ID: {}".format(broadsword.user.id))
            print("Version v.{}".format(BasicUtils.bot_version()))
            print("-----------------------")

        #   Load main modules
        for main_module in main_modules:
            try:
                broadsword.load_extension(main_module)
                log.info("{} loaded.".format(main_module))
                if config.bot["devMode"]:
                    print("{} loaded.".format(main_module))
            except Exception as e:
                log.exception("An exception has occurred in {}: ".format(__name__))
                if config.bot["devMode"]:
                    exc = "{}: {}".format(type(e).__name__, e)
                    print("Failed to load extension {}\n{}".format(plugin, exc))

        #   Load user modules
        for plugin, options in config.plugins.items():
            if not options.get("enabled", True):
                continue
            try:
                broadsword.load_extension(plugin)
                log.info("{} loaded.".format(main_module))
                if config.bot["devMode"]:
                    print("{} loaded.".format(main_module))
            except Exception as e:
                log.exception("An exception has occurred in {}: ".format(__name__))
                if config.bot["devMode"]:
                    exc = "{}: {}".format(type(e).__name__, e)
                    print("Failed to load extension {}\n{}".format(plugin, exc))

    broadsword.run(config.bot["token"])

def stop_bot():
    asyncio.ensure_future(broadsword.close())
    log.info("-----------------------")
    log.info("BroadswordBot connection closed.")
    if config.bot["devMode"]:
        print("-----------------------")
        print("BroadswordBot connection closed.")

if __name__ == '__main__':
    broadsword.loop.add_signal_handler(signal.SIGINT, stop_bot)
    broadsword.loop.add_signal_handler(signal.SIGTERM, stop_bot)
    run_bot()
