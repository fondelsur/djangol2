# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountGsdata(models.Model):
    account_name = models.CharField(max_length=45)
    var = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_gsdata'
        unique_together = (('account_name', 'var'),)


class Airships(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    fuel = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'airships'


class Announcements(models.Model):
    type = models.IntegerField()
    initial = models.BigIntegerField()
    delay = models.BigIntegerField()
    repeat = models.IntegerField()
    author = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'announcements'


class Auction(models.Model):
    id = models.IntegerField(primary_key=True)
    sellerid = models.IntegerField(db_column='sellerId')  # Field name made lowercase.
    sellername = models.CharField(db_column='sellerName', max_length=50)  # Field name made lowercase.
    sellerclanname = models.CharField(db_column='sellerClanName', max_length=50)  # Field name made lowercase.
    itemtype = models.CharField(db_column='itemType', max_length=25)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    itemobjectid = models.IntegerField(db_column='itemObjectId')  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=40)  # Field name made lowercase.
    itemquantity = models.BigIntegerField(db_column='itemQuantity')  # Field name made lowercase.
    startingbid = models.BigIntegerField(db_column='startingBid')  # Field name made lowercase.
    currentbid = models.BigIntegerField(db_column='currentBid')  # Field name made lowercase.
    enddate = models.BigIntegerField(db_column='endDate')  # Field name made lowercase.

    class Meta:
        db_table = 'auction'
        unique_together = (('itemtype', 'itemid', 'itemobjectid'),)


class AuctionBid(models.Model):
    id = models.IntegerField(primary_key=True)
    auctionid = models.IntegerField(db_column='auctionId')  # Field name made lowercase.
    bidderid = models.IntegerField(db_column='bidderId')  # Field name made lowercase.
    biddername = models.CharField(db_column='bidderName', max_length=50)  # Field name made lowercase.
    clan_name = models.CharField(max_length=50)
    maxbid = models.BigIntegerField(db_column='maxBid')  # Field name made lowercase.
    time_bid = models.BigIntegerField()

    class Meta:
        db_table = 'auction_bid'
        unique_together = (('auctionid', 'bidderid'),)


class AuctionWatch(models.Model):
    charobjid = models.IntegerField(db_column='charObjId')  # Field name made lowercase.
    auctionid = models.IntegerField(db_column='auctionId')  # Field name made lowercase.

    class Meta:
        db_table = 'auction_watch'
        unique_together = (('charobjid', 'auctionid'),)


class BbsFavorites(models.Model):
    favid = models.AutoField(db_column='favId', primary_key=True)  # Field name made lowercase.
    playerid = models.IntegerField(db_column='playerId')  # Field name made lowercase.
    favtitle = models.CharField(db_column='favTitle', max_length=50)  # Field name made lowercase.
    favbypass = models.CharField(db_column='favBypass', max_length=127)  # Field name made lowercase.
    favadddate = models.DateTimeField(db_column='favAddDate')  # Field name made lowercase.

    class Meta:
        db_table = 'bbs_favorites'
        unique_together = (('favid', 'playerid'),)


class BotReportedCharData(models.Model):
    botid = models.IntegerField(db_column='botId')  # Field name made lowercase.
    reporterid = models.IntegerField(db_column='reporterId')  # Field name made lowercase.
    reportdate = models.BigIntegerField(db_column='reportDate')  # Field name made lowercase.

    class Meta:
        db_table = 'bot_reported_char_data'
        unique_together = (('botid', 'reporterid'),)


class Buylists(models.Model):
    buylist_id = models.IntegerField()
    item_id = models.IntegerField()
    count = models.BigIntegerField()
    next_restock_time = models.BigIntegerField()

    class Meta:
        db_table = 'buylists'
        unique_together = (('buylist_id', 'item_id'),)


class Castle(models.Model):
    id = models.IntegerField()
    name = models.CharField(primary_key=True, max_length=25)
    taxpercent = models.IntegerField(db_column='taxPercent')  # Field name made lowercase.
    treasury = models.BigIntegerField()
    siegedate = models.BigIntegerField(db_column='siegeDate')  # Field name made lowercase.
    regtimeover = models.CharField(db_column='regTimeOver', max_length=5)  # Field name made lowercase.
    regtimeend = models.BigIntegerField(db_column='regTimeEnd')  # Field name made lowercase.
    shownpccrest = models.CharField(db_column='showNpcCrest', max_length=5)  # Field name made lowercase.
    ticketbuycount = models.SmallIntegerField(db_column='ticketBuyCount')  # Field name made lowercase.

    class Meta:
        db_table = 'castle'


class CastleDoorupgrade(models.Model):
    doorid = models.IntegerField(db_column='doorId', primary_key=True)  # Field name made lowercase.
    ratio = models.IntegerField()
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.

    class Meta:
        db_table = 'castle_doorupgrade'


class CastleFunctions(models.Model):
    castle_id = models.IntegerField()
    type = models.IntegerField()
    lvl = models.IntegerField()
    lease = models.IntegerField()
    rate = models.DecimalField(max_digits=20, decimal_places=0)
    endtime = models.BigIntegerField(db_column='endTime')  # Field name made lowercase.

    class Meta:
        db_table = 'castle_functions'
        unique_together = (('castle_id', 'type'),)


