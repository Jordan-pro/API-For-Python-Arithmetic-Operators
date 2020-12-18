from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)  # Flask("Jordan")
api = Api(app)


# @app.route('/services')
# def service_page():
#     return 'I will become a millionaire'
#
#
# @app.route('/maths')
# def maths_page():
#     #  preparing a response that come to maths_page
#     x = 30 * 3
#     s = str(x)
#     # x = 100/2
#
#     retJson = {
#         'Name':'Jordan',
#         'Age': 28,
#         'Phones':[
#             {
#                 'PhoneName':'Techno-Camon 16',
#                 'PhoneNum':'237655555555'
#             },
#             {
#                 'PhoneName': 'Techno-Camon 11',
#                 'PhoneNum': '237677777777'
#             },
#             {
#                 'PhoneName': 'IPad 2',
#                 'PhoneNum': '237611111111'
#             }
#         ]
#     }
#     return retJson


def checkPostedData(postedData, functionName):
    if functionName == "add" or "subtract" or "multiply" or "modulus" or "exponential" or "floordiv":
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif functionName == "division":
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        # If i'm here, then the resource Add was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "add")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data:
        ret = x + y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        # If i'm here, then the resource Division was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "division")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Division the posted data:
        ret = (x * 1.0) / y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        # If i'm here, then the resource Subtract was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "subtract")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Subtract the posted data:
        ret = x - y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        # If i'm here, then the resource Multiply was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "multiply")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Multiply the posted data:
        ret = x * y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


class Modulus(Resource):
    def post(self):
        # If i'm here, then the resource Modulus was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "modulus")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Modulus the posted data:
        ret = x % y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


class Exponential(Resource):
    def post(self):
        # If i'm here, then the resource Exponential was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "exponential")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Exponential the posted data:
        ret = x ** y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


class Floordiv(Resource):
    def post(self):
        # If i'm here, then the resource Floor Division was requested using the method POST

        # Step 1a: Get posted data:
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data:
        status_code = checkPostedData(postedData, "floordiv")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "status code": status_code
            }
            return jsonify(retJson)

        # If i'm here that means status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Floor Division the posted data:
        ret = x // y
        retMap = {
            'sum': ret,
            'status code': 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Divide, "/division")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Modulus, "/modulus")
api.add_resource(Exponential, "/exponential")
api.add_resource(Floordiv, "/floordiv")


@app.route('/add')  # 127.0.0.1/5000
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)