from __future__ import annotations

import socket, requests

from dataclasses import dataclass
@dataclass
class _ApplicationData:
    MZHR_REQUEST_ADDRESS: str = "http://127.0.0.1:5000/etomazhor_service"
from valve.source import a2s

def _request_from_mazhor_service() -> dict | None:
    try:
        response: requests.Response = requests.get(url=_ApplicationData.MZHR_REQUEST_ADDRESS)
        if response.status_code != 200: return None
        return response.json() if response.json() is not None else None
    except Exception as e: return None

def request_server() -> dict | None:
    mazhor_service_response: dict | None = _request_from_mazhor_service()
    if mazhor_service_response is None: return None
    try:
        with a2s.ServerQuerier((mazhor_service_response["ip"], int(mazhor_service_response["port"]))) as valve_server:
            server_information = valve_server.info()
            players = valve_server.players()
            return { "password": mazhor_service_response["password"], "name": server_information["server_name"], "map": server_information["map"],
                "game": server_information["game"], "vac": server_information["vac_enabled"], "players_list": [player["name"] for player in players["players"]],
                "version": server_information["version"], "players": f'{server_information["player_count"]}/{server_information["max_players"]}',
                "ip": mazhor_service_response["ip"], "port": mazhor_service_response["port"],}
    except (socket.timeout, a2s.NoResponseError): return None

__all__ = ["request_server"]
