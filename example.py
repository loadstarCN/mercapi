import asyncio
import logging

from mercapi import Mercapi


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


async def main():
    m = Mercapi()
    # results = await m.search('sharpnel')

    # print(f'Found {results.meta.num_found} results')
    # for item in results.items:
    #     print(f'Name: {item.name}\nPrice: {item.price}\n')

    # item = results.items[0]
    # full_item = await item.full_item()
    # print(full_item.description)

    # item = await m.item('m90925725213')
    # print(item)

    profile = await m.profile('362164700')
    # print(profile)
    print("-"*80)

    # items = await profile.items()
    # print(items)

    # print("-"*80)
    reviews = await profile.reviews()
    print(reviews)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
