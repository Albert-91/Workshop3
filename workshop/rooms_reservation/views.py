from django.http import HttpResponse
from django.shortcuts import render


def decor_warp_html(form):
    def warp_html(*args, **kwargs):
        result = """
            <html>
                <body>
                    <table border=1>
                        {}
                    </table>
                </body>
            </html>""".format(form(*args, **kwargs))
        return HttpResponse(result)
    return warp_html