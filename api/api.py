class User(db.Model):
    ......
    def to_json(self):
        json_user = {
            'id': self.id,
            'username': self.username
        }
        return json_user
    ......


class User(db.Model):
    ......
    @staticmethod
    def from_json(json_data):
        user = User(
            username = json_data.get('username'),
            password = json_data.get('password')
        )
        return user
    ......

/api/users.py

from flask import request

@api.route('/users/', methods=['POST'])
def create_user():
    user = User.from_json(request.get_json())
    db.session.add(user)
    db.session.commit()

@api.route('/users/', methods=['GET'])
def get_users():
    """获取用户资源集合"""
    pass

@api.route('/users/<int:id>/', methods=['GET'])
def get_id_users(id):
    """获取特定id用户资源"""
    pass

@api.route('/users/', methods=['GET', 'POST'])
def create_user():
    """创建用户资源"""
    pass

@api.route('/users/<int:id>/', methods=['GET', 'PUT'])
def update_id_user(id):
    """更新特定id用户资源"""
    pass

@api.route('/users/<int:id>/', methods=['GET', 'DELETE'])
def delete_id_user(id):
    """删除特定id用户"""
    pass
