from server.database import getconection

colletion = 'sequences'

async def getNextSequence(nome):
    query = {'_id': nome}
    update = { '$inc': { 'seq': 1 } }
    new = 'true'
    sequences_colletion = await getconection(colletion)
    sequence = sequences_colletion.find_one_and_update(query, update)
    return sequence['seq']
     
async def retornarSequence(nome):
    query = {'_id': nome}
    update = { '$inc': { 'seq': -1 } }
    new = 'true'
    sequences_colletion = await getconection(colletion)
    return sequences_colletion.find_one_and_update(query, update)
    
