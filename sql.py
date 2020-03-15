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


async def getUserIncome(id):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT Income FROM Jobs INNER JOIN \
                    Userdata ON Userdata.Job = Jobs.Id WHERE Userdata.Id = {id};")
    return await cur.fetchone()


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
    await data.execute(f"INSERT INTO Userdata VALUES({id},{money},0,0,0,0)")
    await data.commit()


# SHOP FUNCTIONS


async def getShopCategories():
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT DISTINCT Category FROM Shop")
    print([item[0] for item in await cur.fetchall()])
    return [item[0] for item in await cur.fetchall()]


async def getShopItems(category = None):
    data = await sqlite.connect(PATH)
    if category == None:
        cur = await data.execute("SELECT Name FROM Shop")
    else:
        cur = await data.execute(f"SELECT Name FROM Shop WHERE Category = {category};")
    return list(await cur.fetchall())


async def getShopItem(name):
    data = await sqlite.connect(PATH)
    cur = await data.execute(f"SELECT * FROM Shop WHERE Name = {name};")
    return list(await cur.fetchall())


# MISCELLANEOUS FUNCTIONS


async def getCurrency():
    data = await sqlite.connect(PATH)
    cur = await data.execute("SELECT Currency FROM Globals")
    return list(await cur.fetchone())[0]


async def execute(cmd):
    data = await sqlite.connect(PATH)
    await data.execute(cmd)
    await data.commit()


asyncio.run(getShopCategories())