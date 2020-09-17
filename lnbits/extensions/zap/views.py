from flask import g, render_template

from lnbits.decorators import check_user_exists, validate_uuids
from lnbits.extensions.zap import zap_ext


@zap_ext.route("/")
@validate_uuids(["usr"], required=True)
@check_user_exists()
def index():
    return render_template("zap/index.html", user=g.user)
