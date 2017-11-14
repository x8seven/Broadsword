#import urllib.parse as urllib
import discord
import asyncio
from discord.ext import commands as broadsword
from config import config
from lib.libdb import DB

class QueueMessages:
    def __init__(self, bot):
        self.broadsword = bot
        self._task = self.broadsword.loop.create_task(self.qMessageTask())
        print('QueueMessages.qMessageTask should have been run..')
        
    def __unload(self):
        self._task.cancel()
        print('QueueMessages.qMessageTask should have been unloaded..')

    async def qMessageTask(self):
        try:
            while not self.broadsword.is_closed:
                self.cnx = DB()
                self.x = 0
                while self.x < 3:
                    self.id = await self.cnx.gelOldestQueueMessage()
                    if self.id is None:
                        break
                    self.queued_msg = await self.cnx.getQueuedMessage(self.id)
                    if self.queued_msg is not None:
                        if self.queued_msg['channel'] is None:
                            await self.cnx.delQueuedMessage(self.id)
                            continue
                        if self.queued_msg['message'] is None:
                            await self.cnx.delQueuedMessage(self.id)
                            continue
                        self.channel = self.broadsword.get_channel(self.queued_msg['channel'])
                        await self.broadsword.send_message(self.channel, self.queued_msg['message'])
                        await self.cnx.delQueuedMessage(self.id)
                    else:
                        continue
                    self.x += 1
                    del self.channel
                    del self.queued_msg
                    del self.id
                del self.cnx
                await asyncio.sleep(7)
        except Exception as e:
            print(e)
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.qAuthTask())
        except asyncio.CancelledError as e:
            print(e)
        except (OSError, discord.ConnectionClosed):
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.qAuthTask())

class QueueRename:
    def __init__(self, bot):
        self.broadsword = bot
        self._task = self.broadsword.loop.create_task(self.qRenameTask())
        print('QueueMessages.qRenameTask should have been run..')
        
    def __unload(self):
        self._task.cancel()
        print('QueueMessages.qRenameTask should have been unloaded..')

    async def qRenameTask(self):
        try:
            while not self.broadsword.is_closed:
                self.server = self.broadsword.get_server(id=config.bot['guild'])
                self.cnx = DB()
                self.x = 0
                while self.x < 4:
                    self.id = await self.cnx.gelOldestQueueRename()
                    if self.id is None:
                        break
                    self.queued_rename = await self.cnx.getQueuedRename(self.id)
                    if self.queued_rename is not None:
                        if self.queued_rename['discordID'] is None:
                            await self.cnx.delQueuedRename(self.id)
                            continue
                        if self.queued_rename['nick'] is None:
                            await self.cnx.delQueuedRename(self.id)
                            continue
                        try:
                            self.member = self.server.get_member(self.queued_rename['discordID'])
                            await self.broadsword.change_nickname(self.member, self.queued_rename['nick'])
                            await self.cnx.delQueuedRename(self.id)
                        except discord.Forbidden as e:
                            if self.queued_rename['discordID'] == self.server.owner.id:
                                print("Sorry, but owner cann't be renamed!")
                                await self.cnx.delQueuedRename(self.id)
                                continue
                            if e.text == "Privilege is too low...":
                                print("BroadswordBot needs more privileges!")
                    else:
                        continue
                    self.x += 1
                    del self.member
                    del self.queued_rename
                    del self.id
                del self.cnx
                await asyncio.sleep(10)
        except Exception as e:
            print(e)
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.qRenameTask())
        except asyncio.CancelledError as e:
            print(e)
        except (OSError, discord.ConnectionClosed):
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.qRenameTask())

def setup(broadsword):
    broadsword.add_cog(QueueMessages(broadsword))
    broadsword.add_cog(QueueRename(broadsword))