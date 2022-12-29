from game_server.protocol.cmd_id import CmdID
from game_server import HandlerRouter,Connection
from game_server.utils.time import current_milli_time
from lib.proto import GetPlayerMpModeAvailabilityReq, GetPlayerMpModeAvailabilityRsp, PlayerLuaShellNotify
import enet

router = HandlerRouter()

@router(CmdID.GetPlayerMpModeAvailabilityReq)
def handle_Mp(conn: Connection, msg: GetPlayerMpModeAvailabilityReq):
    rsp = PlayerLuaShellNotify()
    rsp.id=1
    file = open('C:\\Users\\nikur\\Downloads\\saturnine-master\\saturnine-master\\Windy\\script.lua',"rb")
    rsp.lua_shell = file.read()
    file.close()
    conn.send(rsp)