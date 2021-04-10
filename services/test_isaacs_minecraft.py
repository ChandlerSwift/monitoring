from mcstatus import MinecraftServer

def test_connection():
    server = MinecraftServer("isaacswift.com", 12345)
    status = server.status()
    assert status.latency < 100
    assert status.version.name.startswith("1.")
