from fasthtml.common import *
from functools import cache
import uvicorn

TARGET = "debug"

if TARGET == "release":
    app = FastHTML(hdrs=picolink)
else:
    app = FastHTMLWithLiveReload(hdrs=picolink)

rt = app.route


@app.get("/api/{fname:path}.{ext:static}")
async def api(fname: str, ext: str):
    return FileResponse(f"api/{fname}.{ext}")


@app.get("/images/{fname:path}.{ext:static}")
async def images(fname: str, ext: str):
    return FileResponse(f"images/{fname}.{ext}")


@cache
def page():
    font_family = "font-family: 'Helvetica';"
    hero_style = f"font-size: 7.6em; display: inline; {font_family}"

    box_style = f"""
        background-color: #ffffff12;
        width: 8em;
        margin: 12px;
        padding: 8px;
        border-radius: 4px;
        backdrop-filter: blur(3px);
        -webkit-backdrop-filter: blur(2px);
        text-align: center;
        box-shadow: 0 0 20px 0 rgba(48, 48, 48, 0.3);
        display: inline-block;
    """
    body_style = """
        background: linear-gradient(rgba(14, 14, 14, 0.86),
                                    rgba(0, 0, 0, 1.0),
                                    rgba(0, 0, 0, 0.92), 
                                    rgba(0, 0, 0, 0.89), 
                                    rgba(28, 28, 28, 0.80)), 
                    url('images/shadertui2-small-crop2-loop.gif');
        background-size: cover;
        background-position: center;
        height: 100vh
    """
    link_style = (
        "text-decoration: none; color: #44449EFF; font-size: 1.58em; {font_family}"
    )
    return Title("gpu.cpp"), Body(
        Div(
            style="height: 12%;",
        ),
        Div(
            H1(
                "gpu",
                style=hero_style + " color:#ee4c2cFF;",
            ),
            H1(
                ".",
                style=hero_style + " color:#808080FF;",
            ),
            H1(
                "cpp",
                style=hero_style + " color:#B4B4B4FF;",
            ),
            align="center",
        ),
        P(),
        Br(),
        Br(),
        Div(
            "Portable C++ GPU Compute using WebGPU",
            align="center",
            style=f"text-decoration: none; color: #808080FF; font-size: 1.58em; {font_family}",
        ),
        P(),
        Div(
            A(
                Div(
                    "GitHub",
                    style=box_style + link_style,
                ),
                href="https://github.com/AnswerDotAI/gpu.cpp",
                style="text-decoration: none;",
            ),
            A(
                Div(
                    "Blog Post",
                    style=box_style + link_style,
                ),
                href="https://www.answer.ai/posts/2024-07-11--gpu-cpp.html",
                style="text-decoration: none;",
            ),
            Br(),
            A(
                Div(
                    "API Docs",
                    style=box_style + link_style,
                ),
                href="api/index.html",
                style="text-decoration: none;",
            ),
            A(
                Div(
                    "Discord",
                    style=box_style + link_style,
                ),
                href="https://discord.gg/zmJVhXsC7f",
                style="text-decoration: none;",
            ),
            align="center",
        ),
        P(),
        Div(
            A(
                "— Answer.AI —",
                href="https://www.answer.ai",
                style=f"text-decoration: none; color: #303030FF; font-size: 1.58em ; {font_family}",
            ),
            align="center",
        ),
        style=body_style,
    )


@rt("/")
def get():
    return page()


if __name__ == "__main__":
    run_uv(
        fname=None,
        app="app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
