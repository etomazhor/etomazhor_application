from __future__ import annotations

from flask import Flask, jsonify, Response
application: Flask = Flask(__name__)

@application.route("/etomazhor_service", methods=["GET"])
def _etomazhor_service_request() -> Response:
    return jsonify({"ip":"195.201.70.82","port":27015,"password":"opaopaetomazhor"})

# [NOTE][DBEUG_SWTCH]
if __name__ == '__main__': application.run(debug=True)
