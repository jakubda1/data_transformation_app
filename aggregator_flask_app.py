from flask import Flask, request, jsonify, make_response
from datahandler import DataHandler
from functools import wraps

app = Flask(__name__)

#                                   ....
#                                 .'' .'''
# .                             .'   :
# \\                          .:    :
#  \\                        _:    :       ..----.._
#   \\                    .:::.....:::.. .'         ''.
#    \\                 .'  #-. .-######'     #        '.
#     \\                 '.##'/ ' ################       :
#      \\                  #####################         :
#       \\               ..##.-.#### .''''###'.._        :
#        \\             :--:########:            '.    .' :
#         \\..__...--.. :--:#######.'   '.         '.     :
#         :     :  : : '':'-:'':'::        .         '.  .'
#         '---'''..: :    ':    '..'''.      '.        :'
#            \\  :: : :     '      ''''''.     '.      .:
#             \\ ::  : :     '            '.      '      :
#              \\::   : :           ....' ..:       '     '.
#               \\::  : :    .....####\\ .~~.:.             :
#                \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
#                 \\    .'  ########## \ \ _.' '. '-.       '''.
#                 :\\  :     ########   \ \      '.  '-.        :
#                :  \\'    '   #### :    \ \      :.    '-.      :
#               :  .'\\   :'  :     :     \ \       :      '-.    :
#              : .'  .\\  '  :      :     :\ \       :        '.   :
#              ::   :  \\'  :.      :     : \ \      :          '. :
#              ::. :    \\  : :      :    ;  \ \     :           '.:
#               : ':    '\\ :  :     :     :  \:\     :        ..'
#                  :    ' \\ :        :     ;  \|      :   .'''
#                  '.   '  \\:                         :.''
#                   .:..... \\:       :            ..''
#                  '._____|'.\\......'''''''.:..'''
#                             \\
ACCESS_TOKENS = ["YouShallNotPass!"]


def token_required(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token not in ACCESS_TOKENS:
            return make_response(jsonify({"message": "Unauthorized!"}))
        else:
            return f(*args, **kwargs)
    return decoration


# Ve WebApp definujte 1 POST endpoint (/api/v1/parse-me/), ktery bude prijimat 2 parametry:
# args -> pole klicu pro vystup (vnoreny slovnk)
# json_data -> vstup jako v prvni casti ulohy (raw vstup, ne soubor)
@app.route("/api/v1/parse-me/", methods=["POST"])
@token_required
def parse_me_view():

    req_json_data = request.json['json_data']  # will result in
    # to ERR 500 if not provided -> mandatory
    req_args = request.json['args']  # will result into ERR 500 if not provided -> mandatory
    dh = DataHandler()
    dh.from_json(req_json_data)
    aggregated_data = dh.aggregate_by_keys(req_args)
    return jsonify(aggregated_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
