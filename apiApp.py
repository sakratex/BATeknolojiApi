from flask import Flask, jsonify,request


Practices = [
    {
        "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
        "title": "Say hello with python",
        "problem": "Print hello world in Python using print",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "",
        "expected_output": "Hello World"
    },
    {
        "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
        "title": "Arithmetic Operators - Sum",
        "problem": "Sum two numbers",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "5,6",
        "expected_output": "11"
    },
    {
        "id": '23',
        "title": "Loops",
        "problem": "Print the square of each number in the loop step",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "4",
        "expected_output": "0,1,4,9"
    }
]

apiApp = Flask(__name__)


@apiApp.route('/BATeknoloji/Api/Pratices', methods=['GET'])
def getPratices():
    return jsonify({'Practices': Practices})


@apiApp.route('/BATeknoloji/Api/Pratices/<string:Practice_id>', methods=['GET'])
def getPratice(Practice_id):
    Practice = [Practice for Practice in Practices if Practice['id'] == Practice_id]
    if len(Practice) == 0:
        return jsonify({'Pratice': 'Not Found !!!'}), 404
    return jsonify({'Pratice': Practice})


@apiApp.route('/BATeknoloji/Api/Pratices', methods=['POST'])
def createPratice():
    newPratice = {
        "id": request.json['id'],
        "title": request.json['title'],
        "problem": request.json['problem'],
        "point": 1,
        "level": request.json['level'],
        "language": request.json['language'],
        "input": request.json['input'],
        "expected_output": request.json['expected_output']
    }
    Practices.append(newPratice)
    return jsonify({'Pratice': newPratice}), 201


@apiApp.route('/BATeknoloji/Api/Pratices/<string:Practice_id>', methods=['DELETE'])
def deletePratice(Practice_id):
    Practice = [Practice for Practice in Practices if Practice['id'] == Practice_id]
    if len(Practice) == 0:
        return jsonify({'Pratice': 'Not found !!!'}), 404
    Practices.remove(Practice[0])
    return jsonify({'Pratice Deleted Succes!':Practice_id, 'result': True})


if __name__ == '__main__':
    apiApp.run(debug=True)

"""
-Eren KÖSE
"""