import asyncio
import i2plib

async def connect_test(destination):
    session_name = "test-connect"

    # create a SAM stream session
    await i2plib.create_session(session_name)

    # connect to a destination
    reader, writer = await i2plib.stream_connect(session_name, destination)

    remote_host = "udhdrtrcetjm5sxzskjyr5ztpeszydbh4dpl3pl4utgqqw2v4jna.b32.i2p"

    writer.write(f"GET /en/ HTTP/1.0\nHost: {remote_host}\r\n\r\n".encode())
    # write data to a socket
    # writer.write(b"PING")

    # asynchronously receive data
    data = await reader.read(4096)
    print(data.decode())

    # close the connection
    writer.close()

# run event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(connect_test("voanmdeayaccgaxumtehvxxiv4sdscsixoxsqmhh7nfwhusrvfaa.b32.i2p"))
loop.stop()

# import asyncio
# import i2plib
#
# async def connect_test(destination):
#     session_name = "test"
#
#     async with i2plib.Session(session_name):
#         async with i2plib.StreamConnection(session_name, destination) as c:
#
#             c.write(f"GET /en/ HTTP/1.0\nHost: {destination}\r\n\r\n".encode())
#
#
#             # c.write(b"PING")
#             resp = await c.read(4096)
#
#             # print(resp.decode())
#
#
#     print(resp.decode())
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(connect_test("voanmdeayaccgaxumtehvxxiv4sdscsixoxsqmhh7nfwhusrvfaa.b32.i2p"))
# loop.stop()
