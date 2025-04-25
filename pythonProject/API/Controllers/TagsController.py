from flask import Blueprint, jsonify, request
from API.UseCases.tagsUseCase import TagsUseCase
from API.Models.Tag import Tag

tags_bp: Blueprint = Blueprint('tags', __name__)
tagUseCase: TagsUseCase = TagsUseCase()

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
