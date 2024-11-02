import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    delay = 1 / power
    for i in range(5):
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял шар {i+1}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Andrey', 5))
    task2 = asyncio.create_task(start_strongman('Alex', 4))
    task3 = asyncio.create_task(start_strongman('Nick', 3))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())