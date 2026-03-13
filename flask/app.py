from flask import Flask, request, jsonify
from db import Session, User

app = Flask(__name__)

@app.route("/create", methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get("name")
    print("name is: ", name)
    email = data.get("email")
    print("email is: ", email)

    # checking data
    if not name or not email:
        return jsonify({"error": "soz you need to provide name and email"}), 400
    
    session = Session()

    try:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        return jsonify({"message": "user created successfully"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=True)