class CastleManorProcure(models.Model):
    castle_id = models.IntegerField()
    crop_id = models.IntegerField()
    amount = models.IntegerField()
    start_amount = models.IntegerField()
    price = models.IntegerField()
    reward_type = models.IntegerField()
    next_period = models.IntegerField()

    class Meta:
        db_table = 'castle_manor_procure'
        unique_together = (('castle_id', 'crop_id', 'next_period'),)


class CastleManorProduction(models.Model):
    castle_id = models.IntegerField()
    seed_id = models.IntegerField()
    amount = models.IntegerField()
    start_amount = models.IntegerField()
    price = models.IntegerField()
    next_period = models.IntegerField()

    class Meta:
        db_table = 'castle_manor_production'
        unique_together = (('castle_id', 'seed_id', 'next_period'),)


class CastleSiegeGuards(models.Model):
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.
    id = models.SmallIntegerField(primary_key=True)
    npcid = models.SmallIntegerField(db_column='npcId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()
    respawndelay = models.IntegerField(db_column='respawnDelay')  # Field name made lowercase.
    ishired = models.IntegerField(db_column='isHired')  # Field name made lowercase.

    class Meta:
        db_table = 'castle_siege_guards'


class CastleTrapupgrade(models.Model):
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.
    towerindex = models.IntegerField(db_column='towerIndex')  # Field name made lowercase.
    level = models.IntegerField()

    class Meta:
        db_table = 'castle_trapupgrade'
        unique_together = (('towerindex', 'castleid'),)


class CharacterContacts(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    contactid = models.IntegerField(db_column='contactId')  # Field name made lowercase.

    class Meta:
        db_table = 'character_contacts'
        unique_together = (('charid', 'contactid'),)


class CharacterFriends(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    friendid = models.IntegerField(db_column='friendId')  # Field name made lowercase.
    relation = models.IntegerField()

    class Meta:
        db_table = 'character_friends'
        unique_together = (('charid', 'friendid'),)


class CharacterHennas(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    symbol_id = models.IntegerField(blank=True, null=True)
    slot = models.IntegerField()
    class_index = models.IntegerField()

    class Meta:
        db_table = 'character_hennas'
        unique_together = (('charid', 'slot', 'class_index'),)


class CharacterInstanceTime(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    instanceid = models.IntegerField(db_column='instanceId')  # Field name made lowercase.
    time = models.BigIntegerField()

    class Meta:
        db_table = 'character_instance_time'
        unique_together = (('charid', 'instanceid'),)


class CharacterItemReuseSave(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    itemobjid = models.IntegerField(db_column='itemObjId')  # Field name made lowercase.
    reusedelay = models.IntegerField(db_column='reuseDelay')  # Field name made lowercase.
    systime = models.BigIntegerField()

    class Meta:
        db_table = 'character_item_reuse_save'
        unique_together = (('charid', 'itemid', 'itemobjid'),)


class CharacterMacroses(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    icon = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    descr = models.CharField(max_length=80, blank=True, null=True)
    acronym = models.CharField(max_length=4, blank=True, null=True)
    commands = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'character_macroses'
        unique_together = (('charid', 'id'),)


class CharacterOfflineTrade(models.Model):
    charid = models.IntegerField(db_column='charId', primary_key=True)  # Field name made lowercase.
    time = models.BigIntegerField()
    type = models.IntegerField()
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'character_offline_trade'


class CharacterOfflineTradeItems(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    item = models.IntegerField()
    count = models.BigIntegerField()
    price = models.BigIntegerField()

    class Meta:
        db_table = 'character_offline_trade_items'


class CharacterPetSkillsSave(models.Model):
    petobjitemid = models.IntegerField(db_column='petObjItemId')  # Field name made lowercase.
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    remaining_time = models.IntegerField()
    buff_index = models.IntegerField()

    class Meta:
        db_table = 'character_pet_skills_save'
        unique_together = (('petobjitemid', 'skill_id', 'skill_level'),)


class CharacterPremiumItems(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    itemnum = models.IntegerField(db_column='itemNum')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    itemcount = models.BigIntegerField(db_column='itemCount')  # Field name made lowercase.
    itemsender = models.CharField(db_column='itemSender', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'character_premium_items'


class CharacterQuestGlobalData(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_quest_global_data'
        unique_together = (('charid', 'var'),)


class CharacterQuests(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    name = models.CharField(max_length=60)
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_quests'
        unique_together = (('charid', 'name', 'var', 'class_index'),)


class CharacterRaidPoints(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    boss_id = models.IntegerField()
    points = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'character_raid_points'
        unique_together = (('charid', 'boss_id'),)


class CharacterRecipebook(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    id = models.DecimalField(max_digits=11, decimal_places=0, primary_key=True)
    classindex = models.IntegerField(db_column='classIndex')  # Field name made lowercase.
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_recipebook'
        unique_together = (('id', 'charid', 'classindex'),)


class CharacterRecipeshoplist(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    recipeid = models.IntegerField(db_column='recipeId')  # Field name made lowercase.
    price = models.BigIntegerField()
    index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_recipeshoplist'
        unique_together = (('charid', 'recipeid'),)


class CharacterRecoBonus(models.Model):
    charid = models.IntegerField(db_column='charId', unique=True)  # Field name made lowercase.
    rec_have = models.IntegerField()
    rec_left = models.IntegerField()
    time_left = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'character_reco_bonus'


class CharacterShortcuts(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    slot = models.DecimalField(max_digits=3, decimal_places=0)
    page = models.DecimalField(max_digits=3, decimal_places=0)
    type = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    shortcut_id = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    level = models.CharField(max_length=4, blank=True, null=True)
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_shortcuts'
        unique_together = (('charid', 'slot', 'page', 'class_index'),)


class CharacterSkills(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_skills'
        unique_together = (('charid', 'skill_id', 'class_index'),)


class CharacterSkillsSave(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    remaining_time = models.IntegerField()
    reuse_delay = models.IntegerField()
    systime = models.BigIntegerField()
    restore_type = models.IntegerField()
    class_index = models.IntegerField()
    buff_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_skills_save'
        unique_together = (('charid', 'skill_id', 'skill_level', 'class_index'),)


class CharacterSubclasses(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    class_id = models.IntegerField()
    exp = models.DecimalField(max_digits=20, decimal_places=0)
    sp = models.DecimalField(max_digits=11, decimal_places=0)
    level = models.IntegerField()
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_subclasses'
        unique_together = (('charid', 'class_id'),)


class CharacterSummonSkillsSave(models.Model):
    ownerid = models.IntegerField(db_column='ownerId')  # Field name made lowercase.
    ownerclassindex = models.IntegerField(db_column='ownerClassIndex')  # Field name made lowercase.
    summonskillid = models.IntegerField(db_column='summonSkillId')  # Field name made lowercase.
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    remaining_time = models.IntegerField()
    buff_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_summon_skills_save'
        unique_together = (('ownerid', 'ownerclassindex', 'summonskillid', 'skill_id', 'skill_level'),)


class CharacterSummons(models.Model):
    ownerid = models.IntegerField(db_column='ownerId')  # Field name made lowercase.
    summonskillid = models.IntegerField(db_column='summonSkillId')  # Field name made lowercase.
    curhp = models.IntegerField(db_column='curHp', blank=True, null=True)  # Field name made lowercase.
    curmp = models.IntegerField(db_column='curMp', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_summons'
        unique_together = (('ownerid', 'summonskillid'),)


class CharacterTpbookmark(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    icon = models.IntegerField()
    tag = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'character_tpbookmark'
        unique_together = (('charid', 'id'),)


class CharacterUiActions(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    cat = models.IntegerField()
    order = models.IntegerField()
    cmd = models.IntegerField()
    key = models.IntegerField()
    tgkey1 = models.IntegerField(db_column='tgKey1', blank=True, null=True)  # Field name made lowercase.
    tgkey2 = models.IntegerField(db_column='tgKey2', blank=True, null=True)  # Field name made lowercase.
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_ui_actions'
        unique_together = (('charid', 'cat', 'cmd'),)


class CharacterUiCategories(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    catid = models.IntegerField(db_column='catId')  # Field name made lowercase.
    order = models.IntegerField()
    cmdid = models.IntegerField(db_column='cmdId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'character_ui_categories'
        unique_together = (('charid', 'catid', 'order'),)


class CharacterVariables(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    var = models.CharField(max_length=255)
    val = models.TextField()

    class Meta:
        managed = False
        db_table = 'character_variables'


class Characters(models.Model):
    account_name = models.CharField(max_length=45, blank=True, null=True)
    charid = models.IntegerField(db_column='charId', primary_key=True)
    char_name = models.CharField(max_length=35)
    level = models.IntegerField(blank=True, null=True)
    maxhp = models.IntegerField(db_column='maxHp', blank=True, null=True)
    curhp = models.IntegerField(db_column='curHp', blank=True, null=True)
    maxcp = models.IntegerField(db_column='maxCp', blank=True, null=True)
    curcp = models.IntegerField(db_column='curCp', blank=True, null=True)
    maxmp = models.IntegerField(db_column='maxMp', blank=True, null=True)
    curmp = models.IntegerField(db_column='curMp', blank=True, null=True)
    face = models.IntegerField(blank=True, null=True)
    hairstyle = models.IntegerField(db_column='hairStyle', blank=True, null=True)
    haircolor = models.IntegerField(db_column='hairColor', blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    heading = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    z = models.IntegerField(blank=True, null=True)
    exp = models.BigIntegerField(blank=True, null=True)
    expbeforedeath = models.BigIntegerField(db_column='expBeforeDeath', blank=True, null=True)
    sp = models.IntegerField()
    karma = models.IntegerField(blank=True, null=True)
    fame = models.IntegerField()
    pvpkills = models.SmallIntegerField(blank=True, null=True)
    pkkills = models.SmallIntegerField(blank=True, null=True)
    clanid = models.IntegerField(blank=True, null=True)
    race = models.IntegerField(blank=True, null=True)
    classid = models.IntegerField(blank=True, null=True)
    base_class = models.IntegerField()
    transform_id = models.SmallIntegerField()
    deletetime = models.BigIntegerField()
    cancraft = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=21, blank=True, null=True)
    title_color = models.IntegerField()
    accesslevel = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    onlinetime = models.IntegerField(blank=True, null=True)
    char_slot = models.IntegerField(blank=True, null=True)
    newbie = models.IntegerField(blank=True, null=True)
    lastaccess = models.BigIntegerField(db_column='lastAccess')  # Field name made lowercase.
    clan_privs = models.IntegerField(blank=True, null=True)
    wantspeace = models.IntegerField(blank=True, null=True)
    isin7sdungeon = models.IntegerField()
    power_grade = models.IntegerField(blank=True, null=True)
    nobless = models.IntegerField()
    subpledge = models.SmallIntegerField()
    lvl_joined_academy = models.IntegerField()
    apprentice = models.IntegerField()
    sponsor = models.IntegerField()
    clan_join_expiry_time = models.BigIntegerField()
    clan_create_expiry_time = models.BigIntegerField()
    death_penalty_level = models.SmallIntegerField()
    bookmarkslot = models.SmallIntegerField()
    vitality_points = models.SmallIntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    language = models.CharField(max_length=2, blank=True, null=True)
    
    def __unicode__(self):
        return self.char_name
    
    class Meta:
        db_table = 'characters'


class ClanData(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    clan_name = models.CharField(max_length=45, blank=True, null=True)
    clan_level = models.IntegerField(blank=True, null=True)
    reputation_score = models.IntegerField()
    hascastle = models.IntegerField(db_column='hasCastle', blank=True, null=True)  # Field name made lowercase.
    blood_alliance_count = models.SmallIntegerField()
    blood_oath_count = models.SmallIntegerField()
    ally_id = models.IntegerField(blank=True, null=True)
    ally_name = models.CharField(max_length=45, blank=True, null=True)
    leader_id = models.IntegerField(blank=True, null=True)
    crest_id = models.IntegerField(blank=True, null=True)
    crest_large_id = models.IntegerField(blank=True, null=True)
    ally_crest_id = models.IntegerField(blank=True, null=True)
    auction_bid_at = models.IntegerField()
    ally_penalty_expiry_time = models.BigIntegerField()
    ally_penalty_type = models.IntegerField()
    char_penalty_expiry_time = models.BigIntegerField()
    dissolving_expiry_time = models.BigIntegerField()
    new_leader_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_data'


class ClanNotices(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    enabled = models.CharField(max_length=5)
    notice = models.TextField()

    class Meta:
        managed = False
        db_table = 'clan_notices'


class ClanPrivs(models.Model):
    clan_id = models.IntegerField()
    rank = models.IntegerField()
    party = models.IntegerField()
    privs = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_privs'
        unique_together = (('clan_id', 'rank', 'party'),)


class ClanSkills(models.Model):
    clan_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    skill_name = models.CharField(max_length=26, blank=True, null=True)
    sub_pledge_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_skills'
        unique_together = (('clan_id', 'skill_id', 'sub_pledge_id'),)


class ClanSubpledges(models.Model):
    clan_id = models.IntegerField()
    sub_pledge_id = models.IntegerField()
    name = models.CharField(max_length=45, blank=True, null=True)
    leader_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_subpledges'
        unique_together = (('clan_id', 'sub_pledge_id'),)


class ClanWars(models.Model):
    clan1 = models.CharField(max_length=35)
    clan2 = models.CharField(max_length=35)
    wantspeace1 = models.DecimalField(max_digits=1, decimal_places=0)
    wantspeace2 = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'clan_wars'


class Clanhall(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    ownerid = models.IntegerField(db_column='ownerId')  # Field name made lowercase.
    lease = models.IntegerField()
    desc = models.TextField()
    location = models.CharField(max_length=15)
    paiduntil = models.BigIntegerField(db_column='paidUntil')  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=1, decimal_places=0)  # Field name made lowercase.
    paid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clanhall'


class ClanhallFunctions(models.Model):
    hall_id = models.IntegerField()
    type = models.IntegerField()
    lvl = models.IntegerField()
    lease = models.IntegerField()
    rate = models.DecimalField(max_digits=20, decimal_places=0)
    endtime = models.BigIntegerField(db_column='endTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clanhall_functions'
        unique_together = (('hall_id', 'type'),)


class ClanhallSiegeAttackers(models.Model):
    clanhall_id = models.IntegerField()
    attacker_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clanhall_siege_attackers'


class ClanhallSiegeGuards(models.Model):
    clanhallid = models.IntegerField(db_column='clanHallId')  # Field name made lowercase.
    npcid = models.SmallIntegerField(db_column='npcId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()
    respawndelay = models.IntegerField(db_column='respawnDelay')  # Field name made lowercase.
    issiegeboss = models.CharField(db_column='isSiegeBoss', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clanhall_siege_guards'


class Crests(models.Model):
    crest_id = models.IntegerField(primary_key=True)
    data = models.CharField(max_length=2176)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crests'


class CursedWeapons(models.Model):
    itemid = models.IntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    playerkarma = models.IntegerField(db_column='playerKarma', blank=True, null=True)  # Field name made lowercase.
    playerpkkills = models.IntegerField(db_column='playerPkKills', blank=True, null=True)  # Field name made lowercase.
    nbkills = models.IntegerField(db_column='nbKills', blank=True, null=True)  # Field name made lowercase.
    endtime = models.BigIntegerField(db_column='endTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cursed_weapons'


class CustomNpcBuffer(models.Model):
    npc_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    skill_fee_id = models.IntegerField()
    skill_fee_amount = models.IntegerField()
    buff_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_npc_buffer'
        unique_together = (('npc_id', 'skill_id', 'buff_group'),)


class CustomSpawnlist(models.Model):
    location = models.CharField(max_length=40)
    count = models.IntegerField()
    npc_templateid = models.IntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    randomx = models.IntegerField()
    randomy = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    respawn_random = models.IntegerField()
    loc_id = models.IntegerField()
    periodofday = models.IntegerField(db_column='periodOfDay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'custom_spawnlist'


class CustomTeleport(models.Model):
    description = models.CharField(db_column='Description', max_length=75, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    loc_x = models.IntegerField(blank=True, null=True)
    loc_y = models.IntegerField(blank=True, null=True)
    loc_z = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    fornoble = models.IntegerField()
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'custom_teleport'


class DimensionalRift(models.Model):
    type = models.IntegerField()
    room_id = models.IntegerField()
    xmin = models.IntegerField(db_column='xMin')  # Field name made lowercase.
    xmax = models.IntegerField(db_column='xMax')  # Field name made lowercase.
    ymin = models.IntegerField(db_column='yMin')  # Field name made lowercase.
    ymax = models.IntegerField(db_column='yMax')  # Field name made lowercase.
    zmin = models.IntegerField(db_column='zMin')  # Field name made lowercase.
    zmax = models.IntegerField(db_column='zMax')  # Field name made lowercase.
    xt = models.IntegerField(db_column='xT')  # Field name made lowercase.
    yt = models.IntegerField(db_column='yT')  # Field name made lowercase.
    zt = models.IntegerField(db_column='zT')  # Field name made lowercase.
    boss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dimensional_rift'
        unique_together = (('type', 'room_id'),)


class Fort(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    siegedate = models.BigIntegerField(db_column='siegeDate')  # Field name made lowercase.
    lastownedtime = models.BigIntegerField(db_column='lastOwnedTime')  # Field name made lowercase.
    owner = models.IntegerField()
    forttype = models.IntegerField(db_column='fortType')  # Field name made lowercase.
    state = models.IntegerField()
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.
    supplylvl = models.IntegerField(db_column='supplyLvL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fort'


class FortDoorupgrade(models.Model):
    doorid = models.IntegerField(db_column='doorId', primary_key=True)  # Field name made lowercase.
    fortid = models.IntegerField(db_column='fortId')  # Field name made lowercase.
    hp = models.IntegerField()
    pdef = models.IntegerField(db_column='pDef')  # Field name made lowercase.
    mdef = models.IntegerField(db_column='mDef')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fort_doorupgrade'


class FortFunctions(models.Model):
    fort_id = models.IntegerField()
    type = models.IntegerField()
    lvl = models.IntegerField()
    lease = models.IntegerField()
    rate = models.DecimalField(max_digits=20, decimal_places=0)
    endtime = models.BigIntegerField(db_column='endTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fort_functions'
        unique_together = (('fort_id', 'type'),)


class FortSiegeGuards(models.Model):
    fortid = models.IntegerField(db_column='fortId')  # Field name made lowercase.
    id = models.SmallIntegerField(primary_key=True)
    npcid = models.SmallIntegerField(db_column='npcId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()
    respawndelay = models.IntegerField(db_column='respawnDelay')  # Field name made lowercase.
    ishired = models.IntegerField(db_column='isHired')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fort_siege_guards'


class FortSpawnlist(models.Model):
    fortid = models.IntegerField(db_column='fortId')  # Field name made lowercase.
    id = models.SmallIntegerField(primary_key=True)
    npcid = models.SmallIntegerField(db_column='npcId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()
    spawntype = models.IntegerField(db_column='spawnType')  # Field name made lowercase.
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fort_spawnlist'


class FortsiegeClans(models.Model):
    fort_id = models.IntegerField()
    clan_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fortsiege_clans'
        unique_together = (('clan_id', 'fort_id'),)


class Forums(models.Model):
    forum_id = models.IntegerField(primary_key=True)
    forum_name = models.CharField(max_length=255)
    forum_parent = models.IntegerField()
    forum_post = models.IntegerField()
    forum_type = models.IntegerField()
    forum_perm = models.IntegerField()
    forum_owner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forums'


class FourSepulchersSpawnlist(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    location = models.CharField(max_length=19)
    count = models.IntegerField()
    npc_templateid = models.SmallIntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    randomx = models.IntegerField()
    randomy = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    key_npc_id = models.SmallIntegerField()
    spawntype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'four_sepulchers_spawnlist'


class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    idnr = models.IntegerField()
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    prize = models.IntegerField()
    newprize = models.IntegerField()
    prize1 = models.IntegerField()
    prize2 = models.IntegerField()
    prize3 = models.IntegerField()
    enddate = models.BigIntegerField()
    finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games'
        unique_together = (('id', 'idnr'),)


class GlobalTasks(models.Model):
    task = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    last_activation = models.BigIntegerField()
    param1 = models.CharField(max_length=100)
    param2 = models.CharField(max_length=100)
    param3 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'global_tasks'


class GlobalVariables(models.Model):
    var = models.CharField(primary_key=True, max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_variables'


class GrandbossData(models.Model):
    boss_id = models.SmallIntegerField(primary_key=True)
    loc_x = models.IntegerField()
    loc_y = models.IntegerField()
    loc_z = models.IntegerField()
    heading = models.IntegerField()
    respawn_time = models.BigIntegerField()
    currenthp = models.DecimalField(db_column='currentHP', max_digits=30, decimal_places=15)  # Field name made lowercase.
    currentmp = models.DecimalField(db_column='currentMP', max_digits=30, decimal_places=15)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grandboss_data'


class GrandbossList(models.Model):
    player_id = models.DecimalField(max_digits=11, decimal_places=0)
    zone = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'grandboss_list'
        unique_together = (('player_id', 'zone'),)


class HerbDroplistGroups(models.Model):
    groupid = models.IntegerField(db_column='groupId')  # Field name made lowercase.
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.
    min = models.SmallIntegerField()
    max = models.SmallIntegerField()
    category = models.SmallIntegerField()
    chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'herb_droplist_groups'
        unique_together = (('groupid', 'itemid', 'category'),)


class Heroes(models.Model):
    charid = models.IntegerField(db_column='charId', primary_key=True)  # Field name made lowercase.
    class_id = models.DecimalField(max_digits=3, decimal_places=0)
    count = models.DecimalField(max_digits=3, decimal_places=0)
    played = models.DecimalField(max_digits=1, decimal_places=0)
    claimed = models.CharField(max_length=5)
    message = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'heroes'


class HeroesDiary(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    time = models.BigIntegerField()
    action = models.IntegerField()
    param = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'heroes_diary'


class ItemAttributes(models.Model):
    itemid = models.IntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    augattributes = models.IntegerField(db_column='augAttributes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_attributes'


class ItemAuction(models.Model):
    auctionid = models.IntegerField(db_column='auctionId', primary_key=True)  # Field name made lowercase.
    instanceid = models.IntegerField(db_column='instanceId')  # Field name made lowercase.
    auctionitemid = models.IntegerField(db_column='auctionItemId')  # Field name made lowercase.
    startingtime = models.BigIntegerField(db_column='startingTime')  # Field name made lowercase.
    endingtime = models.BigIntegerField(db_column='endingTime')  # Field name made lowercase.
    auctionstateid = models.IntegerField(db_column='auctionStateId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_auction'


class ItemAuctionBid(models.Model):
    auctionid = models.IntegerField(db_column='auctionId')  # Field name made lowercase.
    playerobjid = models.IntegerField(db_column='playerObjId')  # Field name made lowercase.
    playerbid = models.BigIntegerField(db_column='playerBid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_auction_bid'
        unique_together = (('auctionid', 'playerobjid'),)


class ItemElementals(models.Model):
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    elemtype = models.IntegerField(db_column='elemType')  # Field name made lowercase.
    elemvalue = models.IntegerField(db_column='elemValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_elementals'
        unique_together = (('itemid', 'elemtype'),)


class Items(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    object_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(blank=True, null=True)
    count = models.BigIntegerField()
    enchant_level = models.IntegerField(blank=True, null=True)
    loc = models.CharField(max_length=10, blank=True, null=True)
    loc_data = models.IntegerField(blank=True, null=True)
    time_of_use = models.IntegerField(blank=True, null=True)
    custom_type1 = models.IntegerField(blank=True, null=True)
    custom_type2 = models.IntegerField(blank=True, null=True)
    mana_left = models.DecimalField(max_digits=5, decimal_places=0)
    time = models.DecimalField(max_digits=13, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'items'


class Itemsonground(models.Model):
    object_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(blank=True, null=True)
    count = models.BigIntegerField()
    enchant_level = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    z = models.IntegerField(blank=True, null=True)
    drop_time = models.BigIntegerField()
    equipable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemsonground'


class Locations(models.Model):
    loc_id = models.SmallIntegerField()
    loc_x = models.IntegerField()
    loc_y = models.IntegerField()
    loc_zmin = models.IntegerField()
    loc_zmax = models.IntegerField()
    proc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locations'
        unique_together = (('loc_id', 'loc_x', 'loc_y'),)


class MerchantLease(models.Model):
    merchant_id = models.IntegerField()
    player_id = models.IntegerField()
    bid = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    player_name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_lease'
        unique_together = (('merchant_id', 'player_id', 'type'),)


class Messages(models.Model):
    messageid = models.IntegerField(db_column='messageId', primary_key=True)  # Field name made lowercase.
    senderid = models.IntegerField(db_column='senderId')  # Field name made lowercase.
    receiverid = models.IntegerField(db_column='receiverId')  # Field name made lowercase.
    subject = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    expiration = models.BigIntegerField()
    reqadena = models.BigIntegerField(db_column='reqAdena')  # Field name made lowercase.
    hasattachments = models.CharField(db_column='hasAttachments', max_length=5)  # Field name made lowercase.
    isunread = models.CharField(db_column='isUnread', max_length=5)  # Field name made lowercase.
    isdeletedbysender = models.CharField(db_column='isDeletedBySender', max_length=5)  # Field name made lowercase.
    isdeletedbyreceiver = models.CharField(db_column='isDeletedByReceiver', max_length=5)  # Field name made lowercase.
    islocked = models.CharField(db_column='isLocked', max_length=5)  # Field name made lowercase.
    sendbysystem = models.IntegerField(db_column='sendBySystem')  # Field name made lowercase.
    isreturned = models.CharField(db_column='isReturned', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messages'


class ModsWedding(models.Model):
    player1id = models.IntegerField(db_column='player1Id')  # Field name made lowercase.
    player2id = models.IntegerField(db_column='player2Id')  # Field name made lowercase.
    married = models.CharField(max_length=5, blank=True, null=True)
    affiancedate = models.DecimalField(db_column='affianceDate', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    weddingdate = models.DecimalField(db_column='weddingDate', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mods_wedding'


class NpcBuffer(models.Model):
    npc_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    skill_fee_id = models.IntegerField()
    skill_fee_amount = models.IntegerField()
    buff_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npc_buffer'
        unique_together = (('npc_id', 'skill_id', 'buff_group'),)


class OlympiadData(models.Model):
    id = models.IntegerField(primary_key=True)
    current_cycle = models.IntegerField()
    period = models.IntegerField()
    olympiad_end = models.BigIntegerField()
    validation_end = models.BigIntegerField()
    next_weekly_change = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'olympiad_data'


class OlympiadFights(models.Model):
    charoneid = models.IntegerField(db_column='charOneId')  # Field name made lowercase.
    chartwoid = models.IntegerField(db_column='charTwoId')  # Field name made lowercase.
    charoneclass = models.IntegerField(db_column='charOneClass')  # Field name made lowercase.
    chartwoclass = models.IntegerField(db_column='charTwoClass')  # Field name made lowercase.
    winner = models.IntegerField()
    start = models.BigIntegerField()
    time = models.BigIntegerField()
    classed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'olympiad_fights'


class OlympiadNobles(models.Model):
    charid = models.IntegerField(db_column='charId', primary_key=True)  # Field name made lowercase.
    class_id = models.IntegerField()
    olympiad_points = models.IntegerField()
    competitions_done = models.SmallIntegerField()
    competitions_won = models.SmallIntegerField()
    competitions_lost = models.SmallIntegerField()
    competitions_drawn = models.SmallIntegerField()
    competitions_done_week = models.IntegerField()
    competitions_done_week_classed = models.IntegerField()
    competitions_done_week_non_classed = models.IntegerField()
    competitions_done_week_team = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'olympiad_nobles'


class OlympiadNoblesEom(models.Model):
    charid = models.IntegerField(db_column='charId', primary_key=True)  # Field name made lowercase.
    class_id = models.IntegerField()
    olympiad_points = models.IntegerField()
    competitions_done = models.SmallIntegerField()
    competitions_won = models.SmallIntegerField()
    competitions_lost = models.SmallIntegerField()
    competitions_drawn = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'olympiad_nobles_eom'


class PetitionFeedback(models.Model):
    charname = models.CharField(db_column='charName', max_length=35)  # Field name made lowercase.
    gmname = models.CharField(db_column='gmName', max_length=35)  # Field name made lowercase.
    rate = models.IntegerField()
    message = models.TextField()
    date = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'petition_feedback'


class Pets(models.Model):
    item_obj_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    level = models.SmallIntegerField()
    curhp = models.IntegerField(db_column='curHp', blank=True, null=True)  # Field name made lowercase.
    curmp = models.IntegerField(db_column='curMp', blank=True, null=True)  # Field name made lowercase.
    exp = models.BigIntegerField(blank=True, null=True)
    sp = models.IntegerField(blank=True, null=True)
    fed = models.IntegerField(blank=True, null=True)
    ownerid = models.IntegerField(db_column='ownerId')  # Field name made lowercase.
    restore = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'pets'


class PetsSkills(models.Model):
    templateid = models.SmallIntegerField(db_column='templateId')  # Field name made lowercase.
    minlvl = models.IntegerField(db_column='minLvl')  # Field name made lowercase.
    skillid = models.SmallIntegerField(db_column='skillId')  # Field name made lowercase.
    skilllvl = models.IntegerField(db_column='skillLvl')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pets_skills'
        unique_together = (('templateid', 'skillid', 'skilllvl'),)


class Posts(models.Model):
    post_id = models.IntegerField()
    post_owner_name = models.CharField(max_length=255)
    post_ownerid = models.IntegerField()
    post_date = models.BigIntegerField()
    post_topic_id = models.IntegerField()
    post_forum_id = models.IntegerField()
    post_txt = models.TextField()

    class Meta:
        managed = False
        db_table = 'posts'


class Punishments(models.Model):
    key = models.CharField(max_length=255)
    affect = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    expiration = models.BigIntegerField()
    reason = models.TextField()
    punishedby = models.CharField(db_column='punishedBy', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'punishments'


class QuestGlobalData(models.Model):
    quest_name = models.CharField(max_length=40)
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quest_global_data'
        unique_together = (('quest_name', 'var'),)


class RaidbossSpawnlist(models.Model):
    boss_id = models.SmallIntegerField(primary_key=True)
    amount = models.IntegerField()
    loc_x = models.IntegerField()
    loc_y = models.IntegerField()
    loc_z = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    respawn_random = models.IntegerField()
    respawn_time = models.BigIntegerField()
    currenthp = models.DecimalField(db_column='currentHp', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentmp = models.DecimalField(db_column='currentMp', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'raidboss_spawnlist'


class RainbowspringsAttackerList(models.Model):
    clanid = models.IntegerField(db_column='clanId', blank=True, null=True)  # Field name made lowercase.
    war_decrees_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rainbowsprings_attacker_list'


class RandomSpawn(models.Model):
    groupid = models.IntegerField(db_column='groupId', primary_key=True)  # Field name made lowercase.
    npcid = models.SmallIntegerField(db_column='npcId')  # Field name made lowercase.
    count = models.IntegerField()
    initialdelay = models.IntegerField(db_column='initialDelay')  # Field name made lowercase.
    respawndelay = models.IntegerField(db_column='respawnDelay')  # Field name made lowercase.
    despawndelay = models.IntegerField(db_column='despawnDelay')  # Field name made lowercase.
    broadcastspawn = models.CharField(db_column='broadcastSpawn', max_length=5)  # Field name made lowercase.
    randomspawn = models.CharField(db_column='randomSpawn', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'random_spawn'


class RandomSpawnLoc(models.Model):
    groupid = models.IntegerField(db_column='groupId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'random_spawn_loc'
        unique_together = (('groupid', 'x', 'y', 'z', 'heading'),)


class SevenSigns(models.Model):
    charid = models.IntegerField(db_column='charId', primary_key=True)  # Field name made lowercase.
    cabal = models.CharField(max_length=4)
    seal = models.IntegerField()
    red_stones = models.IntegerField()
    green_stones = models.IntegerField()
    blue_stones = models.IntegerField()
    ancient_adena_amount = models.DecimalField(max_digits=20, decimal_places=0)
    contribution_score = models.DecimalField(max_digits=20, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'seven_signs'


class SevenSignsFestival(models.Model):
    festivalid = models.IntegerField(db_column='festivalId')  # Field name made lowercase.
    cabal = models.CharField(max_length=4)
    cycle = models.IntegerField()
    date = models.BigIntegerField()
    score = models.IntegerField()
    members = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'seven_signs_festival'
        unique_together = (('festivalid', 'cabal', 'cycle'),)


class SevenSignsStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    current_cycle = models.IntegerField()
    festival_cycle = models.IntegerField()
    active_period = models.IntegerField()
    date = models.BigIntegerField()
    previous_winner = models.IntegerField()
    dawn_stone_score = models.DecimalField(max_digits=20, decimal_places=0)
    dawn_festival_score = models.IntegerField()
    dusk_stone_score = models.DecimalField(max_digits=20, decimal_places=0)
    dusk_festival_score = models.IntegerField()
    avarice_owner = models.IntegerField()
    gnosis_owner = models.IntegerField()
    strife_owner = models.IntegerField()
    avarice_dawn_score = models.IntegerField()
    gnosis_dawn_score = models.IntegerField()
    strife_dawn_score = models.IntegerField()
    avarice_dusk_score = models.IntegerField()
    gnosis_dusk_score = models.IntegerField()
    strife_dusk_score = models.IntegerField()
    accumulated_bonus0 = models.IntegerField()
    accumulated_bonus1 = models.IntegerField()
    accumulated_bonus2 = models.IntegerField()
    accumulated_bonus3 = models.IntegerField()
    accumulated_bonus4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seven_signs_status'


class SiegableClanhall(models.Model):
    clanhallid = models.IntegerField(db_column='clanHallId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    ownerid = models.IntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    nextsiege = models.BigIntegerField(db_column='nextSiege', blank=True, null=True)  # Field name made lowercase.
    siegelenght = models.IntegerField(db_column='siegeLenght', blank=True, null=True)  # Field name made lowercase.
    schedule_config = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siegable_clanhall'


class SiegableHallFlagwarAttackers(models.Model):
    hall_id = models.IntegerField()
    flag = models.IntegerField(primary_key=True)
    npc = models.IntegerField()
    clan_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'siegable_hall_flagwar_attackers'


class SiegableHallFlagwarAttackersMembers(models.Model):
    hall_id = models.IntegerField()
    clan_id = models.IntegerField()
    object_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'siegable_hall_flagwar_attackers_members'


class SiegeClans(models.Model):
    castle_id = models.IntegerField()
    clan_id = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    castle_owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siege_clans'
        unique_together = (('clan_id', 'castle_id'),)


class Spawnlist(models.Model):
    location = models.CharField(max_length=40)
    count = models.IntegerField()
    npc_templateid = models.SmallIntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    randomx = models.IntegerField()
    randomy = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    respawn_random = models.IntegerField()
    loc_id = models.IntegerField()
    periodofday = models.IntegerField(db_column='periodOfDay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spawnlist'
        unique_together = (('npc_templateid', 'locx', 'locy', 'locz'),)


class Teleport(models.Model):
    description = models.CharField(db_column='Description', max_length=75, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    loc_x = models.IntegerField(blank=True, null=True)
    loc_y = models.IntegerField(blank=True, null=True)
    loc_z = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    fornoble = models.IntegerField()
    itemid = models.SmallIntegerField(db_column='itemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teleport'


class Territories(models.Model):
    territoryid = models.IntegerField(db_column='territoryId', primary_key=True)  # Field name made lowercase.
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.
    fortid = models.IntegerField(db_column='fortId')  # Field name made lowercase.
    ownedwardids = models.CharField(db_column='ownedWardIds', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territories'


class TerritoryRegistrations(models.Model):
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.
    registeredid = models.IntegerField(db_column='registeredId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territory_registrations'
        unique_together = (('castleid', 'registeredid'),)


class TerritorySpawnlist(models.Model):
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.
    id = models.SmallIntegerField(primary_key=True)
    npcid = models.SmallIntegerField(db_column='npcId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()
    spawntype = models.IntegerField(db_column='spawnType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territory_spawnlist'


class Topic(models.Model):
    topic_id = models.IntegerField()
    topic_forum_id = models.IntegerField()
    topic_name = models.CharField(max_length=255)
    topic_date = models.BigIntegerField()
    topic_ownername = models.CharField(max_length=255)
    topic_ownerid = models.IntegerField()
    topic_type = models.IntegerField()
    topic_reply = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topic'
