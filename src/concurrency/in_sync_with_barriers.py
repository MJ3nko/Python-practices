import asyncio


async def game_loop():
    barrier = asyncio.Barrier(3)

    while True:
        print("/////////////// FRAME START ////////////////////////", flush=True)
        await asyncio.gather(
            compute_physics(barrier),
            get_input(barrier),
            render_scene(barrier)
        )
        print(r"\\\\\\\\\\\\\\\\\\\\\\ FRAME END \\\\\\\\\\\\\\")
        print()


async def render_scene(barrier: asyncio.Barrier):
    print("Rendering scene!")
    await asyncio.sleep(1.5)
    await barrier.wait()
    print("Rendering done.")
    await asyncio.sleep(0.25)


async def compute_physics(barrier: asyncio.Barrier):
    print("Computing physics!")
    await asyncio.sleep(0.75)
    await barrier.wait()
    print("Physics done.")
    await asyncio.sleep(0.25)


async def get_input(barrier: asyncio.Barrier):
    print("Getting input!")
    await asyncio.sleep(1)
    await barrier.wait()
    print("Input done.")
    await asyncio.sleep(0.25)


def main():
    print("Running game loop!\n")
    asyncio.run(game_loop())


if __name__ == "__main__":
    main()
