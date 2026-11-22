"""PyLabRobot resource bookkeeping with a chatterbox, without liquid or hardware."""
import asyncio
import json
from pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.liquid_handling.backends import LiquidHandlerChatterboxBackend
from pylabrobot.resources import Container, Coordinate, Deck, Tip, TipSpot, set_volume_tracking

async def main():
    set_volume_tracking(True)
    deck = Deck(size_x=300, size_y=200, size_z=200)
    source = Container('source', 20, 20, 30, max_volume=1000)
    destination = Container('destination', 20, 20, 30, max_volume=1000)
    tip = TipSpot('tip', 10, 10, make_tip=lambda: Tip(False, 50, 200, 5))
    for resource, x in [(source, 50), (destination, 100), (tip, 150)]:
        deck.assign_child_resource(resource, location=Coordinate(x, 50, 0))
    source.tracker.set_volume(200)
    destination.tracker.set_volume(0)
    handler = LiquidHandler(backend=LiquidHandlerChatterboxBackend(num_channels=1), deck=deck)
    await handler.setup()
    try:
        await handler.pick_up_tips([tip], use_channels=[0])
        await handler.aspirate([source], vols=[50], use_channels=[0])
        await handler.dispense([destination], vols=[50], use_channels=[0])
        await handler.return_tips()
        remaining = source.tracker.get_used_volume()
        transferred = destination.tracker.get_used_volume()
        assert remaining == 150 and transferred == 50
        print(json.dumps({'mode': 'chatterbox', 'source_uL': remaining,
                          'destination_uL': transferred, 'physical_transfer': False}))
    finally:
        await handler.stop()

asyncio.run(main())
