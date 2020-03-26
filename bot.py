import os
import discord
import pymongo

# Discord bot token
TOKEN = 'NjkwNTM0MDI4MzE0NjczMTUy.XnyZ8w.bsIKcj_Azvy_72aWp_Iv3wNS7TI'

myClient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myClient["mydatabase"]
mycol = mydb["UserKarma"]

if not mycol.find():
    karmaList = [
    {"Name": "Adil", "Opdutter": 0, "Neddutter": 0},
    {"Name": "Chrille", "Opdutter": 0, "Neddutter": 0},
    {"Name": "Hjorth", "Opdutter": 0, "Neddutter": 0},
    {"Name": "Martin", "Opdutter": 0, "Neddutter": 0},
    {"Name": "Magnus", "Opdutter": 0, "Neddutter": 0},
    {"Name": "Simon", "Opdutter": 0, "Neddutter": 0},
    {"Name": "Sten", "Opdutter": 0, "Neddutter": 0}
    ]
    x = mycol.insert_many(karmaList)
    print(x.inserted_ids)

client = discord.Client()

def addOpdut(authorID):
    # ADIL
    if authorID == '100552145421467648':
        mycol.update_one(
            { "Name": "Adil" },
            { "$inc": {"Opdutter": 1}}
        )
    # CHRILLE
    elif authorID == '279307446009462784':
        mycol.update_one(
            { "Name": "Chrille" },
            { "$inc": {"Opdutter": 1}}
        )
    # HJORTH
    elif authorID == '140195461519769601':
        mycol.update_one(
            { "Name": "Hjorth" },
            { "$inc": {"Opdutter": 1}}
        )
    # MARTIN
    elif authorID == '103033943464353792':
        mycol.update_one(
            { "Name": "Martin" },
            { "$inc": {"Opdutter": 1}}
        )
    # MAGNUS 
    elif authorID == '272507977984901120':
        mycol.update_one(
            { "Name": "Magnus" },
            { "$inc": {"Opdutter": 1}}
        )
    # SIMON 
    elif authorID == '619105357473775636':
        mycol.update_one(
            { "Name": "Simon" },
            { "$inc": {"Opdutter": 1}}
        )
    #STEN
    elif authorID == '502882469721407509':
        mycol.update_one(
            { "Name": "Sten" },
            { "$inc": {"Opdutter": 1}}
        )

def removeOpdut(authorID):
    # ADIL
    if authorID == '100552145421467648':
        mycol.update_one(
            { "Name": "Adil" },
            { "$inc": {"Opdutter": -1}}
        )
    # CHRILLE
    elif authorID == '279307446009462784':
        mycol.update_one(
            { "Name": "Chrille" },
            { "$inc": {"Opdutter": -1}}
        )
    # HJORTH
    elif authorID == '140195461519769601':
        mycol.update_one(
            { "Name": "Hjorth" },
            { "$inc": {"Opdutter": -1}}
        )
    # MARTIN
    elif authorID == '103033943464353792':
        mycol.update_one(
            { "Name": "Martin" },
            { "$inc": {"Opdutter": -1}}
        )
    # MAGNUS 
    elif authorID == '272507977984901120':
        mycol.update_one(
            { "Name": "Magnus" },
            { "$inc": {"Opdutter": -1}}
        )
    # SIMON
    elif authorID == '619094316106907658':
        mycol.update_one(
            { "Name": "Simon" },
            { "$inc": {"Opdutter": -1}}
        )
    #STEN
    elif authorID == '502882469721407509':
        mycol.update_one(
            { "Name": "Sten" },
            { "$inc": {"Opdutter": -1}}
        )

def addNeddut(authorID):
    # ADIL
    if authorID == '100552145421467648':
        mycol.update_one(
            { "Name": "Adil" },
            { "$inc": {"Neddutter": 1}}
        )
    # CHRILLE
    elif authorID == '279307446009462784':
        mycol.update_one(
            { "Name": "Chrille" },
            { "$inc": {"Neddutter": 1}}
        )
    # HJORTH
    elif authorID == '140195461519769601':
        mycol.update_one(
            { "Name": "Hjorth" },
            { "$inc": {"Neddutter": 1}}
        )
    # MARTIN
    elif authorID == '103033943464353792':
        mycol.update_one(
            { "Name": "Martin" },
            { "$inc": {"Neddutter": 1}}
        )
    # MAGNUS 
    elif authorID == '272507977984901120':
        mycol.update_one(
            { "Name": "Magnus" },
            { "$inc": {"Neddutter": 1}}
        )
    # SIMON 
    elif authorID == '619105357473775636':
        mycol.update_one(
            { "Name": "Simon" },
            { "$inc": {"Neddutter": 1}}
        )
    #STEN
    elif authorID == '502882469721407509':
        mycol.update_one(
            { "Name": "Sten" },
            { "$inc": {"Neddutter": 1}}
        )

