import base64

script = """
... // your JavaScript code here ...
"""

encoded_script = base64.b64encode(script.encode()).decode()
