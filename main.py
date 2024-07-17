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
    box_style = f"""
        background-color: #22222266;
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
    hover_style = """
        .hover-box:hover {
            background-color: blue;
        }
    """
    # center background image
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

    return Title("FastHTML"), Body(
            Div(
                style="height: 16%;",
            ),
        Div(
            H1(
                "gpu",
                style=f"font-size: {font_size}em; color:#ee4c2cF0; display: inline;",
            ),
            H1(
                ".",
                # style=f"font-size: {font_size}em; display: inline; color:#0F0D8EFF;",
                style=f"font-size: {font_size}em; display: inline; color:#FFFFFFF0;",
            ),
            H1(
                "cpp",
                style=f"font-size: {font_size}em; display: inline; color:#808080F0;",
            ),
            align="center",
            padding="1020px",
        ),
        P(),
        Div(
            "Portable C++ GPU Compute using native WebGPU",
            align="center",
        ),
        P(),
        # Links
        Div(

            Div(
                A("GitHub", href="https://github.com/AnswerDotAI/gpu.cpp", style="text-decoration: none;"),
                style=box_style + hover_style,
                cls="hover-box",
            ),
            Div(
                A(
                    "Intro Blog",
                    href="https://www.answer.ai/posts/2024-07-11--gpu-cpp.html", style="text-decoration: none;"
                ),
                style=box_style,
                cls="hover-box",
            ),
            Br(),
            Div(
                A("API Docs", href="api/index.html", style="text-decoration: none;"),
                style=box_style,
                cls="hover-box",
            ),
            Div(
                A("Discord", href="https://discord.gg/zmJVhXsC7f", style="text-decoration: none;"),
                style=box_style,
                cls="hover-box",
            ),
            align="center",
        ),
        P(),
        Div(
                # link color white
                A("Answer.AI", href="https://www.answer.ai", style=f"text-decoration: none; color: #33333399;"),
            align="center",
        ),
        # set height to take up the full window
        style=body_style,
        cls = "crt",
        # style = "crt { animation: fadeIn; } @keyframes fadeIn { 0% { opacity: 0; } 100% { opacity: 1; } } animation: fadeIn 2s;",
        # style = ".crt { animation: flicker; } @keyframes flicker { 0%, 100% { opacity: 0.6; } 50% { opacity: 0.8; } } @keyframes fadeIn { 0% { opacity: 0; } 100% { opacity: 1; } } animation: fadeIn 2s;",
    )


if __name__ == "__main__":
    run_uv(
        fname=None,
        app="app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
