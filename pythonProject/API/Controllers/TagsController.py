from flask import Blueprint, jsonify, request
from API.UseCases.tagsUseCase import TagsUseCase
from API.UseCases.gameTagsUseCase import GameTagsUseCase
from API.Models.Tag import Tag

tags_bp: Blueprint = Blueprint('tags', __name__)
tagUseCase: TagsUseCase = TagsUseCase()
gameTagsUseCase: GameTagsUseCase = GameTagsUseCase()

@tags_bp.route('/newTag', methods=['POST'])
def new_tag():
    data = request.get_json()
    name = data['name']

    result, newTag = tagUseCase.add_new_tag(name)
    if result:
        return jsonify(newTag.to_dict()), 200
    return jsonify({'error': 'Unable to create new Tag'}), 500

@tags_bp.route('/getAllTags', methods=['GET'])
def get_all_tags():
    result, tags = tagUseCase.get_all_tags()
    if result:
        returnTags = []
        for tag in tags:
            returnTags.append(tag.to_dict())
        return jsonify(returnTags), 200
    return jsonify({'error': 'Unable to get all Tags'}), 500

@tags_bp.route('/getTagsForGame/<int:gameId>', methods=['GET'])
def get_tags_for_game(gameId):
    result, tags = gameTagsUseCase.get_tags_for_game(gameId)
    if result:
        returnTags = []
        for tag in tags:
            returnTags.append(tag.to_dict())
        return jsonify(returnTags), 200
    return jsonify({'error': 'Unable to get tags for game'}), 500