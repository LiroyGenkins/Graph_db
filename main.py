from fastapi import FastAPI
from session_controller import NebulaSession

app = FastAPI()
sess = NebulaSession()


@app.on_event("shutdown")
def shutdown_event():
    sess.close_session()
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")


@app.get("/{space}/name={name}")
async def make_request(space: str, name: str):
    name = name[1:-1]
    print(name)
    resp = sess.session.execute(
        f'USE {space};MATCH (p:person {{name: "{name}"}})-[e:event]-() RETURN e AS events'
    )
    resp = resp if resp.is_succeeded() else resp.error_msg()
    return resp
