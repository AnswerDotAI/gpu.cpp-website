from fasthtml.common import *
from functools import cache
import uvicorn

app = FastHTMLWithLiveReload(
    hdrs=picolink,
)
rt = app.route


@app.get("/{fname:path}.{ext:static}")
async def static(fname: str, ext: str):
    return FileResponse(f"{fname}.{ext}")


@cache
def page():
    font_size = 8.0
    hero_style = f"font-size: {font_size}em; display: inline; font-family: 'Helvetica';"
    box_style = f"""
        background-color: #ffffff12;
        width: 15em;
        margin: 12px;
        padding: 8px;
        border-radius: 4px;
        backdrop-filter: blur(3px);
        -webkit-backdrop-filter: blur(2px);
        color: white;
        font-size: {font_size / 8.0}em;
        text-align: center;
        box-shadow: 0 0 20px 0 rgba(48, 48, 48, 0.3);
        display: inline-block;
        transition: background-color 0.3s ease;
    """
    body_style = """
        background: linear-gradient(rgba(14, 14, 14, 0.86),
                                    rgba(0, 0, 0, 0.95),
                                    rgba(0, 0, 0, 0.92), 
                                    rgba(0, 0, 0, 0.89), 
                                    rgba(28, 28, 28, 0.80)), 
                    url('images/shadertui2-small-crop2-loop.gif');
        background-size: cover;
        background-position: center;
        height: 100vh
    """
    link_style = "text-decoration: none; color: #44449EFF; font-size: 1.3em;  font-family: 'Helvetica';"
    return Title("gpu.cpp"), Body(
        Div(
            style="height: 16%;",
        ),
        Div(
            H1(
                "gpu",
                style=hero_style + " color:#ee4c2cFF;",
            ),
            H1(
                ".",
                style=hero_style + " color:#BBBBBBFF;",
            ),
            H1(
                "cpp",
                style=hero_style + " color:#808080FF;",
            ),
            align="center",
        ),
        P(),
        Div(
            "Portable GPU Compute with C++ & WebGPU",
            align="center",
            style=f"text-decoration: none; color: #88888899; font-size: 1.58em; font-family: 'Helvetica';",
        ),
        P(),
        Div(
            Div(
                A(
                    # Img(src="images/github.svg", style="filter: invert(1);"),
                    "GitHub",
                    href="https://github.com/AnswerDotAI/gpu.cpp",
                    style=link_style,
                ),
                style=box_style,
            ),
            Div(
                A(
                    "Blog Post",
                    href="https://www.answer.ai/posts/2024-07-11--gpu-cpp.html",
                    style=link_style,
                ),
                style=box_style,
            ),
            Br(),
            Div(
                A(
                    "API Docs",
                    href="api/index.html",
                    style=link_style,
                ),
                style=box_style,
            ),
            Div(
                A(
                    "Discord",
                    href="https://discord.gg/zmJVhXsC7f",
                    style=link_style,
                ),
                style=box_style,
            ),
            align="center",
        ),
        P(),
        Div(
            A(
                "Answer.AI",
                href="https://www.answer.ai",
                style=f"text-decoration: none; color: #88888899; font-size: 1.58em ; font-family: 'Helvetica';",
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
