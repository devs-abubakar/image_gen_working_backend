from fastapi import FastApi

app = FastApi()

app.get("/generate")
def gen_image(prompt):
    model