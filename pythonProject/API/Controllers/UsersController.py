from flask import Blueprint, jsonify, request

from API.UseCases.usersUseCase import UsersUseCase

user_bp: Blueprint = Blueprint('users', __name__)
usersUseCase = UsersUseCase()

@user_bp.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = usersUseCase.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 500

@user_bp.route('/all', methods=['GET'])
def get_all_users():
    users = usersUseCase.get_all_users()
    if users:
        outList: list = []
        for user in users:
            outList.append(user.to_dict())

        return jsonify(outList), 200
    return jsonify({'error': 'Unable to get all users'}), 500

@user_bp.route('/email/<string:email>', methods=['GET'])
def get_user_by_email(email):
    success, user = usersUseCase.get_user_by_email(email)
    if success:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    response, user = usersUseCase.login(email, password)
    if response:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'Unable to login'}), 400


@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    fName = data['fName']
    lName = data['lName']
    email = data['email']
    password = data['password']

    response, newUser = usersUseCase.register(fName,lName, email, password)
    if response:
        return jsonify(newUser.to_dict()), 200
    return jsonify({'error': 'Unable to login'}), 500

@user_bp.route('/validateSessionToken', methods=['POST'])
async def validate_session_token():
    session_token = request.form.get('sessionToken')
    response, value = await usersUseCase.validate_session_token(session_token)
    if response:
        return jsonify([{'session': value[0].to_dict()}, {'user': value[1].to_dict()}]), 200
    return jsonify({'error': 'Unable to validate session token'}), 500

@user_bp.route('/remove/<string:sessionId>', methods=['POST'])
async def remove_session(sessionId):
    response, value = await usersUseCase.remove_session(sessionId)
    if response:
        return jsonify({'Success': True}), 200
    return jsonify({'error': "Unable to remove session"}), 500

@user_bp.route('/renew/<string:sessionId>', methods=['POST'])
async def renew_session(sessionId):
    response, value = await usersUseCase.renew_session(sessionId)
    if response:
        return jsonify(value.to_dict()), 200
    return jsonify({'error': 'Unable to renew session'}), 500

