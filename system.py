from __future__ import annotations

from dataclasses import dataclass
from valve.source import a2s
import socket

@dataclass
class ServerConfiguration:
    mazhor_css_ip: str = "195.201.70.82"
    mazhor_css_port: int = 27015
    mazhor_css_password: int = "opaopaetomazhor"

def request_server() -> dict | None:
    try:
        with a2s.ServerQuerier((ServerConfiguration.mazhor_css_ip, ServerConfiguration.mazhor_css_port)) as valve_server:
            server_information = valve_server.info()
            players = valve_server.players()
            return {
                "name": server_information["server_name"], "map": server_information["map"],
                "game": server_information["game"], "vac": server_information["vac_enabled"],
                "version": server_information["version"], "players": f'{server_information["player_count"]}/{server_information["max_players"]}',
                "players_list": [player["name"] for player in players["players"]],}
    except (socket.timeout, a2s.NoResponseError): return None

__all__ = ["request_server", "Configuration"]
