from __future__ import annotations

from dotenv import load_dotenv; load_dotenv(".env.ServerService")
from os import getenv; import typing

from dataclasses import dataclass

mzhr_: typing.Any = lambda ANY: ANY if ANY is not None else None
@dataclass
class _ServerServiceData:
    MZHR_SERVER_DEBUG: bool = mzhr_(getenv("MZHR_SERVER_DEBUG"))

    MZHR_SERVER_CONNECTION_ADDRESS: str = mzhr_(getenv("MZHR_SERVER_CONNECTION_ADDRESS"))
    MZHR_SERVER_CONNECTION_PORT: int = mzhr_(getenv("MZHR_SERVER_CONNECTION_PORT"))
    MZHR_SERVER_CONNECTION_PASSWORD: str = mzhr_(getenv("MZHR_SERVER_CONNECTION_PASSWORD"))

from flask import Flask, jsonify, Response, request
application: Flask = Flask(__name__)

@application.errorhandler(403)
def _etomazhor_forbidden_error(error: typing.Any = None) -> Response: return jsonify({"content": "Forbidden_403"}), 403

@application.errorhandler(404)
def _etomazhor_notfound_error(error: typing.Any = None) -> Response: return jsonify({"content": "NotFound_404"}), 404

@application.route("/etomazhor_service", methods=["GET"])
def _etomazhor_service_request() -> Response:
    return jsonify({"ip":_ServerServiceData.MZHR_SERVER_CONNECTION_ADDRESS,"port":_ServerServiceData.MZHR_SERVER_CONNECTION_PORT,
        "password":_ServerServiceData.MZHR_SERVER_CONNECTION_PASSWORD})

if __name__ == '__main__': application.run(debug=True if _ServerServiceData.MZHR_SERVER_DEBUG == "TRUE" else False)
