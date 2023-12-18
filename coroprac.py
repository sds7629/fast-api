import asyncio
import time

## async
# async def sleep(sec):
#     await asyncio.sleep(sec)
#     return sec


# async def main():
#     sec_list = [1, 2]
#     tasks = [asyncio.create_task(sleep(sec)) for sec in sec_list]
#     tasks_results = await asyncio.gather(*tasks)
#     return tasks_results


# start = time.time()

# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(main())
# loop.close()

# end = time.time()

# print(f"result : {result}")
# print("total time: {0:.2f}sec".format(end - start))

## sync


def sleep(sec):
    time.sleep(sec)
    return sec


def main():
    sec_list = [1, 2]
    tasks = [sleep(sec) for sec in sec_list]
    return tasks


start = time.time()
result = main()
end = time.time()

print(f"result : {result}")
print("total time: {0:.2f}sec".format(end - start))