def removeNeddut(authorID):
    # ADIL
    if authorID == '100552145421467648':
        mycol.update_one(
            { "Name": "Adil" },
            { "$inc": {"Neddutter": -1}}
        )
    # CHRILLE
    elif authorID == '279307446009462784':
        mycol.update_one(
            { "Name": "Chrille" },
            { "$inc": {"Neddutter": -1}}
        )
    # HJORTH
    elif authorID == '140195461519769601':
        mycol.update_one(
            { "Name": "Hjorth" },
            { "$inc": {"Neddutter": -1}}
        )
    # MARTIN
    elif authorID == '103033943464353792':
        mycol.update_one(
            { "Name": "Martin" },
            { "$inc": {"Neddutter": -1}}
        )
    # MAGNUS 
    elif authorID == '272507977984901120':
        mycol.update_one(
            { "Name": "Magnus" },
            { "$inc": {"Neddutter": -1}}
        )
    # SIMON 
    elif authorID == '619105357473775636':
        mycol.update_one(
            { "Name": "Simon" },
            { "$inc": {"Neddutter": -1}}
        )
    #STEN
    elif authorID == '502882469721407509':
        mycol.update_one(
            { "Name": "Sten" },
            { "$inc": {"Neddutter": -1}}
        )


@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 619105859615719434:
        # Kurt approved  
        if payload.emoji.id == 619818932475527210:
            message = await client.http.get_message(payload.channel_id, payload.message_id) # Dictionary
            reactUserID = payload.user_id
            strUerID = str(reactUserID)
            authorDict = message["author"]
            authorID = authorDict["id"] # String

            # If user upvotes his own post
            if strUerID == authorID:
                # Should it be -opdut or +neddut?
                removeOpdut(authorID)
                removeOpdut(authorID)
            else:
                addOpdut(authorID)
        # Kurt disapproved
        elif payload.emoji.id == 651028634945060864:
            message = await client.http.get_message(payload.channel_id, payload.message_id) # Dictionary
            authorDict = message["author"]
            authorID = authorDict["id"] # String
            addNeddut(authorID)

# Should it be possible to remove your own upvote to your own post?
# Or should the karma whores stay punished?
@client.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == 619105859615719434:
        # Kurt approved
        if payload.emoji.id == 619818932475527210:
            message = await client.http.get_message(payload.channel_id, payload.message_id) # Dictionary
            authorDict = message["author"]
            authorID = authorDict["id"] # String
            removeOpdut(authorID)
        # Kurt disapproved
        elif payload.emoji.id == 651028634945060864:
            message = await client.http.get_message(payload.channel_id, payload.message_id) # Dictionary
            authorDict = message["author"]
            authorID = authorDict["id"] # String
            removeNeddut(authorID)

@client.event
async def on_message(message):
    if message.content == "!karma":
        # ADIL
        if message.author.id == 100552145421467648:
            x = mycol.find_one({"Name": "Adil"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))
        # CHRILLE
        elif message.author.id == 279307446009462784:
            x = mycol.find_one({"Name": "Chrille"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))
        # HJORTH
        if message.author.id == 140195461519769601:
            x = mycol.find_one({"Name": "Hjorth"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))
        # MARTIN
        elif message.author.id == 103033943464353792:
            x = mycol.find_one({"Name": "Martin"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))
        # MAGNUS 
        elif message.author.id == 272507977984901120:
            x = mycol.find_one({"Name": "Magnus"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))
        # SIMON
        elif message.author.id == 619105357473775636:
            x = mycol.find_one({"Name": "Simon"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))
        #STEN
        elif message.author.id == 502882469721407509:
            x = mycol.find_one({"Name": "Sten"})
            await message.channel.send('{} has {} total karma. {} opdutter and {} neddutter'.format(x["Name"], x["Opdutter"] - x["Neddutter"], x["Opdutter"], x["Neddutter"]))

    # Hidden easter egg for the boys
    if message.content == "!bot":
        await message.channel.send('Botten er så tæt på at være færdig :pinching_hand:')

# When the bot succesfully joins the discord server.
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for document in mycol.find():
        print(document)

client.run(TOKEN)