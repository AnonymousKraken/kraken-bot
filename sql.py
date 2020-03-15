import asyncio
import aiosqlite3 as sqlite

PATH = "storage/data.db"


# USER FUNCTIONS


async def userExists(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Id FROM Userdata WHERE Userdata.Id = {id};")
    return await cur.fetchone() != None


async def getUserMoney(id):
    data = await sqlite.connect(PATH)
    cur = await data.cursor()
    await cur.execute(f"SELECT Money FROM Userdata WHERE Userdata.Id = {id};")
    return list(await cur.fetchone())[0]


async def getUserJob(id):
    data = await sqlite.connect(PATH)
    cur = await data.cursor()
    await cur.execute(f"SELECT Job FROM Userdata WHERE Userdata.Id = {id};")
    return list(await cur.fetchone())[0]


async def getUserAntivirus(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Antivirus FROM Userdata WHERE Userdata.Id = {id};")
    return await bool(cur.fetchone())


async def getUserVaccinated(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Vaccinated FROM Userdata WHERE Userdata.Id = {id};")
    return await bool(cur.fetchone())


async def getUserSick(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Sick FROM Userdata WHERE Userdata.Id = {id};")
    return await bool(cur.fetchone())


async def setUserMoney(id, amount):
    data = await sqlite.connect(PATH)
    await data.execute(f"UPDATE Userdata SET Money = {amount} WHERE Userdata.Id = {id};")
    await data.commit()


async def addUserMoney(id, amount):
    data = await sqlite.connect(PATH)
    await data.execute(f"UPDATE Userdata SET Money = Userdata.Money + {amount} WHERE Userdata.Id = {id};")
    await data.commit()


async def createUser(id, money=0):
    data = await sqlite.connect(PATH)
    await data.execute(f"INSERT INTO Userdata VALUES({id},{money},0)")
    await data.commit()


# JOB FUNCTIONS


async def getJobIds():
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT RoleId FROM Jobs")
    return [item[0] for item in await cur.fetchall()]


async def getJobName(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Name FROM Jobs WHERE RoleId = {id};")
    return list(await cur.fetchone())[0]


async def getJobIncome(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Income FROM Jobs WHERE RoleId = {id};")
    return list(await cur.fetchone())[0]


# SHOP FUNCTIONS


async def getShopCategories():
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT DISTINCT Category FROM Shop")
    return [item[0] for item in await cur.fetchall()]


async def getShopItems(category = None):
    data = await sqlite.connect(PATH)
    if category == None:
        cur = await data.execute("SELECT Name FROM Shop")
    else:
        cur = await data.execute(f"SELECT Name FROM Shop WHERE Category = \"{category}\";")
    return [item[0] for item in await cur.fetchall()]


async def getItemCategory(name):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Category FROM Shop WHERE Name = \"{name}\";")
    return list(await cur.fetchone())[0]


async def getItemDescription(name):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Description FROM Shop WHERE Name = \"{name}\";")
    return list(await cur.fetchone())[0]


async def getItemPrice(name):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Price FROM Shop WHERE Name = \"{name}\";")
    return list(await cur.fetchone())[0]


async def giveItem(id, item, quantity=1):
    data = await sqlite.connect(PATH)
    await data.execute(f"UPDATE Userdata SET {item} = Userdata.{item} + {quantity} WHERE Userdata.Id = {id};")
    data.commit()


async def removeItem(id, item, quantity=1):
    data = await sqlite.connect(PATH)
    await data.execute(f"UPDATE Userdata SET {item} = Userdata.{item} - {quantity} WHERE Userdata.Id = {id};")
    data.commit()


# MISCELLANEOUS FUNCTIONS


async def getCurrency():
    data = await sqlite.connect(PATH)
    cur = await data.execute("SELECT Currency FROM Globals")
    return list(await cur.fetchone())[0]


async def execute(cmd):
    data = await sqlite.connect(PATH)
    await data.execute(cmd)
    await data.commit()