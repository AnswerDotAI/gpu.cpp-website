from fasthtml.common import *
import uvicorn

# Shoelace components
from fasthtml.components import (
    Sl_icon,
    Sl_button,
    Sl_menu,
    Sl_menu_item,
    Sl_menu_item,
    Sl_menu_item,
    Sl_breadcrumb,
    Sl_breadcrumb_item,
    Sl_breadcrumb_item,
    Sl_card,
)

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
    return Title("FastHTML"), Body(
        Nav(
            Sl_icon("home"),
            Menu('foo', 'Foo', '/foo'),
            Menu('bar', 'Bar', '/bar'),
            ),

        Br(),
        Div(H1("gpu.cpp"), align="center", style="font-size: 10em"),
        Div(H4("Portable GPU Compute Made Simple"), align="center"),
        Div(
            Img(src="images/shadertui.gif", style="height: 300px"),
            Img(src="images/pendulum.gif", style="height: 300px"),
            align="center",
        ),
        Div(
            A("Blog Post", href="https://www.answer.ai/posts/2024-07-11--gpu-cpp.html"),
            Br(),
            A("API Docs", href="api/index.html"),
            Br(),
            A("GitHub", href="https://github.com/AnswerDotAI/gpu.cpp"),
            Br(),
            A("Discord", href="https://discord.gg/zmJVhXsC7f"),
            align="center",
        ),
    )


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
    run_uv(fname=None, app="app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
