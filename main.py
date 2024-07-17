from fasthtml.common import *
import uvicorn

app = FastHTMLWithLiveReload(
    hdrs=picolink,
)
rt = app.route


# For images, CSS, etc.
@app.get("/{fname:path}.{ext:static}")
async def static(fname: str, ext: str):
    return FileResponse(f"{fname}.{ext}")


@rt("/")
def get():
    font_size = 8.0
    hero_style = f"font-size: {font_size}em; display: inline;"
    box_style = f"""
        background-color: #22222277;
        width: 20%;
        margin: 10px;
        padding: 8px;
        border-radius: 3px;
        color: white;
        font-size: {font_size / 8.0}em;
        text-align: center;
        
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
        display: inline-block;
        transition: background-color 0.3s ease;
    """
    body_style = """
        background: linear-gradient(rgba(14, 14, 14, 0.87),
                                    rgba(0, 0, 0, 0.94),
                                    rgba(0, 0, 0, 0.9), 
                                    rgba(0, 0, 0, 0.88), 
                                    rgba(32, 32, 32, 0.88)), 
                    url('images/shadertui2-small-crop2.gif');
        background-size: cover;
        background-position: center;
        height: 100vh
    """
    link_style = "text-decoration: none; color: #4F4F9EFF;"
    return Title("gpu.cpp"), Body(
        Div(
            style="height: 16%;",
        ),
        Div(
            H1(
                "gpu",
                style=hero_style + " color:#ee4c2cF0;",
            ),
            H1(
                ".",
                style=hero_style + " color:#BBBBBBF0;",
            ),
            H1(
                "cpp",
                style=hero_style + " color:#808080F0;",
            ),
            align="center",
        ),
        P(),
        Div(
            "Portable GPU Compute with C++ & WebGPU",
            align="center",
            style=f"text-decoration: none; color: #66666699; font-weight: bold;",
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
                    "Intro Blog",
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
                style=f"text-decoration: none; color: #66666699; font-weight: bold;",
            ),
            align="center",
        ),
        style=body_style,
    )


if __name__ == "__main__":
    run_uv(
        fname=None,
        app="app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
