import i2plib
import asyncio
import requests
from bs4 import BeautifulSoup
#address = 127.0.0.1         port = 7654
async def main():
    dest = await i2plib.new_destination()
    print(dest.base32 + ".b32.i2p")  # print base32 address
    session_nickname = "test-i2p"  # each session must have unique nickname
    _, session_writer = await i2plib.create_session(session_nickname, destination=dest)

    remote_host = "http://2yryi2eb72hnxavjpfot7paiminbzgv5w6fv4sl5wez55ventdeq.b32.i2p"
    reader, writer = await i2plib.stream_connect(session_nickname, remote_host)

    writer.write(f"GET /en/ HTTP/1.0\nHost: {remote_host}\r\n\r\n".encode())


    buflen, resp = 4096, b""
    while 1:
        data = await reader.read(buflen)
        if len(data) > 0:
            resp += data
        else:
            break

    writer.close()
    # print(resp.decode())
    soup = BeautifulSoup(resp.decode(), 'html.parser')
    print(soup.get_text())



asyncio.run(main())
# lis = [0, 1,2,3,4,5,6,7,8,9]
# print(lis[5:len(lis)])


