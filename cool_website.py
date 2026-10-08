from flask import Flask
from flask_cors import CORS

core = Flask(__name__)

@core.route("/")
def Hello():
	return """
	<html>
	<head>
		<title>Hi</title>
	</head>
	<body>
		<p>
		I committed something\n\r
		-ndevbit
		</p>
		<button>Hi</button>
	</body>
	</html>
"""

if __name__ == '__main__':
	core.run(port=5001)
