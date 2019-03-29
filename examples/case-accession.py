import pyriandx

client = pyriandx.client(
    email="xxxxx",
    key="xxxxx",
    institution="melbournetest"
    )

data = {}
data["accessionNumber"] = "1111"
client.create_case(data)