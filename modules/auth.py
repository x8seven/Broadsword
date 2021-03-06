import sys
import asyncio
import weakref
import json
import discord
import logging
from importlib import reload
from discord.ext import commands as broadsword

from lib.esi import ESIApi
from lib.db import DBMain
from lib.utils import AuthUtils
from config import config

log = logging.getLogger(__name__)

class AuthCMD:
    def __init__(self, bot):
        self.broadsword = bot
        self.esi = ESIApi()
        self.server = self.broadsword.get_server(id=config.bot["guild"])

    @broadsword.group(pass_context=True, hidden=False, description='''Группа команд администратора секции аутентификации.''')
    async def auth(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.broadsword.say(
                "{0.mention}, invalid git command passed...".format(ctx.author)
            )

    @auth.command(pass_context=True)
    async def reloadconf(self, ctx):
        try:
            reload(config)
        except Exception:
            log.exception("An exception has occurred in {}: ".format(__name__))


class AuthCheck:
    def __init__(self, bot):
        self.broadsword = bot
        self.server = self.broadsword.get_server(id=config.bot["guild"])
        self.esi = ESIApi()
        self.interval = config.auth["periodicCheckInterval"]
        self._task = self.broadsword.loop.create_task(self.auth_check())
        self.msg_start = "{} should have been run.".\
            format(__class__.__name__)
        self.msg_stop = "{} should have been unloaded.".\
            format(__class__.__name__)
        log.info(self.msg_start)
        
    def __unload(self):
        self._task.cancel()
        log.info(self.msg_stop)

    async def _selfclean(self, vars):
        for attr in vars: self.__dict__.pop(attr,None)

    async def auth_check_task(self):
        try:
            while not self.broadsword.is_closed:
                log.info("Start periodic check authorization.")
                await asyncio.sleep(self.interval)
        except asyncio.CancelledError:
            pass
        except (OSError, discord.ConnectionClosed):
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.auth_check_task())
        except Exception:
            log.exception("An exception has occurred in {}: ".format(__name__))
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.auth_check_task())

    async def auth_check(self):
        try:
            while not self.broadsword.is_closed:
                log.info("Start periodic check authorization.")
                self.users_left = False
                self.auth_groups = await AuthUtils().get_auth_group_ids()
                self.cnx = DBMain()
                self.auth_users = await self.cnx.auth_users_select()
                if self.auth_users is not None:
                    self.msg = "```Left members:"

                    for self.auth_user in self.auth_users:
                        self.member = self.server.get_member(
                                        self.auth_user["discord_id"])
                        if self.member is not None:
                            if self.member == self.server.owner:
                                continue
                            self.is_exempt = await AuthUtils().is_auth_exempt(
                                                    self.member.roles)
                            if not self.is_exempt:
                                self.charinfo = await self.esi.char_get_details(
                                                        self.auth_user["character_id"])
                                if self.charinfo is not None:
                                    if str(self.charinfo["alliance_id"]) not in self.auth_groups:
                                        self.users_left = True
                                        log.info(
                                            "User '{}' as known as '{}' left alliance\\corporation".\
                                            format(self.member.nick, self.member)
                                        )
                                        self.msg += "\n'{}' as known as '{}'".\
                                            format(self.member, self.member.nick)
                                        await self.cnx.auth_user_disable(
                                            self.auth_user["character_id"]
                                        )
                                        await self.broadsword.remove_roles(
                                            self.member,
                                            *self.member.roles
                                        )
                                        if config.auth["kickWhenLeaving"]:
                                            await self.broadsword.kick(self.member)
                                        else:
                                            await self.cnx.member_set_unauthorized(
                                                self.auth_user["discord_id"]
                                            )
                                else:
                                    log.warning("EVE services temprorary unavailable!")
                                    continue

                    self.msg += "```"
                    if self.users_left:
                        if config.auth["alertChannel"] != "":
                            self.channel = self.broadsword.get_channel(
                                config.auth["alertChannel"]
                            )
                            await self.broadsword.send_message(
                                self.channel, self.msg
                            )
                        else:
                            await self.broadsword.send_message(
                                self.server.owner,
                                "Warning! alertChannel is not set!"
                            )
                del self.cnx
                await asyncio.sleep(self.interval)
        except asyncio.CancelledError:
            pass
        except (OSError, discord.ConnectionClosed):
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.auth_check())
        except Exception:
            log.exception("An exception has occurred in {}: ".format(__name__))
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.auth_check())


class AuthTask:
    def __init__(self, bot):
        self.broadsword = bot
        self.server = self.broadsword.get_server(id=config.bot["guild"])
        self.esi = ESIApi()
        self.interval = 3
        self._task = self.broadsword.loop.create_task(self.auth_task())
        self.msg_start = "{} should have been run.".\
            format(__class__.__name__)
        self.msg_stop = "{} should have been unloaded.".\
            format(__class__.__name__)
        log.info(self.msg_start)

    def __unload(self):
        self._task.cancel()
        log.info(self.msg_stop)

    async def _selfclean(self, vars):
        for attr in vars: self.__dict__.pop(attr,None)

    async def auth_task(self):
        try:
            while not self.broadsword.is_closed:
                self.cnx = DBMain()

                self.pending = await self.cnx.auth_pending_select()
                #   self.pendings content:
                #      `id` int(11) NOT NULL AUTO_INCREMENT,
                #      `eve_name` varchar(365) DEFAULT NULL,
                #      `character_id` varchar(128) NOT NULL,
                #      `corporation_id` varchar(128) NOT NULL,
                #      `alliance_id` varchar(128) NOT NULL,
                #      `discord_id` varchar(64) NOT NULL,
                #      `active` varchar(10) NOT NULL,
                #      `pending` varchar(10) NOT NULL,
                #      `added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,

                if self.pending is not None:
                    log.info("Do authorize for '{}'.".format(self.pending["eve_name"]))
                    await self.auth()

                #await self._selfclean(("cnx", "pending"))
                await asyncio.sleep(self.interval)
        except asyncio.CancelledError:
            pass
        except (OSError, discord.ConnectionClosed):
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.auth_task())
        except Exception:
            log.exception("An exception has occurred in {}: ".format(__name__))
            self._task.cancel()
            self._task = self.broadsword.loop.create_task(self.auth_task())

    async def auth(self):
        try:
            #self.cnx = DBMain()

            #self.pending = pending
            #   self.pendings content:
            #      `id` int(11) NOT NULL AUTO_INCREMENT,
            #      `eve_name` varchar(365) DEFAULT NULL,
            #      `character_id` varchar(128) NOT NULL,
            #      `corporation_id` varchar(128) NOT NULL,
            #      `alliance_id` varchar(128) NOT NULL,
            #      `discord_id` varchar(64) NOT NULL,
            #      `active` varchar(10) NOT NULL,
            #      `pending` varchar(10) NOT NULL,
            #      `added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,

            self.auth_roles = []
            self.not_member = True
            self.do_authorize = False
            self.member = self.server.get_member(self.pending["discord_id"])

            for self.role in self.member.roles:
                self.auth_roles.append(self.role)

            self.auth_groups = await AuthUtils().get_auth_group_ids()
            if self.pending["alliance_id"] in self.auth_groups:
                self.auth_group = await AuthUtils().get_auth_group_values(self.pending["alliance_id"])

                self.corpinfo = await self.cnx.corpinfo_get(self.pending["corporation_id"])
                #   self.corpinfo content:
                #      `id` int(11) NOT NULL AUTO_INCREMENT,
                #      `corporation_id` varchar(128) NOT NULL,
                #      `alliance_id` varchar(128) DEFAULT NULL,
                #      `corporation_ticker` varchar(10) NOT NULL,
                #      `corporation_name` varchar(255) NOT NULL,
                #      `corporation_role` varchar(255) NOT NULL,

                if self.corpinfo is None:
                    self.corpinfo = {}
                    self.temp = await self.esi.corp_get_details(self.pending["corporation_id"])
                    #   self.corpinfo_temp content:
                    #       'alliance_id'
                    #       'ceo_id'
                    #       'corporation_description'
                    #       'corporation_name'
                    #       'creation_date'
                    #       'creator_id'
                    #       'faction'
                    #       'member_count'
                    #       'tax_rate'
                    #       'ticker'
                    #       'url'
                    if self.temp is None:
                        return
                    self.corpinfo["corporation_ticker"] = self.temp["ticker"]
                    self.corpinfo["corporation_name"] = self.temp["corporation_name"]
                    if self.auth_group["setCorpRole"] and self.auth_group["type"] == "alliance":
                        self.corpinfo["corporation_role"] = self.corpinfo["corporation_ticker"] + " Members"
                    else:
                        self.corpinfo["corporation_role"] = ""
                    await self.cnx.corpinfo_add(
                        self.pending["corporation_id"],
                        self.corpinfo["corporation_ticker"],
                        self.corpinfo["corporation_name"],
                        self.corpinfo["corporation_role"]
                    )

                # Update DB if setCorpRole has been enabled
                if self.corpinfo["corporation_role"] == ""\
                and self.auth_group["setCorpRole"]\
                and self.auth_group["type"] == "alliance":
                    self.corpinfo["corporation_role"] = \
                        self.corpinfo["corporation_ticker"] + " Members"
                    await self.cnx.corpinfo_update(
                        self.corpinfo["corporation_id"],
                        "corporation_role",
                        self.corpinfo["corporation_role"]
                    )

                if self.auth_group["setCorpRole"]\
                and self.auth_group["type"] == "alliance":
                    self.role_exist = False
                    self.role = None
                    for self.role in self.server.roles:
                        if self.role.name == self.corpinfo["corporation_role"]:
                            self.role_exist = True
                            self.corp_role = self.role
                            break
                    if not self.role_exist:
                        self.corp_role = await self.broadsword.create_role(
                            self.server,
                            name=self.corpinfo["corporation_role"],
                            permissions=discord.Permissions(104324160),
                            colour=discord.Colour(self.auth_group["corpColour"]),
                            hoist=True,
                            mentionable=True
                        )
                    if self.corp_role not in self.auth_roles:
                        self.auth_roles.append(self.corp_role)

                self.role = None
                for self.role in self.server.roles:
                    if self.role.name == self.auth_group["memberRole"]:
                        if self.role not in self.auth_roles:
                            self.auth_roles.append(self.role)
                            self.do_authorize = True
                            break
                        else:
                            self.do_authorize = True
                            break

                if self.do_authorize:
                    await self.broadsword.add_roles(self.member, *self.auth_roles)
                    if config.auth["nameEnforce"]:
                        self.charname = ""
                        self.charinfo = await self.esi.char_get_details(self.pending["character_id"])
                        if self.auth_group["corpTickers"] and self.auth_group["type"] == "alliance":
                            self.charname = "[" + self.corpinfo["corporation_ticker"] + "] "
                        self.charname = self.charname + self.charinfo["name"]
                        await self.cnx.rename_add(self.member.id, self.charname)
                    await self.cnx.auth_pending_disable(self.pending["character_id"])
                    await self.cnx.auth_user_enable(self.pending["character_id"])
                    await self.cnx.auth_user_update(
                        self.pending["character_id"],
                        "eve_name",
                        self.charinfo["name"]
                    )
                    await self.cnx.member_set_authorized(self.member.id)
                    await self.cnx.message_add("'{}' has been authorized.".format(self.pending["eve_name"]), config.auth["alertChannel"])
                    log.info("'{}' has been authorized.".format(self.pending["eve_name"]))
            return 0
        except Exception:
            log.exception("An exception has occurred in {}: ".format(__name__))
        finally:
            await self._selfclean(
                ("cnx", "pending", "auth_roles", "member", "auth_groups"
                "auth_group", "corpinfo", "temp", "role", "corp_role"
                "do_authorize", "charinfo", "charname")
            )


def setup(broadsword):
    broadsword.add_cog(AuthCMD(broadsword))
    broadsword.add_cog(AuthTask(broadsword))
    if config.auth["periodicCheck"]:
        broadsword.add_cog(AuthCheck(broadsword))
